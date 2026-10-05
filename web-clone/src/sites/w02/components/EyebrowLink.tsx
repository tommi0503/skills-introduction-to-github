import { ChevronRight } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** Blue "Section name >" link that heads most sections. */
export function EyebrowLink({ label, className }: { label: string; className?: string }) {
  return (
    <span className={cn('inline-flex items-center text-[16px] leading-6 font-medium', className)} style={{ color: theme.link }}>
      {label}
      <ChevronRight className="ml-[2px] size-4" strokeWidth={2} />
    </span>
  )
}
