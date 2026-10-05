import type { ReactNode } from 'react'
import { ChevronRight } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { fi } from '../theme'

/** White rounded summary tile with a title + chevron header. */
export function SummaryCard({ title, children, className }: { title: string; children?: ReactNode; className?: string }) {
  return (
    <div className={cn('overflow-hidden rounded-[12px] bg-white', className)}>
      <div className="flex items-center justify-between pl-[15px] pr-[10px] pt-[17px]">
        <span className="text-[15px] font-medium leading-none text-black">{title}</span>
        <ChevronRight size={15} strokeWidth={1.6} className="text-[#a0a0a0]" />
      </div>
      {children}
    </div>
  )
}

/** Growing green bars at the bottom-right of the activity card. */
export function MiniBars({ bars, className }: { bars: { h: number; c: string }[]; className?: string }) {
  return (
    <div className={cn('flex items-end gap-[2.5px]', className)}>
      {bars.map((b, i) => (
        <span key={i} className="w-[20px]" style={{ height: b.h, background: b.c }} />
      ))}
    </div>
  )
}

export function SectionHeader({ title, right, className }: { title: ReactNode; right?: ReactNode; className?: string }) {
  return (
    <div className={cn('flex items-center justify-between', className)}>
      <div className="text-[19px] font-semibold tracking-[-0.2px] text-black">{title}</div>
      {right}
    </div>
  )
}

export function Illustration({ className, label }: { className?: string; label: string }) {
  return <ImagePlaceholder className={className} label={label} />
}

export const greyText = { color: fi.grey }
