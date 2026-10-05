import type { CSSProperties } from 'react'
import { cn } from '../../../ui'

export interface FolderShapeProps {
  back: string
  front: string
  className?: string
  /** Open tray variant: a white sheet standing in a low front with a dipped top edge. */
  paper?: boolean
  style?: CSSProperties
}

/** iOS-style folder drawn with two layers (tabbed back + front panel). Scales to its box. */
export function FolderShape({ back, front, className, paper, style }: FolderShapeProps) {
  return (
    <svg viewBox="0 0 100 88" preserveAspectRatio="none" className={cn('block', className)} style={style}>
      {paper ? (
        <>
          <rect x="6.5" y="0.5" width="87" height="56" fill="#fff" stroke="#e4e4e4" strokeWidth="1" vectorEffect="non-scaling-stroke" />
          <path d="M0 33 Q0 29 4 29 H6 Q10 29 10 34 V40 Q10 46 16 46 H84 Q90 46 90 40 V34 Q90 29 94 29 H96 Q100 29 100 33 V80 Q100 88 92 88 H8 Q0 88 0 80 Z" fill={front} />
        </>
      ) : (
        <>
          <path d="M0 7 Q0 0 7 0 H32 Q36 0 39 3 L44 8 H93 Q100 8 100 15 V80 H0 Z" fill={back} />
          <rect x="0" y="16" width="100" height="72" rx="7" fill={front} />
        </>
      )}
    </svg>
  )
}
