import {defineConfig} from 'vite';
export default defineConfig({server:{fs:{allow:['/workspace/skills-introduction-to-github']}},build:{chunkSizeWarningLimit:2000}});
