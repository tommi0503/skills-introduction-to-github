import type { ReactNode } from 'react'
import { t22 } from '../theme'

export interface UnderlineFieldProps {
  value?: string
  placeholder?: string
  /** Trailing adornments (chevron, clear button, unit...). */
  trailing?: ReactNode
  height?: number
  fontSize?: number
  lineWidth?: number
  /** Pushes the text towards the underline (logical px). */
  offsetY?: number
}

/** Single-line form value sitting on a thin underline. */
export function UnderlineField({ value, placeholder, trailing, height = 38, fontSize = 18, lineWidth = 2, offsetY = 0 }: UnderlineFieldProps) {
  return (
    <div className="flex items-center" style={{ height, paddingTop: offsetY * 2, borderBottom: `${lineWidth}px solid ${t22.line}` }}>
      <span
        className="flex-1"
        style={{ fontSize, color: value ? t22.text : t22.placeholder, letterSpacing: -0.4 }}
      >
        {value ?? placeholder}
      </span>
      {trailing}
    </div>
  )
}
