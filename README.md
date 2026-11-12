# Oelewappers

Profiles live in `src/politicians.json`; names, parties, and portraits were matched against the official [current Tweede Kamer members list](https://www.tweedekamer.nl/kamerleden_en_commissies/alle_kamerleden). To keep the page accurate when membership changes, refresh this small list from that source.

## Run locally

```sh
npm install
npm run dev
```

## Build for Vercel

Import this folder as a Vite project in Vercel; its defaults work. Or run `npm run build` and deploy the generated `dist/` directory. No server-side configuration or environment variables are needed.
