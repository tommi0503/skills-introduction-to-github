import { ImagePlaceholder } from '../../../ui'
import type { Category } from '../data'
import { theme } from '../theme'

/** Horizontally scrolling round category shortcuts (clipped at the right edge). */
export function CategoryRow({ items, top }: { items: Category[]; top: number }) {
  return (
    <div className="absolute flex" style={{ left: 31, top, gap: 26.5 }}>
      {items.map((c) => (
        <div key={c.key} className="flex w-[52px] flex-col items-center">
          <div
            className="flex h-[52px] w-[52px] items-center justify-center rounded-full"
            style={{ background: theme.circle }}
          >
            <ImagePlaceholder className="h-[30px] w-[30px] rounded-[6px]" label={c.label} />
          </div>
          <span className="mt-[6px] text-[11.5px] whitespace-nowrap text-[#2f2f35]">{c.label}</span>
        </div>
      ))}
    </div>
  )
}
