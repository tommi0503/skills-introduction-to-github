import { AudioLines, Diamond, Sun, Thermometer, Wind, type LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import type { Condition, ConditionIcon } from '../data'

const icons: Record<ConditionIcon, LucideIcon> = { sun: Sun, water: Thermometer, wind: Wind, swell: Diamond, wave: AudioLines }
const tints: Partial<Record<ConditionIcon, string>> = { sun: '#f5c84a', water: '#7fc4ff' }

export interface ConditionItemProps {
  condition: Condition
  /** colour the sun/water glyphs (weather strip) or keep them white (summary card) */
  tinted?: boolean
  iconSize?: number
  className?: string
}

export function ConditionItem({ condition, tinted, iconSize = 18, className }: ConditionItemProps) {
  const Icon = icons[condition.icon]
  const color = tinted ? tints[condition.icon] : undefined
  return (
    <div className={cn('flex items-center', className)}>
      <Icon size={iconSize} strokeWidth={2} style={{ color }} fill={condition.icon === 'swell' || (tinted && condition.icon === 'sun') ? 'currentColor' : 'none'} />
      <span className="ml-[8px]">{condition.value}</span>
      {condition.unit && <span className="ml-[3px] text-[10px] font-normal text-white/60">{condition.unit}</span>}
    </div>
  )
}
