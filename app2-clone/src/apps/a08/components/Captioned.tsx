import { cn } from '../../../ui'

export interface CaptionedButtonProps {
  label: string
  caption: string
  className?: string
  buttonClassName?: string
}

/** Full-width capsule button with a small caption beneath. */
export function CaptionedButton({ label, caption, className, buttonClassName }: CaptionedButtonProps) {
  return (
    <div className={cn('flex flex-col items-center', className)}>
      <button type="button" className={cn('h-[55px] w-[334px] rounded-full text-[16px] font-[550]', buttonClassName)}>
        {label}
      </button>
      <span className="mt-[9px] text-[12.5px] leading-[16px] text-[#6b7079]">{caption}</span>
    </div>
  )
}
