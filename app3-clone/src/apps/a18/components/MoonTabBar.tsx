import { cn } from '../../../ui'
import type { Tab } from '../data'
import { theme } from '../theme'

export function MoonTabBar({ tabs, active }: { tabs: Tab[]; active: string }) {
  return (
    <div
      className="absolute top-[766px] left-[22px] flex h-[60px] w-[346px] items-center rounded-full px-[3px]"
      style={{ background: theme.tabBar + 'ee', boxShadow: '0 0 0 1px rgba(255,255,255,0.06)' }}
    >
      {tabs.map((t) => {
        const on = t.key === active
        const Icon = t.icon
        return (
          <div
            key={t.key}
            className={cn('flex h-[54px] flex-1 flex-col items-center justify-center gap-[4px] rounded-full', on && 'bg-[#46464b]')}
          >
            <Icon
              size={20}
              strokeWidth={1.6}
              fill={on ? theme.accent : '#6a6a70'}
              color={on ? theme.accent : '#6a6a70'}
            />
            <span className={cn('text-[9.5px] leading-none font-medium', on ? 'text-white' : 'text-[#6f6f74]')}>{t.label}</span>
          </div>
        )
      })}
    </div>
  )
}
