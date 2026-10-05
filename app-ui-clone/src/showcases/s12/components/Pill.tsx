import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export type PillTone = 'glass' | 'grey' | 'outline'

const tones: Record<PillTone, string> = {
  glass: 'bg-white/20 text-white/80',
  grey: 'bg-[#efefef] text-[#9a9a9a]',
  outline: 'border border-white/90 text-white/90',
}

/** Small uppercase label capsule used above headings and on cards. */
export function Pill({ tone, width, height = 25, children, className }: { tone: PillTone; width: number; height?: number; children: ReactNode; className?: string }) {
  return (
    <span
      className={cn('flex items-center justify-center rounded-full text-[11.5px] tracking-[-0.01em] uppercase', tones[tone], className)}
      style={{ width, height }}
    >
      {children}
    </span>
  )
}
