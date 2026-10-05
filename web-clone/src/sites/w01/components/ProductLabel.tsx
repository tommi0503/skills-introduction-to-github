import { ChevronRight } from 'lucide-react'
import type { Product } from '../data'
import { theme } from '../theme'

/** "Name. Tag >" label + one-line description under a product media block. */
export function ProductLabel({ name, tag, body }: Product) {
  return (
    <div>
      <div className="flex h-6 items-center text-[16px] leading-4 font-medium tracking-[0.16px]">
        <span style={{ color: theme.ink }}>{name}</span>
        <span className="ml-2" style={{ color: theme.muted }}>{tag}</span>
        <ChevronRight className="ml-2 size-[18px]" strokeWidth={2} style={{ color: theme.muted }} />
      </div>
      <p className="mt-4 text-[16px] leading-[21.6px]" style={{ color: theme.muted }}>{body}</p>
    </div>
  )
}
