export const brand = 'SalesTrigger'
export const hero = ['AI-SDR as a Service', 'for LinkedIn']
export const funnel = {
  title: 'How sales works on LinkedIn', sub: 'Comparison of funnel stages',
  rows: [
    { label: 'Search for clients', tag: '5 hours', pct: '20%', w: 250 },
    { label: 'Creating messages', tag: '6 hours', pct: '10%', w: 250 },
    { label: 'Sending requests', pct: '25%', w: 170 },
    { label: 'Dialogue support', pct: '10%', w: 175 },
    { label: 'Engagement', tag: '10 o’clock', pct: '4%', w: 140, extra: ['-100%', '+11x'] },
  ],
}
export const process = {
  title: ['How sales works', 'on LinkedIn'],
  cols: [
    { tag: '>5 hours', text: 'Collecting potential clients, analyzing profiles and data', step: 'Search for leads' },
    { tag: '>6 hours', text: 'Creation of personalized texts for the target audience. SDRs select tone, structure and wording for first contact', step: 'Writing messages' },
    { tag: '10-15%', text: 'Automation of mailings, launching follow-up chains', step: 'Sending messages before the first response' },
    { tag: '>10 hours/week', tag2: '4-10%', text: 'SDRs continue to communicate manually, answer questions and arrange a call or meeting', step: 'Conduct dialogues and bring to meetings' },
  ],
}
export const market = {
  title: 'Market potential (2024-2030)', source: 'Source: Statista via JonDenies',
  bars: [
    { name: ['B2B Digital', 'Marketing/', 'Advertising'], cagr: 'CAGR + 12%', value: '$50B → $113B', x: 12, y: 41, w: 103, h: 187, color: '#2f6df6' },
    { name: ['Sales', 'Enablement', 'Platforms'], cagr: 'CAGR + 13%', value: '$5.4B → $12.8', x: 119, y: 60, w: 101, h: 168, color: '#76a6f9' },
    { name: ['AI-SDR'], cagr: 'CAGR + 17%', value: '$4.1B → $9', x: 225, y: 105, w: 160, h: 123, color: '#ee6a1c' },
  ],
}
