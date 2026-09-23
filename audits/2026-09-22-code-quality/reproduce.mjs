import { readFileSync } from 'node:fs';
import vm from 'node:vm';
const source = readFileSync(new URL('../../app/src/components/SourceDialog.tsx', import.meta.url), 'utf8');
const normalize = source.match(/const normalize = (.*);/)[1].replace('(text: string)', '(text)');
// Extract the actual loop; only replace React markup by an equivalent text slice.
let highlight = source.slice(source.indexOf('function highlight('), source.indexOf('\nfunction inline('));
highlight = highlight.replace('(text: string, query: string): ReactNode', '(text, query)')
  .replace('parts: ReactNode[]', 'parts')
  .replace('<mark key={index}>{text.slice(index, index + match.length)}</mark>', 'text.slice(index, index + match.length)');
try {
  vm.runInNewContext(`const normalize = ${normalize}; ${highlight}; highlight('texte', '\u0301');`, {}, { timeout: 100 });
  console.log('Completed');
} catch (error) {
  console.log(JSON.stringify({ source: 'SourceDialog.tsx highlight', query: 'U+0301', result: error.message }));
}
