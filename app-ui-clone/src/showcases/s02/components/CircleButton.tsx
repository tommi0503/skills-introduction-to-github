import type { LucideIcon } from 'lucide-react'
import { IconButton } from '../../../ui'

interface CircleButtonProps {
  icon: LucideIcon
  iconSize?: number
}

/** 46pt white round header button with a hairline shadow. */
export function CircleButton({ icon, iconSize = 20 }: CircleButtonProps) {
  return (
    <IconButton
      icon={icon}
      size={46}
      iconSize={iconSize}
      strokeWidth={1.6}
      className="bg-white text-[#5a5a5a] shadow-[0_1px_4px_rgba(0,0,0,0.06),0_0_0_1px_rgba(0,0,0,0.03)]"
    />
  )
}
