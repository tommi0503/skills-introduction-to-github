export interface PlanStep {
  amount: string
  when: string
  /** Fraction of the circle filled (0..1). */
  progress: number
}

export const payment = {
  url: 'www.amazon.com',
  title: 'Payment calculator',
  subtitle: ['Use the slider to estimate your payment plan', 'for your next purchase with Pay in 4.'],
  question: 'How much do you plan to spend?',
  amount: '$100',
  /** Slider position, 0..1 of the track. */
  sliderValue: 0.18,
  planTitle: 'Payment plan',
  planBadge: 'Pay in 4',
  steps: [
    { amount: '$25', when: 'Today', progress: 0.25 },
    { amount: '$25', when: 'In 2 weeks', progress: 0.5 },
    { amount: '$25', when: 'In 4 weeks', progress: 0.75 },
    { amount: '$25', when: 'In 6 weeks', progress: 1 },
  ] satisfies PlanStep[],
  activeStep: 0,
  note: 'No interest. No credit impact.',
  feedback: ['Did this help you', 'understand how Pay in 4', 'works?'],
}

export interface RatingOption {
  label: string
  selected?: boolean
}

export const support = {
  header: 'Support',
  headerSub: 'Helping you 24/7',
  messageTime: '23:18',
  title: ['How was your support', 'experience?'],
  skip: 'Skip',
  subtitle: 'Please rate our support to help us improve',
  ratings: [{ label: 'Poor' }, { label: 'Great' }, { label: 'Wow', selected: true }] satisfies RatingOption[],
  reasonsTitle: 'Why did you love it?',
  reasons: ['App Functionality', 'Product Experience', 'Support Journey', "Agent's Approach", 'Chat Outcome'],
  action: 'Submit',
}

export const delivery = {
  searchPlaceholder: 'What can we get you?',
  address: 'Carrer de Còrsega, 344',
  categories: ['Groceries', 'SuperGlovo'],
  title: ['How was your experience', 'with Support?'],
  stars: 5,
  prompt: 'That’s great. What did you like?',
  options: [
    ['Clear communications', 'Effective solution'],
    ['Fast resolution', 'Smooth experience'],
    ['Other'],
  ],
  selected: 'Smooth experience',
  action: 'Done',
}

export const run = {
  time: '1:45',
  sheetTitle: 'A Rainy Run',
  question: ['We noticed you ended the', 'Guided Run early. What did you', 'think?'],
  moreTitle: 'Tell Us More',
  tags: [['Good Coaching', 'Would Run Again'], ['Inspiring', 'Music', 'Motivating'], ['Fun', 'Would Recommend']],
  action: 'Submit',
  footer: 'Your feedback helps us improve our guided runs',
}
