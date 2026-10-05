/** Design tokens for the investment app showcase. */
export const theme = {
  ink: '#1c1c1e',
  muted: '#8a8a8f',
  stage:
    'radial-gradient(ellipse 900px 400px at 50% 110%, #9442ee 0%, #a663ef 28%, #c595f0 52%, rgba(222,190,240,0) 88%), linear-gradient(180deg,#fffdf0 0%,#fcf8ef 16%,#f6edef 30%,#efe1f0 44%,#e7d2f0 58%,#dcbef0 72%,#d0aaf0 100%)',
  bigWord: 'rgba(255,255,255,0.6)',
  portfolioScreen: 'linear-gradient(180deg,#dedcee 0%,#dfdef0 12%,#e6e5f3 22%,#efeff7 30%,#f5f4f9 38%,#f6f5fa 46%,#ffffff 64%,#ffffff 100%)',
  topUpScreen: 'linear-gradient(180deg,#d6e0d8 0%,#d6e1d8 12%,#dce3de 20%,#e2e8e4 28%,#ecf0ec 35%,#f5f7f4 41%,#fbfbfb 48%,#ffffff 56%,#ffffff 100%)',
  chartFill: '#a69bd9',
  translucent: 'rgba(255,255,255,0.45)',
  keyBg: '#ebebeb',
  ethCard: '#adc4fd',
  positive: '#2fa84f',
  cryptoPositive: '#34a01a',
  keyTones: {
    plain: '#ebebeb',
    warning: '#ffd55c',
    danger: '#f59aa7',
    success: '#d2f8db',
    primary: '#1c1c1e',
  },
} as const

export type KeyTone = keyof typeof theme.keyTones
