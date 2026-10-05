/** Design tokens for the Harvey clone. */
export const theme = {
  color: {
    page: '#fafaf9',
    ink: '#0f0e0d',
    inkSoft: '#33312c',
    muted: '#706d66',
    line: '#cccac6',
    onDark: '#fafaf9',
    onDarkSoft: '#cccac6',
    nav: '#0f0e0d',
  },
  font: {
    sans: "'Hanken Grotesk Variable', sans-serif",
    serif: "'Tinos', 'Times New Roman', serif",
  },
  tone: {
    /** Flat stand-ins for the dark textured card backgrounds. */
    cardGreen: '#2f3a39',
    cardBrown: '#3a352c',
  },
} as const
