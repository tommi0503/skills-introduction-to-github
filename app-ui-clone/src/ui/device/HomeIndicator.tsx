import { cn } from '../core/cn'

export interface HomeIndicatorProps {
  tone?: 'dark' | 'light'
  width?: number
  bottom?: number
  className?: string
}

/** Bottom home bar (logical units). */
export function HomeIndicator({ tone = 'dark', width = 134, bottom = 8, className }: HomeIndicatorProps) {
  return (
    <div
      className={cn('absolute left-1/2 z-50 h-[5px] -translate-x-1/2 rounded-full', className)}
      style={{ width, bottom, background: tone === 'dark' ? '#111' : '#fff' }}
    />
  )
}
