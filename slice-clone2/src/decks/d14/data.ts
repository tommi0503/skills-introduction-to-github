const intro = 'This page is an introductory page'
const forTopic = 'for your content topic.'

export const cover = {
  title: ['Organic Brand', 'Proposal'],
  sub: 'A Mission-Driven Business Proposal',
  body: ['This page is an introductory page for your content topic.', 'Please add a brief introduction to your topic here.'],
}

export const mission = {
  title: ['Mission &', 'Values'],
  body: [intro, forTopic],
  cards: ['Trust', 'Responsibility', 'Innovation', 'Sustainability'].map((k) => ({ k, body: [intro, forTopic] })),
}

export const philosophy = {
  title: 'Brand Philosophy',
  sub: 'Starting Point for a Sustainable Future',
  body: 'This page is an introductory page for your content topic.',
  circles: ['Philosophy', 'Vision', 'Purpose'].map((k, i) => ({ no: `0${i + 1}`, k })),
}

export const problem = {
  title: ['Problem &', 'Solution'],
  body: ['Please add a short description', 'about the topic. Explain the relevant', 'details that are related to the', 'relevant information.'],
  cards: [
    { k: 'Problem', body: ['Organic labeling no longer', 'guarantees trust'] },
    { k: 'Solution', body: ['Overused claims, certification', 'confusion, and limited accessibility', 'challenge consumer confidence'] },
  ],
}

export const market = {
  kicker: 'Food, Beauty, Fashion Growth',
  title: ['Green Market', 'Growth'],
  body: [intro, forTopic],
  ticks: [200, 150, 100, 50, 0],
  values: [35, 60, 100, 185],
}

export const delivery = {
  title: 'Delivery Diagram',
  sub: 'Transparent Value Chain',
  body: 'This page is an introductory page for your content topic.',
  center: 'Value Chain',
  text: ['This page is an introductory', 'page for your content topic.'],
  esgText: ['This page is an introductory page', 'for your content topic.'],
}

export const positioning = {
  title: ['Market', 'Positioning Map'],
  body: [intro, forTopic],
  axes: [
    { text: 'High Authenticity', cx: 804, cy: 199, w: 237 },
    { text: 'Low Price', cx: 495, cy: 405, w: 164 },
    { text: 'High Price', cx: 1127, cy: 405, w: 164 },
    { text: 'Low Authenticity', cx: 804, cy: 621, w: 237 },
  ],
  brands: [
    { k: 'A Brand', x: 606, y: 306, ours: false },
    { k: 'B Brand', x: 652, y: 360, ours: false },
    { k: 'Our brand', x: 858, y: 334, ours: true },
    { k: 'C Brand', x: 631, y: 504, ours: false },
    { k: 'D Brand', x: 865, y: 489, ours: false },
  ],
}

const bio = ['This page is an introductory page for', 'your content topic. Please add a brief', 'introduction to your topic here.']
export const team = {
  title: 'Our Team',
  sub: 'Experienced & Passionate Leaders',
  members: [
    { name: 'Alex Morgan', role: 'Creative Director', x: 171 },
    { name: 'Casey Taylor', role: 'Product Designer', x: 524 },
    { name: 'Jordan Lee', role: 'Brand Storyteller', x: 867 },
  ].map((m) => ({ ...m, bio })),
}

export const traction = {
  kicker: 'Growth Metrics',
  title: 'Traction',
  body: [intro, forTopic],
  ticks: [80, 60, 40, 20, 0],
  series: [[25, 45, 75], [15, 30, 50], [10, 15, 20]],
  metrics: [{ k: 'Users', v: '250K' }, { k: 'Revenue', v: '$1,2M' }, { k: 'Downloads', v: '500K' }],
}

export const figures = {
  title: 'Traction',
  desc: ['Please add a short description about the topic.', 'Explain the relevant details that are related to the relevant information.'],
}
