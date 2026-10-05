import { ShoppingCart } from 'lucide-react'
import { theme } from '../theme'

/** Lime cart pill with item count. */
export function CartBadge({ count }: { count: number }) {
  return (
    <div
      className="flex h-[36px] w-[58px] items-center justify-center gap-[8px] rounded-[7px] font-poppins text-[15px] font-semibold"
      style={{ background: theme.lime, color: theme.ink }}
    >
      <ShoppingCart size={18} strokeWidth={2.2} />
      <span>{count}</span>
    </div>
  )
}
