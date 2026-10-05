import { Key } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { AuthOption } from '../data'

/** Provider sign-in button; brand marks are placeholders, SSO uses a lucide key. */
export function AuthButton({ option, className }: { option: AuthOption; className?: string }) {
  const mark =
    option.key === 'sso' ? (
      <Key size={18} strokeWidth={1.6} className="-scale-x-100" />
    ) : (
      <ImagePlaceholder
        label={`${option.key} logo`}
        tone={option.dark ? '#d4d4d4' : undefined}
        className={cn(option.key === 'microsoft' ? 'h-[20px] w-[20px]' : 'h-[22px] w-[20px]', option.key !== 'microsoft' && 'rounded-full')}
      />
    )
  return (
    <div
      className={cn(
        'flex h-[40px] items-center justify-center gap-[9px] rounded-[8px] text-[15px] font-medium',
        option.dark ? 'bg-black text-white' : 'border border-[#dedede] bg-white text-[#1a1a1a]',
        className,
      )}
    >
      {mark}
      {option.label}
    </div>
  )
}
