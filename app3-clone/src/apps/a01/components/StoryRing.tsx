import type { ReactNode } from 'react'
import { ImagePlaceholder } from '../../../ui'
import { ig } from '../theme'

export interface StoryRingProps {
  size: number
  /** Ring thickness. */
  ring?: number
  /** Gap between ring and picture. */
  gap?: number
  gapColor?: string
  tone?: string
  children?: ReactNode
}

/** Gradient story ring around a circular picture placeholder. */
export function StoryRing({ size, ring = 3, gap = 3, gapColor = '#fff', tone, children }: StoryRingProps) {
  return (
    <div className="relative shrink-0 rounded-full" style={{ width: size, height: size, background: ig.ring, padding: ring }}>
      <div className="h-full w-full rounded-full" style={{ background: gapColor, padding: gap }}>
        <ImagePlaceholder tone={tone} className="h-full w-full rounded-full" label="story" />
      </div>
      {children}
    </div>
  )
}
