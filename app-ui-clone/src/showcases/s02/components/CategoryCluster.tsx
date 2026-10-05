import type { Category } from '../data'

interface CategoryClusterProps {
  items: Category[]
  /** Optional overlay glyph for an item (e.g. the magnifier on the globe). */
  badgeFor?: (key: string) => React.ReactNode
}

/** Scattered pastel category bubbles (positions come from data). */
export function CategoryCluster({ items, badgeFor }: CategoryClusterProps) {
  return (
    <>
      {items.map(({ key, icon: Icon, x, y, size, bg, fg }) => (
        <div
          key={key}
          className="absolute flex items-center justify-center rounded-full"
          style={{ left: x - size / 2, top: y - size / 2, width: size, height: size, background: bg, color: fg }}
        >
          <div className="relative">
            <Icon size={size * 0.45} strokeWidth={1.9} />
            {badgeFor?.(key)}
          </div>
        </div>
      ))}
    </>
  )
}
