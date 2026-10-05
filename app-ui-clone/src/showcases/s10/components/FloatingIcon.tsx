import type { LucideIcon } from 'lucide-react'

/** Round coloured badge holding a filled icon (floating decorations on the onboarding). */
export function FloatingIcon({
  icon: Icon,
  size,
  color,
  iconSize,
  filled = true,
}: {
  icon: LucideIcon
  size: number
  color: string
  iconSize: number
  filled?: boolean
}) {
  return (
    <div className="flex items-center justify-center rounded-full" style={{ width: size, height: size, background: color }}>
      <Icon size={iconSize} fill={filled ? 'currentColor' : 'none'} strokeWidth={filled ? 1.6 : 2.2} />
    </div>
  )
}
