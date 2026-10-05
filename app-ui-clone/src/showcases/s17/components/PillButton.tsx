import { cn } from '../../../ui'

export type PillVariant = 'outline' | 'solid'

/** Large rounded CTA, outlined or white-filled. */
export function PillButton({ label, variant, className }: { label: string; variant: PillVariant; className?: string }) {
  return (
    <span
      className={cn(
        'flex items-center justify-center rounded-full text-[#111]',
        variant === 'outline' ? 'border border-[#d6d6d6]' : 'bg-white',
        className,
      )}
    >
      {label}
    </span>
  )
}
