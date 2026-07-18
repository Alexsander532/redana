# NotaCerta — Landing Page

Landing page minimalista para SaaS de correção de redação do ENEM.

## Stack (SEO/GEO)

- **Astro** — HTML estático, rápido, excelente para SEO
- CSS próprio, sem runtime pesado
- Schema.org (Organization, WebSite, SoftwareApplication, FAQPage)
- Meta tags Open Graph + Twitter
- `lang="pt-BR"`, canonical, robots.txt

## Planos

| Plano      | Preço        | Observação        |
|-----------|--------------|-------------------|
| Free      | R$ 0         | 5 correções grátis |
| Mensal    | R$ 9,90/mês  | Base              |
| Trimestral| R$ 8,40/mês  | 15% off           |
| Anual     | R$ 6,90/mês  | 30% off           |

## Rodar local

```bash
cd notacerta
npm install
npm run dev
```

Build de produção:

```bash
npm run build
npm run preview
```

## Estrutura

```
src/
  layouts/BaseLayout.astro   # SEO + JSON-LD
  pages/index.astro          # Landing completa
  styles/global.css
public/
  favicon.svg
  robots.txt
```
