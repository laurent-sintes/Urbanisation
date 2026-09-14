import { test } from 'node:test';
import assert from 'node:assert/strict';
import {
  adaptCatalog, createPublicationClient, fetchJson,
  publicationUrl, sourceUrl,
} from './src/publication.ts';

const snapshot = version => ({
  space: 'release', version,
  nodes: [{ id: 'stable', kind: 'domain', fields: { name: 'Stable in ' + version }, source_refs: [], review: { state: 'proposed' } }],
  relations: [],
});
const catalog = (current = 'v3', versions = ['v3', 'v2', 'v1']) => ({ current_version: current, versions: versions.map(version => ({ version, revision: Number(version.slice(1)) })) });
const response = (value, status = 200) => new Response(JSON.stringify(value), { status, headers: { 'content-type': 'application/json' } });
const deferred = () => {
  let resolve, reject;
  const promise = new Promise((yes, no) => { resolve = yes; reject = no; });
  return { promise, resolve, reject };
};

test('API catalog identity and server order are preserved without filename inference', () => {
  const result = adaptCatalog(catalog('v2', ['v3', 'v2', 'v1']));
  assert.equal(result.current, 'v2');
  assert.deepEqual(result.releases.map(item => item.version), ['v3', 'v2', 'v1']);
  assert.throws(() => adaptCatalog(catalog('absent')), /absente/);
  assert.throws(() => adaptCatalog(catalog('v3', ['v3', 'v3'])), /dupliquée/);
  assert.throws(() => adaptCatalog({ versions: [] }), /invalide/);
});

test('current load follows explicit catalog pointer and pins its model request', async () => {
  const calls = [];
  const client = createPublicationClient(async (url, init) => {
    calls.push(url);
    assert.equal(init.cache, 'no-store');
    assert.ok(init.signal instanceof AbortSignal);
    return response(url === '/api/releases' ? catalog('v2') : snapshot('v2'));
  });
  await client.setVersion();
  assert.deepEqual(calls, ['/api/releases', '/api/model?version=v2']);
  assert.equal(client.getState().model.version, 'v2');
  assert.equal(client.getState().loading, false);
  client.dispose();
});

test('periodic check refreshes current on a new pointer, and preserves unchanged model identity', async () => {
  let current = 'v2';
  let modelReads = 0;
  const client = createPublicationClient(async url => {
    if (url === '/api/releases') return response(catalog(current));
    modelReads++;
    return response(snapshot(new URL(url, 'http://local').searchParams.get('version')));
  });
  await client.setVersion();
  const initial = client.getState().model;
  await client.check();
  assert.equal(client.getState().model, initial);
  assert.equal(modelReads, 1);
  current = 'v3';
  await client.check();
  assert.equal(client.getState().model.version, 'v3');
  assert.equal(modelReads, 2);
  assert.equal(client.getState().model.nodeById.has('stable'), true);
  client.dispose();
});

test('historical selection stays fixed when the current publication changes', async () => {
  let current = 'v2';
  const calls = [];
  const client = createPublicationClient(async url => {
    calls.push(url);
    return response(url === '/api/releases' ? catalog(current) : snapshot('v1'));
  });
  await client.setVersion('v1');
  current = 'v3';
  await client.check();
  assert.equal(client.getState().model.version, 'v1');
  assert.equal(client.getState().catalog.current, 'v3');
  assert.equal(calls.filter(url => url.startsWith('/api/model')).length, 1);
  client.dispose();
});

test('an explicitly pinned current version becomes historical without following a new pointer', async () => {
  let current = 'v2';
  const client = createPublicationClient(async url => response(url === '/api/releases' ? catalog(current) : snapshot('v2')));
  await client.setVersion('v2');
  current = 'v3';
  await client.check();
  assert.equal(client.getState().model.version, 'v2');
  assert.equal(client.getState().catalog.current, 'v3');
  client.dispose();
});

test('failed current refresh keeps previous publication and automatically retries its new target', async () => {
  let current = 'v2';
  let failing = false;
  const client = createPublicationClient(async url => {
    if (url === '/api/releases') return response(catalog(current));
    if (failing) return response({ error: 'Publication momentanément indisponible' }, 503);
    return response(snapshot(current));
  });
  await client.setVersion();
  current = 'v3';
  failing = true;
  await client.check();
  assert.equal(client.getState().model.version, 'v2');
  assert.match(client.getState().notice, /v2 reste affichée/);
  assert.equal(client.getState().error, '');
  failing = false;
  await client.check();
  assert.equal(client.getState().model.version, 'v3');
  assert.equal(client.getState().notice, '');
  client.dispose();
});

test('failed manual refresh retries even if the selected immutable version did not change', async () => {
  let failing = false;
  let modelReads = 0;
  const client = createPublicationClient(async url => {
    if (url === '/api/releases') return response(catalog());
    modelReads++;
    if (failing) throw new Error('offline');
    return response(snapshot('v3'));
  });
  await client.setVersion();
  failing = true;
  await client.reload();
  assert.match(client.getState().notice, /offline/);
  failing = false;
  await client.check();
  assert.equal(modelReads, 3);
  assert.equal(client.getState().notice, '');
  client.dispose();
});

test('changing to unavailable history clears current data without any fallback', async () => {
  const calls = [];
  const client = createPublicationClient(async url => {
    calls.push(url);
    if (url === '/api/releases') return response(catalog());
    return response(snapshot('v3'));
  });
  await client.setVersion();
  const pending = client.setVersion('missing');
  assert.equal(client.getState().model, undefined);
  await pending;
  assert.equal(client.getState().model, undefined);
  assert.match(client.getState().error, /missing/);
  assert.equal(calls.filter(url => url.startsWith('/api/model')).length, 1);
  client.dispose();
});

test('historical model HTTP failure never falls back to a different publication', async () => {
  const calls = [];
  const client = createPublicationClient(async url => {
    calls.push(url);
    return url === '/api/releases' ? response(catalog()) : response({ error: { message: 'Historique indisponible' } }, 404);
  });
  await client.setVersion('v1');
  assert.equal(client.getState().model, undefined);
  assert.match(client.getState().error, /Historique indisponible/);
  assert.deepEqual(calls, ['/api/releases', '/api/model?version=v1']);
  client.dispose();
});

test('unexpected model identity is rejected rather than accepted as historical data', async () => {
  const client = createPublicationClient(async url => response(url === '/api/releases' ? catalog() : snapshot('v3')));
  await client.setVersion('v1');
  assert.equal(client.getState().model, undefined);
  assert.match(client.getState().error, /ne correspond pas/);
  client.dispose();
});

test('obsolete requests are aborted and ignored even when transport ignores AbortSignal', async () => {
  const oldResponse = deferred();
  const oldStarted = deferred();
  let oldSignal;
  const client = createPublicationClient(async (url, init) => {
    if (url === '/api/releases') return response(catalog());
    if (url.endsWith('version=v1')) {
      oldSignal = init.signal;
      oldStarted.resolve();
      return oldResponse.promise;
    }
    return response(snapshot('v2'));
  });
  const first = client.setVersion('v1');
  await oldStarted.promise;
  const next = client.setVersion('v2');
  assert.equal(oldSignal.aborted, true);
  await next;
  oldResponse.resolve(response(snapshot('v1')));
  await first;
  assert.equal(client.getState().model.version, 'v2');
  client.dispose();
});

test('polling coalesces while a request is pending; disposal prevents late updates', async () => {
  const gate = deferred();
  let calls = 0;
  let notifications = 0;
  const client = createPublicationClient(async () => { calls++; return gate.promise; });
  client.subscribe(() => notifications++);
  const pending = client.setVersion();
  const repeated = client.check();
  assert.equal(calls, 1);
  assert.equal(pending, repeated);
  client.dispose();
  const countAtDisposal = notifications;
  gate.resolve(response(catalog()));
  await pending;
  assert.equal(calls, 1);
  assert.equal(notifications, countAtDisposal);
});

test('catalog network failure preserves loaded data and reconnects automatically', async () => {
  let failing = false;
  const client = createPublicationClient(async url => {
    if (failing) throw new Error('Serveur déconnecté');
    return response(url === '/api/releases' ? catalog() : snapshot('v3'));
  });
  await client.setVersion();
  const before = client.getState().model;
  failing = true;
  await client.check();
  assert.equal(client.getState().model, before);
  assert.match(client.getState().notice, /Serveur déconnecté/);
  assert.equal(client.getState().error, '');
  failing = false;
  await client.check();
  assert.equal(client.getState().model.version, 'v3');
  assert.equal(client.getState().notice, '');
  client.dispose();
});

test('malformed initial catalog and HTTP errors expose their concrete error', async () => {
  const client = createPublicationClient(async () => response({ not: 'a catalog' }));
  await client.setVersion();
  assert.equal(client.getState().model, undefined);
  assert.match(client.getState().error, /invalide/);
  client.dispose();
  await assert.rejects(fetchJson('/api/model', undefined, async () => response({ error: 'Service indisponible' }, 503)), /Service indisponible/);
});

test('publication and source URL parameters preserve literal values', () => {
  assert.equal(publicationUrl(), '/api/model');
  assert.equal(publicationUrl('version&other=value'), '/api/model?version=version%26other%3Dvalue');
  assert.equal(new URL(sourceUrl('connaissance/test.md', 'ancre & suite'), 'http://local').searchParams.get('anchor'), 'ancre & suite');
});
