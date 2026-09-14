import { defineConfig, type Plugin } from 'vite';
import react from '@vitejs/plugin-react';
import { fileURLToPath } from 'node:url';

const repositoryRoot = fileURLToPath(new URL('../../', import.meta.url));
function identity(): Plugin {
  const middleware = (req: any, res: any, next: () => void) => {
    if (req.url?.split('?')[0] !== '/__atlas_experiment') return next();
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify({ appName: 'FLOW Atlas Exploration', repositoryRoot, pid: process.pid }));
  };
  return { name: 'atlas-experiment-identity', configureServer: s => { s.middlewares.use(middleware); }, configurePreviewServer: s => { s.middlewares.use(middleware); } };
}
const proxy = { '/api': 'http://127.0.0.1:8765' };
export default defineConfig({
  plugins: [react(), identity()],
  server: { host: '127.0.0.1', port: 8767, strictPort: true, proxy },
  preview: { host: '127.0.0.1', port: 8767, strictPort: true, proxy },
  build: { chunkSizeWarningLimit: 1700 }
});
