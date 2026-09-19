import type { JsonRecord } from './types.ts';
import { publicText } from './publicText.ts';

export interface ReaderExample { title: string; situation: string; outcome?: string; lesson?: string }

/** Read this snapshot only. Explicit examples in old scopes remain readable;
 * never manufacture a scenario from a definition or fetch one from the backlog. */
export function businessExamples(fields: Readonly<JsonRecord>): ReaderExample[] {
  if (Array.isArray(fields.examples)) return fields.examples.flatMap(value => {
    if (!value || typeof value !== 'object') return [];
    const item = value as JsonRecord;
    if (typeof item.title !== 'string' || typeof item.situation !== 'string') return [];
    return [{ title: publicText(item.title), situation: publicText(item.situation),
      ...(typeof item.outcome === 'string' ? { outcome: publicText(item.outcome) } : {}),
      ...(typeof item.lesson === 'string' ? { lesson: publicText(item.lesson) } : {}) }];
  });
  const scope = typeof fields.scope === 'string' ? publicText(fields.scope) : '';
  const examples = scope.split(/\n\s*\n/).flatMap(paragraph => {
    const marker = /\bExemples?(?:\s+(?:métier|fictifs?|simplifi[ée]s?|illustratifs?|concrets?|discut[ée]s?)){0,3}(?:\s+(?:FLOW|textile))?\s*(?::|\.\*\*)\s*/i.exec(paragraph);
    if (!marker) return [];
    const situation = paragraph.slice(marker.index + marker[0].length).trim();
    return situation ? [{ title: 'Exemple illustratif', situation }] : [];
  });
  return examples.filter((example, index) => examples.findIndex(other => other.situation === example.situation) === index);
}

export function exampleSearchText(fields: Readonly<JsonRecord>): string {
  return businessExamples(fields).map(example => [example.title, example.situation, example.outcome, example.lesson].filter(Boolean).join('\n')).join('\n');
}
