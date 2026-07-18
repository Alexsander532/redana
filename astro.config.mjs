import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://notacerta.com.br',
  compressHTML: true,
  build: {
    inlineStylesheets: 'auto',
  },
});
