import { ImagePlaceholder } from '../../../ui'
import type { Category } from '../data'
import { explorePalette as c } from '../theme'

/** Horizontal icon+label category strip with an underline on the active item. */
export function CategoryTabs({ items, active, centers }: { items: Category[]; active: string; centers: number[] }) {
  return (
    <div className="relative h-[69px] overflow-hidden" style={{ boxShadow: '0 4px 4px -2px rgba(0,0,0,0.06)' }}>
      {items.map((item, i) => {
        const on = item.key === active
        const Icon = item.icon
        return (
          <div
            key={item.key}
            className="absolute top-0 flex -translate-x-1/2 flex-col items-center"
            style={{ left: centers[i], color: on ? c.text : c.muted }}
          >
            <div className="flex h-[26px] w-[26px] items-center justify-center" style={{ marginTop: 4 }}>
              {Icon ? (
                <Icon size={23} strokeWidth={1.3} color={c.text} />
              ) : (
                <ImagePlaceholder className="rounded-[4px]" style={{ width: 22, height: 20 }} label={`${item.label} icon`} />
              )}
            </div>
            <span className={on ? 'mt-[6px] text-[11px] font-semibold' : 'mt-[6px] text-[11px] font-medium'} style={{ color: on ? c.text : c.muted }}>
              {item.label}
            </span>
            {on && <span className="mt-[11px] h-[2px] w-[34px] rounded-full" style={{ background: c.text }} />}
          </div>
        )
      })}
    </div>
  )
}
