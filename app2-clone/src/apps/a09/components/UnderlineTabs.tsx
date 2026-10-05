import { cn } from '../../../ui'

export interface UnderlineTabsProps {
  items: string[]
  active: number
  /** Equal-width cells (package selector) vs. content-width (profile tabs). */
  equal?: boolean
  className?: string
  itemClassName?: string
  barClassName?: string
  /** How far the active bar extends past the label cell (px) and sits below it. */
  barOverhang?: number
  barDrop?: number
}

export function UnderlineTabs({ items, active, equal, className, itemClassName, barClassName, barOverhang = 0, barDrop = 0 }: UnderlineTabsProps) {
  return (
    <div className={cn('flex', className)}>
      {items.map((t, i) => (
        <div
          key={t}
          className={cn('relative flex items-center justify-center whitespace-nowrap', equal && 'flex-1', itemClassName)}
          style={{ color: i === active ? '#222325' : '#95979d', fontWeight: i === active ? 600 : 500 }}
        >
          {t}
          {i === active && (
            <span
              className={cn('absolute bg-[#111]', barClassName ?? 'h-[3px]')}
              style={{ left: -barOverhang, right: -barOverhang, bottom: -barDrop }}
            />
          )}
        </div>
      ))}
    </div>
  )
}
