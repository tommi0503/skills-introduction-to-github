export const roadmap = [
  { date: 'October 2025', mau: '6k', users: '150', items: ['AI Inbox', 'First users', 'Integration with Make, n8n'] },
  { date: '1st quarter 2026', mau: '15k', users: '400', items: ['AI-SDR', 'Lead management'] },
  { date: '3rd quarter 2026', mau: '120k', users: '1 800', items: ['AI Person Engine', 'Team management'] },
  { date: '1st quarter 2027', mau: '250k', users: '3 500', items: ['AI Writer', 'Integrations with CRM and calendar'] },
  { date: '3rd quarter 2027', mau: '1M', users: '8,000', items: ['New SDR with email outreach', 'SDR for transaction management'] },
]
export const journey = {
  title: ['From lead generation agency', 'to AI-SDR for LinkedIn'],
  sub: ["We've gone through the entire LinkedIn", 'sales cycle and are turning it into a product'],
  points: [
    { name: 'Start', date: '2023', text: ['Launched a LinkedIn B2B', 'agency'], x: 10, y: 137, dx: 16, dy: 145 },
    { name: 'Growth', date: 'June 2024', text: ['Built intel lead-gen (events) →', 'buyers need meetings'], x: 74, y: 92, dx: 80, dy: 100 },
    { name: 'Pivot', date: 'July 2025', text: ['Focused on outreach, kept intent', 'module'], x: 161, y: 57, dx: 166, dy: 70 },
    { name: 'Sales', date: 'Sep 2025', text: ['We received our first paying users'], x: 246, y: 14, dx: 250, dy: 26 },
  ],
  cards: [
    { x: 181, title: 'Why us?', rows: [['3 years in B2B', 'Antispam, paysmoke, deliverability — automated'], ['Sold to product', 'Founder-market fit before they started scaling it'], ["Let's not stop", 'Agency -> data -> product -> AI-SDR']] },
    { x: 263, title: 'Key insights', rows: [['Payback', 'Without automation, LinkedIn lead gen does not scale'], ['Market', 'We tackle — depends on workflow coverage'], ['Demand', 'Teams want their own AI-SDR, not a tool']] },
  ],
}
export const market = {
  items: [
    { name: 'B2B Digital Marketing/Advertising', value: '$50B → $113B', color: '#2f6df6' },
    { name: 'Sales Enablement Platforms', value: '$5.4B → $12.8', color: '#b9cdf5' },
    { name: 'AI-SDR', value: '$4B → $138', color: '#ee6a1c' },
    { name: 'Linkedin automation', value: '$0.6B → $1.9B', color: '#f6c6b8' },
  ],
  callouts: [
    { t: 'CAGR + 12%', x: 212, y: 53, orange: false }, { t: 'CAGR + 13%', x: 248, y: 121, orange: false },
    { t: 'CAGR + 17%', x: 178, y: 137, orange: true }, { t: 'CAGR + 15%', x: 262, y: 158, orange: true },
  ],
}
export const contacts = {
  raising: { label: 'We are raising', value: '500K' },
  split: [{ v: '15%', l: 'Team', x: 92, w: 37, c: '#f0721a' }, { v: '15%', l: 'Advertising', x: 129, w: 37, c: '#f5964f' }, { v: '70%', l: 'Development', x: 166, w: 175, c: '#f8cdb8' }],
  lines: ['Tg: @Andreyshpa', 'Mail: CEO@Salestrigger.in', 'LinkedIn: linkedin.com/in/andreyshpa'],
}
