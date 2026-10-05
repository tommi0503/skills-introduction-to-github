import type { QuickAction } from '../data'
import { theme } from '../theme'

/** Stacked shortcut rows separated by hairlines. */
export function QuickActionList({ items, rowHeight }: { items: QuickAction[]; rowHeight: number }) {
  return (
    <div>
      {items.map((a, i) => {
        const Icon = a.icon
        return (
          <div
            key={a.key}
            className="flex items-center gap-[12px] pb-[5.4px] font-poppins text-[13.5px] font-medium"
            style={{ height: rowHeight, color: theme.ink, borderTop: i ? `1px solid ${theme.hairline}` : undefined }}
          >
            <span className="flex w-[18px] justify-center">
              {Icon ? <Icon size={18} strokeWidth={2.6} fill={a.filled ? "currentColor" : "none"} /> : <span className="text-[17px] leading-none font-bold">{a.glyph}</span>}
            </span>
            {a.label}
          </div>
        )
      })}
    </div>
  )
}
