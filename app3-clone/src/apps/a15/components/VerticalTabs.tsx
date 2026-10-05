import { ImagePlaceholder, cn } from '../../../ui'
import type { Vertical } from '../data'
import { palette as c } from '../theme'

export interface VerticalTabsProps {
  items: Vertical[]
  active: string
  /** x centre of each item. */
  centers: number[]
  iconSize: number
  showNew: boolean
  labelGap: number
  underlineWidth: number
  className?: string
}

/** Homes / Experiences / Services switcher with 3D-icon placeholders. */
export function VerticalTabs({ items, active, centers, iconSize, showNew, labelGap, underlineWidth, className }: VerticalTabsProps) {
  return (
    <div className={cn('relative', className)}>
      {items.map((v, i) => {
        const on = v.key === active
        return (
          <div key={v.key} className="absolute top-0 flex -translate-x-1/2 flex-col items-center" style={{ left: centers[i] }}>
            <div className="relative">
              <ImagePlaceholder className="rounded-[10px]" style={{ width: iconSize, height: iconSize }} label={`${v.label} icon`} />
              {showNew && v.isNew && (
                <span
                  className="absolute top-[3px] left-[38px] rounded-full px-[6px] py-[1.5px] text-[8.5px] leading-[11px] font-bold text-white"
                  style={{ background: c.newBadge, boxShadow: '0 0 0 1.5px #fff' }}
                >
                  NEW
                </span>
              )}
            </div>
            <span
              className={on ? 'text-[11.5px] font-semibold' : 'text-[11.5px] font-medium'}
              style={{ marginTop: labelGap, color: on ? c.text : c.muted }}
            >
              {v.label}
            </span>
            <span
              className="mt-[5px] h-[3px] rounded-full"
              style={{ width: underlineWidth, background: on ? c.text : 'transparent' }}
            />
          </div>
        )
      })}
    </div>
  )
}
