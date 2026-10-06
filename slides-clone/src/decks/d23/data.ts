export interface PillData { label: string; x: number; y: number; w: number }
export const cover = {
  brand: 'vero',
  nav: 'Action',
  page: 'Page 01',
  title: ['LET’S BUILD', 'THE FUTURE', 'OF REAL-TIME', 'AI SUPPORT', 'TOGETHER.'],
  contact: ['hello@vero.ai', 'www.vero.ai'],
  pills: [
    { label: 'EARLY ADOPTERS', x: 446, y: 436, w: 206 },
    { label: 'STRATEGIC PARTNERSHIPS', x: 968, y: 404, w: 276 },
    { label: 'INVESTMENT CONVERSATIONS', x: 640, y: 612, w: 310 },
  ] as PillData[],
}
