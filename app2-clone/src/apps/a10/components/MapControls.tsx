import { Cloud, Map, Mic } from 'lucide-react'
import { cn } from '../../../ui'

/** Vertical map-style / weather pill and the 3D-view button on the right of the map. */
export function MapControls({ variant = 'dark', className }: { variant?: 'dark' | 'light'; className?: string }) {
  const bg = variant === 'dark' ? 'bg-[#2c2c2e]/90' : 'bg-[#5f5a4c]/80'
  return (
    <div className={cn('absolute right-[18px] flex flex-col items-center gap-[8px] text-white', className)}>
      <div className={cn('flex h-[88px] w-[42px] flex-col items-center justify-around rounded-full py-[6px]', bg)}>
        <Map size={21} strokeWidth={2.4} />
        <Cloud size={19} strokeWidth={1.8} />
      </div>
      <div className={cn('flex h-[42px] w-[42px] items-center justify-center rounded-full', bg)}>
        <Mic size={19} strokeWidth={2.2} />
      </div>
    </div>
  )
}
