import { brand } from '../data'
import { CartBadge } from './CartBadge'

/** "TheKitchen~" wordmark row with the cart badge. Positioned by the parent. */
export function BrandBar({ cartCount }: { cartCount: number }) {
  return (
    <div className="flex h-[36px] items-center justify-between">
      <span className="font-poppins text-[27px] leading-none font-semibold tracking-[-0.01em] text-white">{brand}</span>
      <CartBadge count={cartCount} />
    </div>
  )
}
