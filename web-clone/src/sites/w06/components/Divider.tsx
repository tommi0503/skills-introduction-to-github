import type { CSSProperties } from 'react'

/** 1px horizontal rule. */
export function Divider({ color, style }: { color: string; style?: CSSProperties }) {
  return <div style={{ height: 1, background: color, ...style }} />
}
