import { BellDot, type LucideIcon } from 'lucide-react'
import { TabBar as BaseTabBar, cn, type TabItem } from '../../../ui'
import { tabs, type TabEntry } from '../data'
import { theme } from '../theme'

const resolveIcon = (icon: TabEntry['icon']): LucideIcon => (icon === 'explore' ? BellDot : icon)

/** Floating pill tab bar + detached profile circle. */
export function FoodTabBar({ activeKey, top = 750 }: { activeKey: string; top?: number }) {
  const main = tabs.filter((t) => t.label)
  const extra = tabs.filter((t) => !t.label)
  const items: TabItem[] = main.map((t) => ({ key: t.key, label: t.label, icon: resolveIcon(t.icon) }))
  return (
    <div className="absolute right-[18px] left-[28px] flex items-center justify-between" style={{ top }}>
      <BaseTabBar
        items={items}
        activeKey={activeKey}
        className="h-[55px] w-[268px] rounded-full border border-[#f0f0f2] bg-[#fbfbfc] px-[2px]"
        renderItem={(item, active) => {
          const Icon = item.icon!
          return (
            <span
              className={cn('flex h-[50px] w-[88px] flex-col items-center justify-center gap-[2px] rounded-full', active && 'bg-[#eef0f6]')}
              style={{ color: active ? theme.blue : '#555' }}
            >
              <Icon size={19} strokeWidth={1.8} />
              <span className={cn('text-[14px] leading-[17px]', active && 'font-semibold')}>{item.label}</span>
            </span>
          )
        }}
      />
      {extra.map((t) => {
        const Icon = resolveIcon(t.icon)
        return (
          <span key={t.key} className="flex h-[55px] w-[55px] items-center justify-center rounded-full border border-[#f0f0f2] bg-[#fbfbfc] text-[#444]">
            <Icon size={22} strokeWidth={1.6} />
          </span>
        )
      })}
    </div>
  )
}
