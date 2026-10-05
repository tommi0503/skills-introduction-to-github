export type Verdict = 'good' | 'bad'

export interface ExamplePhoto {
  verdict: Verdict
  label: string
}

export const selfieScreen = {
  title: ['Upload a photo of', 'yourself holding your ID'],
  examples: [
    { verdict: 'good', label: 'Correct example' },
    { verdict: 'bad', label: 'Wrong example' },
  ] satisfies ExamplePhoto[],
  tips: ['To get it right make sure the photo is taken in good light', 'Details are in focus', 'There is no glare on the ID'],
  action: 'Continue',
}

export const nationalIdScreen = {
  title: 'National ID',
  subtitle: 'Upload a photo or scan of your document.',
  link: 'Choose a different ID document',
  slides: ['Upload the front side of your document', 'Upload the back side of your document'],
  activeSlide: 0,
  action: 'Continue',
}
