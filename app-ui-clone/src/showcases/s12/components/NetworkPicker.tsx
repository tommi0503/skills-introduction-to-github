import { cn } from '../../../ui'
import type { Network } from '../data'

/** Square social-network toggles; the selected one is solid black. */
export function NetworkPicker({ items, active }: { items: Network[]; active: string }) {
  return (
    <div className="flex gap-[6.7px]">
      {items.map(({ key, icon: Icon }) => (
        <span
          key={key}
          className={cn(
            'flex size-[49px] items-center justify-center rounded-[12px]',
            key === active ? 'bg-[#111] text-white' : 'bg-white text-[#555]',
          )}
        >
          <Icon size={20} strokeWidth={2.2} />
        </span>
      ))}
    </div>
  )
}
