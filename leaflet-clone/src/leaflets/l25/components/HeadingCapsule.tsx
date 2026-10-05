import type { CSSProperties } from 'react'
import { library } from '../../shared-2425/theme'

interface HeadingCapsuleProps {
  title: string
  style?: CSSProperties
}

/** Lavender, navy-outlined full capsule carrying a section title. */
export function HeadingCapsule({ title, style }: HeadingCapsuleProps) {
  return (
    <div
      className="absolute box-border flex items-center justify-center rounded-full font-dohyeon text-[25px] leading-none [-webkit-text-stroke:0.6px_currentColor]"
      style={{ background: library.lavender, border: `2.5px solid ${library.ink}`, color: library.title, ...style }}
    >
      {title}
    </div>
  )
}
