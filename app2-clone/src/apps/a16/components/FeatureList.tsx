import { Check } from 'lucide-react'
import { cn } from '../../../ui'

export interface Feature {
  label: string
  highlight?: boolean
}

/** Check-marked feature bullets; highlighted items use the accent colour. */
export function FeatureList({ items, className }: { items: Feature[]; className?: string }) {
  return (
    <ul className={cn('flex flex-col gap-[16px]', className)}>
      {items.map((f) => (
        <li
          key={f.label}
          className={cn('flex items-center gap-[10px] text-[16.5px] leading-[22px]', f.highlight ? 'font-semibold text-[#5b5bd6]' : 'text-[#111]')}
        >
          <Check size={17} strokeWidth={2.2} />
          {f.label}
        </li>
      ))}
    </ul>
  )
}
