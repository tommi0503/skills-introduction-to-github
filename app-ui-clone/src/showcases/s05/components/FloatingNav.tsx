import { TabBar, cn } from '../../../ui'
import type { NavEntry } from '../data'
import { theme } from '../theme'

export interface FloatingNavProps {
  items: NavEntry[]
  activeKey: string
  className?: string
}

const ACTIVE = '#2fc163'

/** Active glyph: the icon's silhouette filled green with a white detail on top. */
function ActiveGlyph({ item }: { item: NavEntry }) {
  const Icon = item.icon
  const Detail = item.activeDetail
  return (
    <span className="relative flex h-[22px] w-[22px] items-center justify-center">
      <Icon size={22} strokeWidth={1.8} color={ACTIVE} fill={ACTIVE} className="absolute inset-0" />
      {Detail ? (
        <Detail size={13} strokeWidth={2.2} color="#fff" className="relative" />
      ) : (
        <span className="relative h-[7px] w-[7px] rounded-full bg-white" />
      )}
    </span>
  )
}

/** Grey capsule holding four round icon buttons; the active one is tinted green. */
export function FloatingNav({ items, activeKey, className }: FloatingNavProps) {
  return (
    <div className={cn('rounded-full', className)} style={{ background: theme.navPill, boxShadow: '0 4px 14px rgba(0,0,0,0.06)' }}>
      <TabBar
        className="h-[76px] w-[292px] justify-between px-[6px]"
        items={items}
        activeKey={activeKey}
        renderItem={(item, active) => {
          const entry = items.find((i) => i.key === item.key)!
          const Icon = entry.icon
          return (
            <span
              className="flex h-[64px] w-[64px] items-center justify-center rounded-full"
              style={{
                background: active ? '#d9ece0' : '#fbfbfb',
                boxShadow: active ? 'none' : '0 2px 6px rgba(0,0,0,0.05)',
              }}
            >
              {active ? <ActiveGlyph item={entry} /> : <Icon size={21} strokeWidth={1.6} color="#2b2b2b" />}
            </span>
          )
        }}
      />
    </div>
  )
}
