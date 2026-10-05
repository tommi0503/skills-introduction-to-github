/** Design tokens for the Cloudflare clone. */
export const theme = {
  color: {
    page: '#ffffff',
    ink: '#262626',
    inkStrong: '#1f1f1f',
    muted: 'rgba(38,38,38,0.7)',
    subtle: '#707070',
    orange: '#ff5e1f',
    heroOrange: '#fd5c1b',
    alert: '#b52831',
    line: '#f0f0f0',
    border: '#e5e5e5',
    panel: '#fdfdfc',
  },
  font: { sans: "'Archivo Variable', sans-serif" },
  /** Horizontal extent of the dashed page rails. */
  rail: { left: 120, right: 1319 },
} as const
