# Oelewappers

A small, responsive Dutch-politics portrait site: each new page load picks a profile that has not appeared in this browser tab's recent shuffle history. Ten image-led profiles, with portraits credited and linked to their Wikipedia source pages.

## Run locally

```sh
npm install
npm run dev
```

## Build for Vercel

Import this folder as a Vite project in Vercel; its defaults work. Or run `npm run build` and deploy the generated `dist/` directory. No server-side configuration or environment variables are needed.

Profiles and Wikimedia-hosted images live in `src/politicians.json`. Portrait credits with author, license, and source links appear on each page. The portrait shuffle is in `src/profile-picker.js`.
