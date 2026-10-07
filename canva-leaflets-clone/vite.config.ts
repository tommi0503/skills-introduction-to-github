import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'
import {fileURLToPath} from 'node:url'
import {realpathSync} from 'node:fs'
export default defineConfig({plugins:[react(),tailwindcss()],server:{fs:{allow:[fileURLToPath(new URL('..',import.meta.url)),realpathSync(fileURLToPath(new URL('./node_modules',import.meta.url)))]}}})
