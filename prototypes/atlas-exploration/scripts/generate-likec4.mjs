import { mkdir, readFile, writeFile } from 'node:fs/promises';
import { dirname, resolve } from 'node:path';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';
import { loadPublication } from './load-publication.mjs';
import { projectLikeC4 } from './project-likec4.mjs';

const prototypeRoot = resolve(dirname(fileURLToPath(import.meta.url)), '..');
const version = process.argv.find(arg => arg.startsWith('--version='))?.slice('--version='.length);
const publication = await loadPublication({ version });
const { dsl, manifest } = projectLikeC4(publication.raw, publication.descriptor);
const generatedRoot = resolve(prototypeRoot, '.generated');
const dslRoot = resolve(generatedRoot, 'likec4');
await mkdir(dslRoot, { recursive: true });
await writeFile(resolve(dslRoot, 'atlas.c4'), dsl, 'utf8');
await writeFile(resolve(generatedRoot, 'likec4-manifest.json'), `${JSON.stringify(manifest, null, 2)}\n`, 'utf8');
const packageRoot = resolve(prototypeRoot, 'node_modules/likec4');
const packageJson = JSON.parse(await readFile(resolve(packageRoot, 'package.json'), 'utf8'));
const binary = resolve(packageRoot, typeof packageJson.bin === 'string' ? packageJson.bin : packageJson.bin.likec4);
const result = spawnSync(process.execPath, [binary, 'gen', 'react', dslRoot, '--outfile', resolve(generatedRoot, 'likec4.generated.js')], {
  cwd: prototypeRoot,
  stdio: 'inherit',
  windowsHide: true,
  env: { ...process.env, NO_COLOR: '1' },
});
if (result.error) throw result.error;
if (result.status !== 0) process.exit(result.status ?? 1);
console.log(`LikeC4 generated: ${manifest.publication}, ${Object.keys(manifest.atlasToLikeC4).length} published elements; original relation IDs retained.`);
