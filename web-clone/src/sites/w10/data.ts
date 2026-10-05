/** Content + layout data for the Giga clone (frame px from reference-dom/10.json and the flat capture). */

export interface Rect {
  x: number
  y: number
  w: number
  h: number
}

export const announcement = { text: 'New: your voice agents can book a callback and place it themselves.', link: 'Learn more' }

export const nav = {
  brand: 'Giga',
  menu: [
    { label: 'Platform', x: 509 },
    { label: 'Solutions', x: 617 },
    { label: 'Industries', x: 731 },
    { label: 'Company', x: 849 },
  ],
  signIn: 'Sign in',
  cta: 'See a demo',
}

export const hero = {
  eyebrow: 'AI Agents for Customer Experience',
  title: ['Fast forward', 'to fixed.'],
  body: 'Giga’s AI agents take action across voice, chat, and email. They complete customer requests, follow up when needed, and pursue relevant sales opportunities.',
  demo: {
    greeting: 'hello',
    prompt: 'Enter your work email to unlock Voice and Chat.',
    placeholder: 'you@company.com',
    submit: 'Continue',
    note: 'Used to personalize your demo and follow up.',
    brand: 'GIGA',
    talk: 'Talk',
    channels: ['Voice', 'Chat'],
  },
}

/** Customer wordmarks in the marquee (logo placeholders). */
export const logos: Rect[] = [
  { x: 110, y: 1601, w: 98, h: 20 },
  { x: 342, y: 1599, w: 89, h: 24 },
  { x: 565, y: 1596, w: 174, h: 29 },
  { x: 873, y: 1600, w: 46, h: 21 },
  { x: 1053, y: 1598, w: 139, h: 25 },
  { x: 1326, y: 1595, w: 103, h: 31 },
]

export const industries = {
  eyebrow: 'Industries',
  title: 'Giga agents are flexible.',
  body: 'Swap rigid workflows for agents that adapt to your industry and its unique needs.',
  cardLead: 'See how Giga will improve your business.',
  cardRest: 'Explore your industry, or leave your work email and we’ll build a page for your company.',
  field: 'Your work email',
  submit: 'Build my page',
  /** Stacked industry photo slices to the right of the form card: [x, width]. */
  slices: [
    [771, 246],
    [1017, 124],
    [1141, 61],
    [1202, 31],
    [1233, 16],
    [1249, 7],
    [1256, 8],
    [1264, 7],
  ] as Array<[number, number]>,
}

export interface ChatItem {
  from: 'user' | 'agent'
  text: string[]
  /** Tool-call label shown above an agent reply. */
  tool?: string
  detail?: string
  open?: boolean
  top: number
  right?: number
  width?: number
}

export const agents = {
  title: ['Agents that keep', 'getting better.'],
  body: ['Orders, billing, accounts, and subscriptions, updated', 'during the conversation.'],
  steps: ['The customer asks', 'Giga checks the order', 'Giga calls the driver', 'Giga confirms', 'Giga gets better'],
  activeStep: 4,
  chat: {
    status: 'waiting',
    moodLabel: 'Mood',
    mood: 'Moving on',
    input: 'Message',
    brand: 'GIGA',
    channel: 'Chat',
    items: [
      { from: 'user', text: ['Help. My dinner is on its way to my ex’s', 'place. My date arrives in 30 minutes.'], top: 2702, width: 277 },
      { from: 'agent', tool: 'Order checked', text: ['I can still catch it. Your new address is farther, so it’s $3.80', 'more. Should I call the driver?'], top: 2797 },
      { from: 'user', text: ['Yes. Hurry.'], top: 2900, width: 91 },
      { from: 'agent', tool: 'Driver called', text: ['Done. It arrives 8 minutes before your date. Should I delete', 'the old address?'], top: 2974 },
      { from: 'user', text: ['Please. Forever.'], top: 3077, width: 126 },
      { from: 'agent', tool: 'Old address deleted', detail: 'Mood detected: moving on', open: true, text: ['Deleted. That leaves you 8 minutes to plate it and take the', 'credit. Enjoy your evening.'], top: 3151 },
    ] satisfies ChatItem[],
  },
}
