import { Bell, Flame, Zap } from 'lucide-react'
import { IconButton } from '../../../ui'
import { theme } from '../theme'

interface BrandHeaderProps {
  name: string
  badge: string
}

/** Logo + app name + membership badge on the left, notification bell on the right. */
export function BrandHeader({ name, badge }: BrandHeaderProps) {
  return (
    <div className="flex items-center justify-between">
      <div className="flex items-center gap-[10px]">
        <div className="flex h-[36px] w-[36px] items-center justify-center rounded-full bg-[#f4f4f6]">
          <Flame size={23} strokeWidth={0} fill={theme.brand} />
        </div>
        <div className="leading-none text-white">
          <div className="text-[17px] font-medium tracking-[-0.1px]">{name}</div>
          <div className="mt-[4px] flex items-center gap-[2px] text-[11px] font-medium text-white/75">
            <Zap size={11} strokeWidth={0} fill={theme.pro} />
            <span>{badge}</span>
          </div>
        </div>
      </div>
      <IconButton icon={Bell} size={37} iconSize={18} strokeWidth={1.8} className="bg-[#f4f4f6] text-[#111]" />
    </div>
  )
}
