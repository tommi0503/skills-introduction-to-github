import { cn } from '../../../ui'

/** Small "New" chip. */
export function Badge({ children, className }: { children: string; className?: string }) {
  return (
    <span className={cn('inline-flex h-[22px] w-[43px] items-center justify-center rounded-[36px] bg-[#f7f8f4] font-geist text-[12px] tracking-[0.12px] text-[#151515] uppercase', className)}>
      {children}
    </span>
  )
}
