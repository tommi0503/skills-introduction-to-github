import type { CSSProperties } from 'react'
import { theme } from '../theme'

export interface EtchProps {
  orientation?: 'horizontal' | 'vertical'
  /** Which side of the 2px pair is the dark line. */
  darkFirst?: boolean
  style?: CSSProperties
}

/** 2px engraved rule: one dark and one light hairline side by side. */
export function Etch({ orientation = 'horizontal', darkFirst = true, style }: EtchProps) {
  const [a, b] = darkFirst ? [theme.etchDark, theme.etchLight] : [theme.etchLight, theme.etchDark]
  const horizontal = orientation === 'horizontal'
  return (
    <div
      className="absolute"
      style={{
        ...(horizontal ? { height: 2 } : { width: 2 }),
        background: `linear-gradient(${horizontal ? 'to bottom' : 'to right'}, ${a} 50%, ${b} 50%)`,
        ...style,
      }}
    />
  )
}
