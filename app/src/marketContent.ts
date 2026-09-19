import type { MarketComparison } from './types.ts';
import { publicText } from './publicText.ts';

/** The comparison is public; adoption history and review annotations stay internal. */
export function marketText(text = ''): string {
  return publicText(text)
    .replace(/Comparaison proposée au titre de U\d+, sans validation ni réalisation installée déduites\./g, '')
    .replace(/\bU\d+(?:\/U\d+)*\s*:\s*/g, '')
    .replace(/\s+(?:adoptés?|adoptées?|validés?|validées?)\s+U\d+(?:\/U\d+)*/g, '')
    .replace(/\s*\(?\b(?:U|CMP|ELM)\d+(?:\/(?:U|CMP|ELM)\d+)*\)?/g, '')
    .replace(/[ \t]+/g, ' ').trim();
}

export function marketSearchText(entries?: readonly MarketComparison[]): string {
  return (entries || []).map(entry => [entry.vendor, entry.product, entry.element_name,
    entry.element_type, entry.relationship, entry.similarities, entry.differences, entry.flow_position, entry.term_choice, entry.definition_choice]
    .map(value => marketText(value)).filter(Boolean).join('\n')).join('\n');
}

/** Put explanations of the actual vocabulary first, preserving order within each group. */
export function marketComparisonsForReading(entries: readonly MarketComparison[] = []): readonly MarketComparison[] {
  const hasChoice = (entry: MarketComparison) => Boolean(entry.term_choice || entry.definition_choice);
  return [...entries.filter(hasChoice), ...entries.filter(entry => !hasChoice(entry))];
}
