import { ChevronRight, House } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { CartItemRow, GiftSummary } from '../components/CartItemCard'
import { HighlightStatusBar } from '../components/HighlightStatusBar'
import { CheckDot, CtaButton, NavBar, Toggle } from '../components/Primitives'
import { cart, cartItems } from '../data'
import { cu } from '../theme'

const card = 'mx-[17.5px] overflow-hidden rounded-[16px] bg-white'

function DeliveryPanel() {
  return (
    <div className="absolute inset-x-0 bg-white" style={{ top: 156, height: 100 }}>
      <div className="flex items-center pr-[25px] pl-[23.7px]" style={{ marginTop: 21 }}>
        <span className="text-[17px] font-bold text-[#1a1a1a]">{cart.address.name}</span>
        <span className="ml-[5px] text-[13.5px] text-[#666]">{cart.address.detail}</span>
        <span className="ml-auto flex items-center text-[13.5px] text-[#888]">
          {cart.address.action}
          <ChevronRight size={14} strokeWidth={1.5} className="ml-[2px] text-[#bbb]" />
        </span>
      </div>
      <div className="flex items-center pr-[23.5px] pl-[23.7px]" style={{ marginTop: 13 }}>
        <span className="text-[13.5px] text-[#6a5cf0] underline underline-offset-[3px]">{cart.store.name}</span>
        <span className="text-[13.5px] text-[#777]">{cart.store.suffix}</span>
        <span className="ml-auto text-[15px] font-bold text-[#5a6ef0]">
          {cart.store.autoMatch}
          <sup className="text-[9px]">✦</sup>
        </span>
        <span className="ml-[6px]">
          <Toggle />
        </span>
      </div>
    </div>
  )
}

export function CartScreen() {
  return (
    <div className="relative h-full overflow-hidden font-pretendard" style={{ background: cu.section }}>
      <div className="absolute inset-x-0 top-0 h-[156px] bg-white" />
      <HighlightStatusBar />
      <NavBar title={cart.title} actions={[House]} />

      <div className="absolute" style={{ left: 15.3, top: 122 }}>
        <span className="block px-[4px] text-[16.5px] font-bold" style={{ color: cu.green }}>
          {cart.tab.label} {cart.tab.count}
        </span>
        <span className="mt-[8px] block h-[3px] w-[48.7px]" style={{ background: cu.green }} />
      </div>

      <DeliveryPanel />

      <div className="absolute inset-x-0" style={{ top: 272 }}>
        <div className="flex items-center pr-[24px] pl-[23.7px]">
          <CheckDot />
          <span className="ml-[7px] text-[17px] text-[#222]">{cart.selectAll}</span>
          <span className="ml-auto flex items-center gap-[9px] text-[13.5px] text-[#999]">
            {cart.bulkActions[0]}
            <span className="h-[10px] w-px bg-[#ddd]" />
            {cart.bulkActions[1]}
          </span>
        </div>

        <div className={`${card} mt-[11px] flex h-[57px] items-center pl-[18px]`}>
          <ImagePlaceholder label="coupon emblem" tone="#ece8fb" className="h-[28px] w-[28px] rounded-full" />
          <div className="ml-[11px]">
            <p className="text-[13px] leading-[18px] font-semibold text-[#222]">{cart.coupon.title}</p>
            <p className="text-[10.5px] leading-[15px] text-[#b5b5b5]">{cart.coupon.caption}</p>
          </div>
        </div>

        <div className={`${card} mt-[13.5px]`}>
          <div className="flex h-[50px] items-center gap-[6px] bg-[#f4fbf3] pl-[15px] text-[13.5px] text-[#444]">
            <span className="text-[17px]">{cart.promo.emoji}</span>
            <span>
              <b className="font-bold" style={{ color: cu.check }}>
                {cart.promo.highlight}
              </b>
              {cart.promo.text}
            </span>
          </div>
          <CartItemRow item={cartItems[0]} />
          <GiftSummary {...cart.gift} />
        </div>

        <div className={`${card} mt-[14.5px] pb-[30px]`}>
          <CartItemRow item={cartItems[1]} />
        </div>
      </div>

      <div className="absolute inset-x-0 bottom-0 bg-white" style={{ top: 744.7 }}>
        <CtaButton className="absolute text-[20px] font-bold" style={{ left: 15.3, right: 16, top: 9.1 }}>
          {cart.cta}
        </CtaButton>
      </div>
    </div>
  )
}
