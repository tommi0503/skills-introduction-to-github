export const brand = { name: 'DigiCorp', blue: '#0a49ff' }
export interface Task { label: string; start: number; done: number; end: number; pct: string; note: string; y: number; active?: boolean }
export const progress = {
  section: 'Progress Projection',
  title: ['Highlighting Progress', 'and Results'],
  tasks: [
    { label: 'Strategic', start: 259, done: 296, end: 330, pct: '30%', y: 350, note: 'Complete and refine the technology roadmap, ensuring 5 steps.' },
    { label: 'Allocate Resources', start: 277, done: 348, end: 413, pct: '60%', y: 409, note: 'Distribute resources effectively to support critical projects.' },
    { label: 'Monitor KPIs', start: 277, done: 431, end: 447, pct: '90%', y: 468, active: true, note: 'Regularly track and assess key performance indicators in gauge.' },
    { label: 'Technology', start: 323, done: 397, end: 432, pct: '70%', y: 530, note: 'Stay agile and responsive by continually evaluating new technologies.' },
  ] as Task[],
}
export const kpi = {
  section: 'Key Performance Indicator',
  title: ['20XX Business', 'Performance'],
  hero: { value: '93,3%', label: ['Customer', 'Satisfaction'] },
  stats: [
    { value: '22,7%', label: 'Revenue Growth' },
    { value: '35%', label: 'Market Penetration' },
    { value: '42', label: 'Employee Net Promoter Score' },
  ],
}
