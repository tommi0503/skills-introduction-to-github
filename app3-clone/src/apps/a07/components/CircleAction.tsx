import type { LucideIcon } from 'lucide-react'

export interface CircleActionProps {
  icon: LucideIcon
  label: string
  size?: number
  background?: string
}

export function CircleAction({ icon: Icon, label, size = 48, background = 'rgba(255,255,255,0.18)' }: CircleActionProps) {
  return (
    <div className="flex w-[90px] flex-col items-center text-white">
      <span className="flex items-center justify-center rounded-full" style={{ width: size, height: size, background }}>
        <Icon size={20} strokeWidth={2.2} />
      </span>
      <span className="mt-[9px] text-[13px] font-medium">{label}</span>
    </div>
  )
}
