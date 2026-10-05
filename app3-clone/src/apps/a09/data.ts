export interface PadKey {
  digit: string
  letters?: string
}

/** iOS number-pad rows (null = empty slot, 'delete' = backspace key). */
export const padRows: Array<Array<PadKey | null | 'delete'>> = [
  [{ digit: '1', letters: '' }, { digit: '2', letters: 'ABC' }, { digit: '3', letters: 'DEF' }],
  [{ digit: '4', letters: 'GHI' }, { digit: '5', letters: 'JKL' }, { digit: '6', letters: 'MNO' }],
  [{ digit: '7', letters: 'PQRS' }, { digit: '8', letters: 'TUV' }, { digit: '9', letters: 'WXYZ' }],
  [null, { digit: '0' }, 'delete'],
]

export const smsScreen = {
  title: 'We just sent you an SMS',
  subtitle: 'Enter the security code we sent to',
  masked: '*******',
  help: 'Help',
  link: "Didn't receive a code?",
  action: 'Done',
  codeLength: 6,
}

export const digitScreen = {
  title: '6-digit code',
  subtitle: 'Code sent to +65 9036 6027 unless you already have an account',
  /** Number of boxes before the separator dash, and after. */
  groups: [3, 3],
  resend: 'Resend code in 00:14',
  link: 'Already have an account? Log in',
  suggestionLabel: 'From Messages',
  suggestionCode: '276-011',
}
