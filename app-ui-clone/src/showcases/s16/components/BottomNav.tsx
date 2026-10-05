import type { LucideIcon } from 'lucide-react'
import type { ReactNode } from 'react'
import { TabBar, type TabItem } from '../../../ui'
import { theme } from '../theme'
import { CompassGlyph } from './CompassGlyph'

export interface NavEntry {
  key: string
  label?: string
  icon?: LucideIcon
  /** Custom glyph renderer receiving the active state. */
  glyph?: (active: boolean) => ReactNode
  /** The raised centre action. */
  center?: boolean
}

export interface BottomNavProps {
  items: NavEntry[]
  activeKey: string
  top?: number
}

/** Floating dark pill navigation with a raised white centre button. */
export function BottomNav({ items, activeKey, top = 745 }: BottomNavProps) {
  const tabs: TabItem[] = items.map((i) => ({ key: i.key, label: i.label, icon: i.icon }))
  const byKey = new Map(items.map((i) => [i.key, i]))
  return (
    <div
      className="absolute flex items-center rounded-full px-[18px]"
      style={{ left: 27, width: 339, top, height: 72, background: theme.dark }}
    >
      <TabBar
        items={tabs}
        activeKey={activeKey}
        className="h-full w-full justify-between"
        renderItem={(item, active) => {
          const entry = byKey.get(item.key)!
          if (entry.center) return <CenterAction key={item.key} />
          const Icon = item.icon
          return (
            <div className="flex w-[52px] flex-col items-center gap-[4px] text-white">
              <span className="flex h-[24px] items-center justify-center">
                {entry.glyph ? entry.glyph(active) : Icon && <Icon size={21} strokeWidth={1.7} />}
              </span>
              <span className="text-[12px] leading-none font-light tracking-[-0.2px]">{item.label}</span>
            </div>
          )
        }}
      />
    </div>
  )
}

function CenterAction() {
  return (
    <div
      className="flex items-center justify-center rounded-full bg-white"
      style={{ width: 49, height: 49, boxShadow: '0 0 0 3px #f7a334, 0 0 7px 4px rgba(250,170,60,0.5)', color: theme.ink }}
    >
      <CompassGlyph size={21} />
    </div>
  )
}
