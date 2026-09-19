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
    entry.element_type, entry.relationship, entry.similarities, entry.differences, entry.flow_position]
    .map(value => marketText(value)).filter(Boolean).join('\n')).join('\n');
}
