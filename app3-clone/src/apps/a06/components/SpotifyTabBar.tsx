import type { ReactNode } from 'react'
import { ImagePlaceholder, TabBar, type TabItem } from '../../../ui'
import { nav } from '../data'
import { sp } from '../theme'

export interface SpotifyTabBarProps {
  tabs: string[]
  active: string
  /** Extra content under the tab row (e.g. "Offline mode"). */
  footer?: ReactNode
  /** Height of the fading backdrop. */
  height?: number
  /** Distance of the tab row's bottom edge from the screen bottom. */
  rowBottom?: number
}

/** Bottom navigation over a black fade, shared by all Spotify screens. */
export function SpotifyTabBar({ tabs, active, footer, height = 112, rowBottom = 30 }: SpotifyTabBarProps) {
  const items: TabItem[] = tabs.map((k) => ({
    key: k,
    label: nav[k].label,
    icon: nav[k].icon,
    node: nav[k].brand ? <ImagePlaceholder tone="#ffffff" className="h-[25px] w-[25px] rounded-full" label="Spotify logo" /> : undefined,
  }))
  return (
    <div
      className="absolute inset-x-0 bottom-0 z-20"
      style={{ height, background: 'linear-gradient(to bottom, rgba(0,0,0,0) 0%, rgba(0,0,0,0.82) 42%, #000 100%)' }}
    >
      <div className="absolute inset-x-0" style={{ bottom: rowBottom }}>
      <TabBar
        items={items}
        activeKey={active}
        renderItem={(item, on) => {
          const Icon = item.icon
          return (
            <div className="flex flex-1 flex-col items-center" style={{ color: on ? sp.white : sp.dim }}>
              <div className="flex h-[26px] items-center">
                {item.node ?? (Icon && <Icon size={24} strokeWidth={on ? 2.4 : 1.6} fill={on && item.key === 'home' ? 'currentColor' : 'none'} />)}
              </div>
              <span className="mt-[4px] text-[10.5px]" style={{ fontWeight: on ? 700 : 400 }}>
                {item.label}
              </span>
            </div>
          )
        }}
      />
      </div>
      {footer}
    </div>
  )
}
