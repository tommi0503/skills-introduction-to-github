/** One block of an assistant response (rendered in the serif reading face). */
export type ResponseBlock =
  | { kind: 'p'; text: string }
  | { kind: 'h'; text: string }
  | { kind: 'li'; lead?: string; text: string; trailing?: 'broccoli' | 'droplet' }

export const composer = {
  model: 'Sonnet 4.6',
  effort: 'Low',
  chatPlaceholder: 'Chat with Claude',
  replyPlaceholder: 'Reply to Claude',
}

export const emptyChat = {
  greeting: 'Lex returns!',
  banner: { text: 'Get more with Claude Pro', action: 'Upgrade' },
}

export interface PlanOption {
  key: string
  price: string
  billing: string
  selected?: boolean
  badge?: string
}

export const plans = {
  title: 'Get more Claude',
  subtitle: 'Choose the plan that’s right for you',
  pro: {
    name: 'Pro',
    tagline: 'For everyday productivity',
    options: [
      { key: 'monthly', price: 'S$ 29.98', billing: 'Billed monthly' },
      { key: 'annual', price: 'S$ 299.98', billing: 'Billed annually', selected: true, badge: 'Save 17%' },
    ] satisfies PlanOption[],
    cta: 'Get Pro plan',
    includesTitle: 'Everything in Free, plus:',
    includes: [
      'Send more messages with Claude Pro',
      'Access more Claude models',
      'Organize chats and documents with unlimited Projects',
    ],
    footnote: 'Limits apply',
  },
  max: { name: 'Max', tagline: '5x or 20x more usage than Pro' },
}

export const conversation = {
  prompt: 'Give me a 2-day healthy meal plan',
  notification: {
    title: 'Turn On Response Notifications',
    body: 'Feel free to step away, we will notify you as soon as Claude responds.',
    action: 'Turn On',
  },
  response: [
    { kind: 'p', text: 'Here’s a simple 2-day healthy meal plan:' },
    { kind: 'h', text: 'Day 1' },
    { kind: 'li', lead: 'Breakfast:', text: 'Oatmeal with banana slices and a drizzle of honey' },
    { kind: 'li', lead: 'Lunch:', text: 'Turkey and cheese sandwich on whole wheat bread with baby carrots' },
    { kind: 'li', lead: 'Dinner:', text: 'Baked chicken, brown rice, and steamed broccoli' },
    { kind: 'li', lead: 'Snack:', text: 'Apple slices with peanut butter' },
    { kind: 'h', text: 'Day 2' },
    { kind: 'li', lead: 'Breakfast:', text: 'Scrambled eggs with whole wheat toast and orange juice' },
    { kind: 'li', lead: 'Lunch:', text: 'Veggie wrap with hummus, cucumber, and shredded cheese' },
    { kind: 'li', lead: 'Dinner:', text: 'Salmon with sweet potato and green beans' },
    { kind: 'li', lead: 'Snack:', text: 'Greek yogurt with a handful of berries' },
    { kind: 'h', text: 'Easy rules to remember:' },
    { kind: 'li', text: 'Half your plate = fruits & veggies', trailing: 'broccoli' },
    { kind: 'li', text: 'Drink water instead of soda', trailing: 'droplet' },
    { kind: 'li', text: 'Pick whole wheat bread over white bread — it keeps you full longer!' },
  ] satisfies ResponseBlock[] as ResponseBlock[],
  disclaimer: 'Claude is AI and can make mistakes.\nPlease double-check responses.',
}
