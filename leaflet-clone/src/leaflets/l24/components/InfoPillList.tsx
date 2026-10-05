import { cn } from '../../../ui'
import { FramedPill } from '../../shared-2425/components/FramedPill'

export interface PillInfo {
  label: string
  value: string
}

interface InfoPillListProps {
  items: PillInfo[]
  fill: string
  pillWidth: number
  pillHeight: number
  /** Distance between consecutive row centres. */
  pitch: number
  /** Gap between pill and value text. */
  gap: number
  labelClassName?: string
  valueClassName?: string
}

/** Vertical list of "pill label + value" rows (대상 / 일정 … , 운영대상 / 운영장소 …). */
export function InfoPillList({ items, fill, pillWidth, pillHeight, pitch, gap, labelClassName, valueClassName }: InfoPillListProps) {
  return (
    <div className="flex flex-col" style={{ gap: pitch - pillHeight }}>
      {items.map((it) => (
        <div key={it.label} className="flex items-center" style={{ gap, height: pillHeight }}>
          <FramedPill fill={fill} width={pillWidth} height={pillHeight} borderWidth={1.8} className={labelClassName}>
            {it.label}
          </FramedPill>
          <span className={cn('whitespace-nowrap', valueClassName)}>{it.value}</span>
        </div>
      ))}
    </div>
  )
}
