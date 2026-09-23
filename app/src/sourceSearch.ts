/** Shared matching for source highlighting and its result count. */
export const normalizeSourceText = (text: string): string => text.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase();

export function sourceMatches(text: string, query: string): { start: number; end: number }[] {
  const needle = normalizeSourceText(query.trim());
  if (!needle) return [];
  let flat = '', offset = 0;
  const starts: number[] = [], ends: number[] = [];
  for (const character of text) {
    const normalized = normalizeSourceText(character);
    flat += normalized;
    for (let i = 0; i < normalized.length; i++) {
      starts.push(offset);
      ends.push(offset + character.length);
    }
    if (!normalized && ends.length) ends[ends.length - 1] = offset + character.length;
    offset += character.length;
  }
  const matches: { start: number; end: number }[] = [];
  for (let index = flat.indexOf(needle); index >= 0; index = flat.indexOf(needle, index + needle.length)) {
    matches.push({ start: starts[index], end: ends[index + needle.length - 1] });
  }
  return matches;
}
