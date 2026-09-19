import { fileURLToPath, pathToFileURL } from 'node:url';
import { createRequire } from 'node:module';
import path from 'node:path';

const requireApp = createRequire(new URL('../../app/package.json', import.meta.url));
const { default: react } = await import(pathToFileURL(requireApp.resolve('@vitejs/plugin-react')).href);
const root = fileURLToPath(new URL('.', import.meta.url));
export default {
  root,
  plugins: [react()],
  resolve: { alias: Object.fromEntries(['react', 'react-dom'].map(name => [name, path.dirname(requireApp.resolve(name + '/package.json'))])) },
  server: {
    host: '127.0.0.1', port: 5174, strictPort: true,
    proxy: { '/api': { target: 'http://127.0.0.1:8765', changeOrigin: true } },
    fs: { allow: [root, ...['../../app/src', '../../app/node_modules'].map(relative => fileURLToPath(new URL(relative, import.meta.url)))] },
  },
  build: { outDir: fileURLToPath(new URL('../../app/.runtime/branding/preview-dist', import.meta.url)), emptyOutDir: true },
};
