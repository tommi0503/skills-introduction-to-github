import type { LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'

export interface MonoTabProps {
  icon: LucideIcon
  label: string
  color: string
  iconSize?: number
  gap?: number
  labelClassName?: string
  /** Optional underline marker under the label (active tab). */
  marker?: string
}

/** Icon over a tracked monospace caption — used by the tab bar and the edit toolbar. */
export function MonoTab({ icon: Icon, label, color, iconSize = 21, gap = 6, labelClassName, marker }: MonoTabProps) {
  return (
    <div className="relative flex flex-1 flex-col items-center" style={{ color, gap }}>
      <Icon size={iconSize} strokeWidth={1.8} />
      <span className={cn('font-plexmono text-[9.5px] leading-none font-medium tracking-[0.12em]', labelClassName)}>{label}</span>
      {marker && <span className="absolute -bottom-[9px] h-[2.5px] w-[14px] rounded-full" style={{ background: marker }} />}
    </div>
  )
}
