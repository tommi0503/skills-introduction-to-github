import { TabBar, cn } from '../../../ui'
import type { NavEntry } from '../data'
import { theme } from '../theme'

export interface FloatingNavProps {
  items: NavEntry[]
  activeKey: string
  className?: string
}

const ACTIVE = '#2fc163'
const INK = '#2b2b2b'

/** Icon with an optional centred detail; active = filled green silhouette with a white detail. */
function NavGlyph({ entry, active }: { entry: NavEntry; active: boolean }) {
  const { icon: Icon, detail: Detail, detailSize = 10 } = entry
  return (
    <span className="relative flex h-[22px] w-[22px] items-center justify-center">
      <Icon
        size={22}
        strokeWidth={active ? 2 : 1.6}
        color={active ? ACTIVE : INK}
        fill={active ? ACTIVE : 'none'}
        className="absolute inset-0"
      />
      {Detail && (
        <Detail
          size={detailSize}
          strokeWidth={active ? 2.6 : 2.2}
          color={active ? '#fff' : INK}
          fill={active && detailSize < 10 ? '#fff' : 'none'}
          className="relative"
        />
      )}
    </span>
  )
}

/** Grey capsule holding four round icon buttons; the active one is tinted green. */
export function FloatingNav({ items, activeKey, className }: FloatingNavProps) {
  return (
    <div className={cn('rounded-full', className)} style={{ background: theme.navPill, boxShadow: '0 4px 14px rgba(0,0,0,0.06)' }}>
      <TabBar
        className="h-[76px] w-[292px] justify-between px-[4px]"
        items={items}
        activeKey={activeKey}
        renderItem={(item, active) => {
          const entry = items.find((i) => i.key === item.key)!
          return (
            <span
              className="flex h-[68px] w-[68px] items-center justify-center rounded-full"
              style={{
                background: active ? '#d9ece0' : '#fbfbfb',
                boxShadow: active ? 'none' : '0 2px 6px rgba(0,0,0,0.05)',
              }}
            >
              <NavGlyph entry={entry} active={active} />
            </span>
          )
        }}
      />
    </div>
  )
}
