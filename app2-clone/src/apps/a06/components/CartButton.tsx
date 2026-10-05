import { ShoppingCart } from 'lucide-react'
import { theme } from '../theme'

export function CartButton({ count }: { count?: string }) {
  return (
    <span className="relative inline-flex">
      <ShoppingCart size={24} strokeWidth={1.8} />
      {count && (
        <span className="absolute -right-[7px] -top-[9px] flex h-[16px] w-[16px] items-center justify-center rounded-full text-[10px] font-semibold text-white" style={{ background: theme.pink }}>
          {count}
        </span>
      )}
    </span>
  )
}
