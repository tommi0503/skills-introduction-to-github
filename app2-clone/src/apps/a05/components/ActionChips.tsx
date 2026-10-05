import { ImagePlaceholder, cn } from '../../../ui'
import type { Action } from '../data'
import { Floating } from './Floating'

/** Floating row of labelled actions (share / directions / site / ig). */
export function ActionChips({ items, className }: { items: Action[]; className?: string }) {
  return (
    <div className={cn('flex gap-[11px]', className)}>
      {items.map((a) => (
        <Floating key={a.key} className="h-[35px] gap-[6px] px-[13px] text-[13.5px] text-[#555]" style={{ boxShadow: '0 2px 8px rgba(0,0,0,.13)' }}>
          {a.icon ? <a.icon size={16} strokeWidth={1.7} color="#333" /> : <ImagePlaceholder label="instagram" className="h-[14px] w-[14px] rounded-[4px]" />}
          {a.label}
        </Floating>
      ))}
    </div>
  )
}
