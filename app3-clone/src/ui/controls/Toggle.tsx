import type { ReactNode } from 'react'
import { cn } from '../core/cn'

export interface ToggleProps {
  on: boolean
  width?: number
  height?: number
  onColor?: string
  offColor?: string
  knobColor?: string
  /** Optional text shown inside the track (e.g. "ON"). */
  label?: ReactNode
  className?: string
}

export function Toggle({
  on,
  width = 51,
  height = 31,
  onColor = '#34c759',
  offColor = '#e5e5ea',
  knobColor = '#fff',
  label,
  className,
}: ToggleProps) {
  const pad = 2
  const knob = height - pad * 2
  return (
    <div
      className={cn('relative flex shrink-0 items-center rounded-full', className)}
      style={{ width, height, background: on ? onColor : offColor }}
    >
      {label && (
        <span className="absolute" style={{ left: on ? 10 : undefined, right: on ? undefined : 10 }}>
          {label}
        </span>
      )}
      <span
        className="absolute rounded-full shadow"
        style={{ width: knob, height: knob, top: pad, left: on ? width - knob - pad : pad, background: knobColor }}
      />
    </div>
  )
}
