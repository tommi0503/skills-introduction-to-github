import { Plus, X } from 'lucide-react'
import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'
import { ActionListRow, CartItemRow, FeeLine } from '../components/CheckoutRows'
import { checkout } from '../data'
import { uber } from '../theme'

/** Uber Eats checkout presented as a sheet over a stacked (dimmed) card. */
export function Checkout() {
  return (
    <AppScreen className="font-inter" background="#000">
      <StatusBar color="#fff" />
      <div className="absolute top-[46px] right-[18px] left-[18px] h-[20px] rounded-t-[10px]" style={{ background: uber.sheetBack }} />
      <div className="absolute inset-x-0 top-[56px] bottom-0 rounded-t-[12px] bg-white" style={{ color: uber.ink }}>
        <header className="relative flex h-[60px] items-center justify-center">
          <X size={24} strokeWidth={2.6} className="absolute left-[22px]" />
          <h1 className="text-[17px] font-medium">{checkout.title}</h1>
        </header>
        <div className="px-[18px]">
          <div className="flex h-[54px] items-center justify-between">
            <h2 className="text-[17px] font-medium">{checkout.itemsTitle}</h2>
            <span className="mr-[8px] text-[13px] font-medium" style={{ color: uber.green }}>
              {checkout.seeMenu}
            </span>
          </div>
          {checkout.items.map((it) => (
            <CartItemRow key={it.name} item={it} />
          ))}
          <div className="h-px" style={{ background: uber.hairline }} />
          <button
            type="button"
            className="mt-[18px] flex h-[37px] items-center gap-[10px] rounded-full px-[18px] text-[13.5px] font-medium"
            style={{ background: uber.chip }}
          >
            <Plus size={15} strokeWidth={2.4} />
            {checkout.addItems}
          </button>
        </div>
        <div className="mt-[16px] h-px" style={{ background: uber.hairline }} />
        {checkout.actions.map((a) => (
          <ActionListRow key={a.key} row={a} />
        ))}
        <div className="px-[18px]">
          <div
            className="mt-[18px] flex h-[58px] items-center gap-[14px] rounded-[10px] px-[16px] text-[15px] font-semibold"
            style={{ background: uber.upsellBg }}
          >
            <UberOneGlyph color={uber.upsellIcon} />
            {checkout.upsell}
          </div>
          <div className="mt-[27px]">
            {checkout.fees.map((f) => (
              <FeeLine key={f.label} row={f} />
            ))}
          </div>
        </div>
        <div className="mt-[2px] h-px" style={{ background: uber.hairline }} />
        <div className="px-[18px] pt-[16px]">
          <button type="button" className="flex h-[58px] w-full items-center justify-center bg-black text-[17px] font-medium text-white">
            {checkout.cta}
          </button>
        </div>
      </div>
      <HomeIndicator />
    </AppScreen>
  )
}

/** Simple ring-with-quarter mark used for the membership upsell (drawn with plain shapes). */
function UberOneGlyph({ color }: { color: string }) {
  return (
    <svg width={24} height={24} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2.4}>
      <circle cx={12} cy={12} r={10} />
      <path d="M12 2v20M12 12H2" />
    </svg>
  )
}
