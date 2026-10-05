import { Minus, Plus, Trash2 } from 'lucide-react'
import { theme } from '../theme'

/** Pill with decrement (trash when qty = 1), value and increment. */
export function QuantityStepper({ quantity }: { quantity: number }) {
  const Dec = quantity > 1 ? Minus : Trash2
  return (
    <div
      className="flex h-[32px] w-[91px] items-center justify-between rounded-[7px] px-[10px] text-[#111]"
      style={{ background: theme.field }}
    >
      <Dec size={quantity > 1 ? 15 : 14} strokeWidth={1.9} />
      <span className="text-[14px] font-medium">{quantity}</span>
      <Plus size={15} strokeWidth={1.9} />
    </div>
  )
}
