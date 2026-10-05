import type { LucideIcon } from 'lucide-react'

export interface BlobNavProps {
  items: { key: string; icon: LucideIcon }[]
  activeKey: string
  size?: number
  spacing?: number
}

/** Three linked circular tabs inside a black "metaball" outline. */
export function BlobNav({ items, activeKey, size = 43, spacing = 62.5 }: BlobNavProps) {
  const ring = 4
  const width = size + spacing * (items.length - 1)
  return (
    <div className="relative" style={{ width: width + ring * 2, height: size + ring * 2 }}>
      <span
        className="absolute rounded-full bg-black"
        style={{ left: ring + size / 2, right: ring + size / 2, top: ring + size / 2 - 9, height: 18 }}
      />
      {items.map(({ key, icon: Icon }, i) => {
        const active = key === activeKey
        return (
          <span
            key={key}
            className="absolute flex items-center justify-center rounded-full"
            style={{
              left: i * spacing,
              top: 0,
              width: size + ring * 2,
              height: size + ring * 2,
              background: active ? '#fff' : '#3d3d3d',
              border: `${ring}px solid #000`,
              color: active ? '#222' : '#fff',
            }}
          >
            <Icon size={19} strokeWidth={1.6} />
          </span>
        )
      })}
    </div>
  )
}
