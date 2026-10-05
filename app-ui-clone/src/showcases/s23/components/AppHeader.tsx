import { cn } from '../../../ui'
import { guideLabel, topTabs } from '../data'
import { LaundryStatusBar } from './LaundryStatusBar'
import { TopTabs } from './TopTabs'

export interface AppHeaderProps {
  time: string
  tone?: 'dark' | 'light'
  /** Solid white background (scrolled screens) or transparent (hero). */
  solid?: boolean
  className?: string
}

/** Status bar + tabs, pinned to the top of every Laundrygo screen. */
export function AppHeader({ time, tone = 'dark', solid = true, className }: AppHeaderProps) {
  return (
    <div className={cn('absolute inset-x-0 top-0 z-30', solid && 'bg-white', className)}>
      <LaundryStatusBar time={time} tone={tone} />
      <TopTabs tabs={topTabs} guideLabel={guideLabel} tone={tone} />
    </div>
  )
}
