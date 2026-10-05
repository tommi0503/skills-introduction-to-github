/** Design tokens shared by the library programme leaflets 24 and 25. */
export const library = {
  paper: '#f6f6f1',
  cream: '#f2ecdc',
  navy: '#50547c',
  ink: '#3e4166',
  deep: '#383c60',
  title: '#203a60',
  coral: '#e2625e',
  yellow: '#f1e097',
  lavender: '#dde2f5',
  pale: '#e5eaf6',
  green: '#bcdcb8',
  rule: '#d9d7cf',
  white: '#ffffff',
} as const

/** Shared sheet geometry (sheet px, measured on the flat references). */
export const ground = {
  /** y of the outlined top edge of the green ground band. */
  top: 942,
  line: 2.5,
} as const
