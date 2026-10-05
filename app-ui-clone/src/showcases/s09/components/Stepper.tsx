import { Minus, Plus } from 'lucide-react'
import { theme } from '../theme'

/** Quantity − n + control. */
export function Stepper({ value }: { value: number }) {
  return (
    <div className="flex h-full w-full items-center justify-between rounded-[10px] px-[18px] font-poppins text-[15px] font-semibold" style={{ background: theme.stepper, color: theme.ink }}>
      <Minus size={16} strokeWidth={2} />
      <span>{value}</span>
      <Plus size={16} strokeWidth={2} />
    </div>
  )
}
