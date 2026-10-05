import { Button } from '../../../ui'
import type { StoreCart } from '../data'
import { checkoutLabel, subtotalLabel } from '../data'
import { theme } from '../theme'
import { CartItemRow } from './CartItemRow'
import { StoreHeader } from './StoreHeader'

/** One merchant's cart: header, items and (when present) subtotal + checkout. */
export function StoreSection({ store }: { store: StoreCart }) {
  return (
    <section className="px-[20px]">
      <StoreHeader store={store} />
      <div className="mt-[17px] flex flex-col gap-[16px]">
        {store.items.map((it) => (
          <CartItemRow key={it.id} item={it} />
        ))}
      </div>
      {store.subtotal && (
        <>
          <div className="mt-[16px] flex justify-between text-[13.5px] leading-[18px]">
            <span className="font-semibold text-[#111]">{subtotalLabel}</span>
            <span style={{ color: theme.price }}>{store.subtotal}</span>
          </div>
          <Button
            className="mt-[16px] h-[43px] w-full rounded-[10px] text-[15.5px] font-medium text-white"
            style={{ background: theme.accent }}
          >
            {checkoutLabel}
          </Button>
        </>
      )}
    </section>
  )
}
