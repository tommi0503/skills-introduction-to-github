import { cn } from '../../../ui'

export interface UnderlineTabsProps {
  items: string[]
  active: string
  /** left offset of each label (px) — tabs are laid out by the reference spacing. */
  gap: number
  className?: string
  itemClassName?: string
  activeClassName?: string
  inactiveClassName?: string
  /** extra underline width on each side */
  bleed?: number
}

/** Horizontal text tabs with a black underline under the active one and a hairline beneath. */
export function UnderlineTabs({ items, active, gap, className, itemClassName, activeClassName, inactiveClassName, bleed = 2 }: UnderlineTabsProps) {
  return (
    <div className={cn('flex items-stretch whitespace-nowrap border-b border-[#ebedef]', className)} style={{ gap }}>
      {items.map((t) => {
        const on = t === active
        return (
          <div key={t} className={cn('relative flex items-center', itemClassName, on ? activeClassName : inactiveClassName)}>
            {t}
            {on && <span className="absolute -bottom-px h-[2.5px] bg-black" style={{ left: -bleed, right: -bleed }} />}
          </div>
        )
      })}
    </div>
  )
}
