import type { JsonRecord } from './types.ts';
import { publicText } from './publicText.ts';

export interface ReaderExample {
  title: string; situation: string; outcome?: string; lesson?: string;
  trigger?: string; objective?: string; constraints?: string[];
  options?: { title: string; description: string }[];
  contributions?: { node_id: string; role: string }[];
  sourceNode?: string; contribution?: string;
}
type ResolveFields = (id: string) => Readonly<JsonRecord> | undefined;

function structuredExample(value: unknown): ReaderExample[] {
  if (!value || typeof value !== 'object') return [];
  const item = value as JsonRecord;
  if (typeof item.title !== 'string' || typeof item.situation !== 'string') return [];
  const result: ReaderExample = { title: publicText(item.title), situation: publicText(item.situation) };
  for (const key of ['outcome', 'lesson', 'trigger', 'objective'] as const) {
    if (typeof item[key] === 'string') result[key] = publicText(item[key]);
  }
  if (Array.isArray(item.constraints)) result.constraints = item.constraints.filter((v): v is string => typeof v === 'string').map(publicText);
  if (Array.isArray(item.options)) result.options = item.options.flatMap(v =>
    v && typeof v.title === 'string' && typeof v.description === 'string'
      ? [{ title: publicText(v.title), description: publicText(v.description) }] : []);
  if (Array.isArray(item.contributions)) result.contributions = item.contributions.flatMap(v =>
    v && typeof v.node_id === 'string' && typeof v.role === 'string'
      ? [{ node_id: v.node_id, role: publicText(v.role) }] : []);
  return [result];
}

/** Read this snapshot only. Explicit examples in old scopes remain readable;
 * never manufacture a scenario from a definition or fetch one from the backlog. */
export function businessExamples(fields: Readonly<JsonRecord>, resolve?: ResolveFields): ReaderExample[] {
  const local = localExamples(fields);
  const shared = Array.isArray(fields.scenario_refs) ? fields.scenario_refs.flatMap(ref => {
    if (!ref || typeof ref.node_id !== 'string' || typeof ref.scenario_id !== 'string') return [];
    const source = resolve?.(ref.node_id);
    const example = Array.isArray(source?.examples) ? source.examples.find(item => item?.id === ref.scenario_id) : undefined;
    return structuredExample(example).map(item => ({ ...item, sourceNode: ref.node_id,
      ...(typeof ref.contribution === 'string' ? { contribution: publicText(ref.contribution) } : {}) }));
  }) : [];
  return [...local, ...shared];
}

function localExamples(fields: Readonly<JsonRecord>): ReaderExample[] {
  if (Array.isArray(fields.examples)) return fields.examples.flatMap(structuredExample);
  const scope = typeof fields.scope === 'string' ? publicText(fields.scope) : '';
  const examples = scope.split(/\n\s*\n/).flatMap(paragraph => {
    const marker = /\bExemples?(?:\s+(?:métier|fictifs?|simplifi[ée]s?|illustratifs?|concrets?|discut[ée]s?)){0,3}(?:\s+(?:FLOW|textile))?\s*(?::|\.\*\*)\s*/i.exec(paragraph);
    if (!marker) return [];
    const situation = paragraph.slice(marker.index + marker[0].length).trim();
    return situation ? [{ title: 'Exemple illustratif', situation }] : [];
  });
  return examples.filter((example, index) => examples.findIndex(other => other.situation === example.situation) === index);
}

export function exampleSearchText(fields: Readonly<JsonRecord>, resolve?: ResolveFields): string {
  return businessExamples(fields, resolve).map(e => [e.title, e.situation, e.outcome, e.lesson, e.trigger, e.objective,
    ...(e.constraints || []), ...(e.options || []).map(o => `${o.title} ${o.description}`),
    ...(e.contributions || []).map(c => c.role), e.contribution].filter(Boolean).join('\n')).join('\n');
}
