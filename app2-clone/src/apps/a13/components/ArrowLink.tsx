import { ArrowRight } from 'lucide-react'
import { cn } from '../../../ui'

export interface ArrowLinkProps {
  label: string
  className?: string
  iconSize?: number
}

/** Purple "Learn more →" style text link. */
export function ArrowLink({ label, className, iconSize = 15 }: ArrowLinkProps) {
  return (
    <span className={cn('inline-flex items-center gap-[7px] text-[#6a4fc8]', className)}>
      {label}
      <ArrowRight size={iconSize} strokeWidth={1.8} />
    </span>
  )
}
