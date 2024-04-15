// vite-env.d.ts

declare module 'vite' {
  interface ImportMeta {
    globEager: (pattern: string) => Record<string, any>
  }
}
