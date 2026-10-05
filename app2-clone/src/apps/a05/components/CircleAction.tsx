import type { LucideIcon } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'

export interface CircleActionProps {
  label: string
  icon?: LucideIcon
  /** placeholder colour when the circle is a photo / app icon */
  tone?: string
}

/** Big round target with a bold caption under it (share sheet). */
export function CircleAction({ label, icon: Icon, tone }: CircleActionProps) {
  return (
    <div className="flex w-[64px] flex-col items-center gap-[10px]">
      {Icon ? (
        <span className="flex h-[55px] w-[55px] items-center justify-center rounded-full bg-[#e4e7ea]">
          <Icon size={21} strokeWidth={1.7} color="#111" />
        </span>
      ) : (
        <ImagePlaceholder label={label} tone={tone} className="h-[55px] w-[55px] rounded-full" />
      )}
      <span className="whitespace-nowrap text-[12.5px] font-semibold leading-none text-[#222]">{label}</span>
    </div>
  )
}
