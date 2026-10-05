import { Check } from 'lucide-react'

export interface RadioMarkProps {
  checked: boolean
  size: number
  color: string
  /** Ring colour when unchecked. */
  idle: string
  /** Optional white halo around the checked state. */
  halo?: boolean
}

/** Circular selection mark: filled with a check when selected, an empty ring otherwise. */
export function RadioMark({ checked, size, color, idle, halo }: RadioMarkProps) {
  if (!checked)
    return <span className="block shrink-0 rounded-full bg-white" style={{ width: size, height: size, border: `1.5px solid ${idle}` }} />
  return (
    <span
      className="flex shrink-0 items-center justify-center rounded-full"
      style={{ width: size, height: size, background: color, boxShadow: halo ? `0 0 0 3px #fff, 0 0 0 4px ${idle}` : undefined }}
    >
      <Check size={size * 0.58} strokeWidth={3.4} color="#fff" />
    </span>
  )
}
