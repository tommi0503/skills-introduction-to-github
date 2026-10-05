import { Cloud, QrCode, Search } from 'lucide-react'
import { TabBar, cn } from '../../../ui'
import type { CuTab, CuTabKey } from '../data'
import { cu } from '../theme'

function TabGlyph({ tab, active }: { tab: CuTab; active: boolean }) {
  const color = active ? '#444' : '#555'
  if (tab.key === 'stock') {
    return (
      <span className="relative inline-block h-[26px] w-[28px]">
        <Cloud size={26} strokeWidth={1.4} color={color} />
        <Search size={11} strokeWidth={2} color={color} className="absolute right-0 bottom-0 bg-white" />
      </span>
    )
  }
  const Icon = tab.icon!
  return (
    <span className="relative inline-flex">
      <Icon size={26} strokeWidth={1.4} color={color} fill={active ? color : 'none'} />
      {tab.key === 'home' && (
        <span
          className={cn('absolute inset-x-0 bottom-[5px] text-center text-[7px] leading-none font-extrabold', active ? 'text-white' : 'text-[#555]')}
        >
          CU
        </span>
      )}
    </span>
  )
}

export interface CuTabBarProps {
  tabs: CuTab[]
  active: CuTabKey
  /** Horizontal centre (pt) of each tab; defaults to equal-width cells. */
  centers?: number[]
  /** Bar height (pt), measured per screen. */
  height?: number
}

/** Bottom navigation with the raised gradient QR button in the middle. */
export function CuTabBar({ tabs, active, centers, height = 83 }: CuTabBarProps) {
  return (
    <div
      className="absolute inset-x-0 bottom-0 rounded-t-[22px] bg-white"
      style={{ height, boxShadow: '0 -2px 10px rgba(0,0,0,0.06)' }}
    >
      <TabBar
        items={tabs}
        activeKey={active}
        className="relative px-[2px] pt-[10px]"
        renderItem={(item, isActive) => {
          const index = tabs.findIndex((t) => t.key === item.key)
          const tab = tabs[index]
          const x = centers?.[index]
          return (
            <div
              className={cn('flex flex-col items-center', x === undefined ? 'relative flex-1' : 'absolute top-[10px] w-[80px]')}
              style={x === undefined ? undefined : { left: x - 40 }}
            >
              {tab.fab ? (
                <>
                <span className="h-[26px]" />
                <div
                  className="absolute flex h-[50px] w-[50px] items-center justify-center rounded-full text-white"
                  style={{ top: -25.5, background: cu.qr, boxShadow: '0 3px 8px rgba(110,100,240,0.35)' }}
                >
                  <QrCode size={25} strokeWidth={1.7} />
                </div>
                </>
              ) : (
                <TabGlyph tab={tab} active={isActive} />
              )}
              <span
                className={cn('mt-[1px] text-[10px] leading-[14px] whitespace-nowrap', isActive ? 'font-bold text-[#333]' : 'text-[#555]')}
              >
                {tab.label}
              </span>
            </div>
          )
        }}
      />
    </div>
  )
}
