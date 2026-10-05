import { cn } from '../../../ui'
import { theme } from '../theme'

export interface TopTabsProps {
  tabs: string[]
  activeIndex?: number
  guideLabel: string
  tone?: 'dark' | 'light'
  className?: string
}

/** "월정액 / 자유이용" segmented header with the lime "가이드" pill. */
export function TopTabs({ tabs, activeIndex = 0, guideLabel, tone = 'dark', className }: TopTabsProps) {
  const active = tone === 'dark' ? '#111' : '#fff'
  const inactive = tone === 'dark' ? '#5c5c5c' : 'rgba(255,255,255,0.85)'
  return (
    <div className={cn('relative flex h-[59px] items-start justify-between px-[25px] font-pretendard', className)}>
      <div className="flex gap-[24px] pt-[18px]">
        {tabs.map((tab, i) => (
          <div key={tab} className="relative">
            <span
              className={cn('text-[16.8px] tracking-[0px]', i === activeIndex ? 'font-bold' : 'font-medium')}
              style={{ color: i === activeIndex ? active : inactive }}
            >
              {tab}
            </span>
            {i === activeIndex && (
              <span className="absolute top-[39px] right-0 left-0 h-[4.5px]" style={{ background: theme.limeLine }} />
            )}
          </div>
        ))}
      </div>
      <div
        className="mt-[14.5px] flex h-[33px] w-[60px] items-center justify-center rounded-full text-[13px] font-bold text-black"
        style={{ background: theme.lime }}
      >
        {guideLabel}
      </div>
    </div>
  )
}
