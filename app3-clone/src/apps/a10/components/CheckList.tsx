import { Check } from 'lucide-react'
import { theme } from '../theme'

export function CheckList({ items, className }: { items: string[]; className?: string }) {
  return (
    <ul className={className}>
      {items.map((t) => (
        <li key={t} className="mb-[17px] flex items-start gap-[11px]">
          <span
            className="mt-[2px] flex h-[22px] w-[22px] shrink-0 items-center justify-center rounded-full"
            style={{ background: theme.checkFill }}
          >
            <Check size={14} strokeWidth={3} className="text-white" />
          </span>
          <span className="text-[15.5px] leading-[25px]" style={{ color: theme.body }}>
            {t}
          </span>
        </li>
      ))}
    </ul>
  )
}
