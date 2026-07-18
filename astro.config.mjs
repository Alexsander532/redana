import { defineConfig } from 'astro/config';

export default defineConfig({
  site: 'https://redana.com.br',
  compressHTML: true,
  build: {
    inlineStylesheets: 'auto',
  },
});
