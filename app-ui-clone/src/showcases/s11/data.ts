export interface Shelf {
  title: string
  count: string
  /** Translucent shelf bar colour (null = no shelf, e.g. a faded section). */
  shelf: string | null
  books: number
}

export const shelves: Shelf[] = [
  { title: 'Design', count: '16 books', shelf: 'rgba(240, 150, 50, 0.72)', books: 4 },
  { title: 'Psychology', count: '3 books', shelf: 'rgba(40, 150, 235, 0.72)', books: 3 },
  { title: 'Novels', count: '8 books', shelf: null, books: 4 },
]

export const library = {
  eyebrow: 'My Favourite',
  title: 'BOOKS',
  cta: 'Add Books',
}

export const chapter = {
  eyebrow: 'Chapter 1',
  title: ['The Psychopathology', 'of Everyday Things'],
  dropCap: 'S',
  /** Each entry is one visual line so the justified layout matches the page exactly. */
  lines: [
    'ignifiers are the most important addition to',
    'the chapter, a concept first introduced in my',
    'book Living with Complexity. The first edition',
    'had a focus upon affordances, but although',
    'affordances  Preface to the Revised Edition xv',
    'make sense for interaction with physical',
    'objects, they are confusing when dealing with',
    'virtual ones. As a result, affordances have',
    'created much confusion in the world of design.',
    'Affordances define what actions are possible.',
    'Signifiers specify how people discover those',
    'possibilities: signifiers are signs, perceptible',
    'signals of what can be done. Signifiers are of far',
    'more importance to designers than are',
    'affordances. Hence, the extended treatment. I',
    'added a very brief section on HCD, a term that',
    'didn’t yet exist when the first edition was',
    'published, although looking back, we see that',
    'the entire book was about HCD. Other than',
    'that, the chapter is the same, and although all',
  ],
  faded: ['the photographs and drawings are new, the', 'examples are pretty much the same'],
}

export const player = { time: '12:07', modes: ['Read', 'Listen'], active: 'Read' }

export const captions = { left: '@ninaskrbic', right: 'IOS Design' }
