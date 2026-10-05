import { EllipsisVertical, Gift, Share } from 'lucide-react'
import { AppScreen, Avatar, ImagePlaceholder } from '../../../ui'
import { FiStatusBar } from '../components/FiStatusBar'
import { OrderStepper } from '../components/OrderStepper'
import { PillButton } from '../components/PillButton'
import { order, pet } from '../data'
import { fi } from '../theme'

export function OrderScreen() {
  const { promo } = order
  return (
    <AppScreen background="#fcfcfc">
      <FiStatusBar />
      <div className="absolute left-[24px] top-[59px] flex items-center gap-[8px]">
        <Avatar size={39} />
        <span className="text-[30px] font-medium tracking-[-0.5px] text-black">{pet.name}</span>
      </div>
      <EllipsisVertical size={22} strokeWidth={2.6} className="absolute left-[342px] top-[69px]" />

      {/* order status panel */}
      <section className="absolute inset-x-0 top-[116px] h-[290px]" style={{ background: fi.panel }}>
        <h2 className="absolute left-[19px] top-[22px] text-[23px] font-medium tracking-[-0.3px] text-black">{order.title}</h2>
        <div className="absolute left-[19px] top-[60px] text-[11px]" style={{ color: fi.muted }}>{order.number}</div>
        <OrderStepper steps={order.steps} className="absolute left-[23px] top-[103px]" />
        <p className="absolute left-[22px] right-[20px] top-[189px] text-[13px] leading-[20px] tracking-[0.1px]" style={{ color: fi.muted }}>
          {order.tracking}
        </p>
        <div className="absolute inset-x-0 top-[249px] text-center text-[13px] underline underline-offset-2" style={{ color: fi.muted }}>
          {order.help}
        </div>
      </section>

      {/* referral */}
      <h3 className="absolute left-[23px] top-[434px] text-[22px] font-medium tracking-[-0.2px] text-black">{order.earnTitle}</h3>
      <div className="absolute left-[22px] top-[479px] h-[256px] w-[343px] overflow-hidden rounded-[14px]" style={{ background: fi.cream }}>
        <ImagePlaceholder className="absolute right-0 top-0 h-full w-[132px]" label="dogs photo" />
        <span className="absolute left-[19px] top-[22px] flex h-[28px] w-[28px] items-center justify-center rounded-full" style={{ background: fi.yellow }}>
          <Gift size={14} strokeWidth={2.4} fill="#000" stroke="#000" />
        </span>
        <div className="absolute left-[21px] top-[59px] w-[200px] text-[19px] font-semibold leading-[24px] tracking-[-0.3px] text-black">
          {promo.title}
        </div>
        <div className="absolute left-[21px] top-[117px] text-[13.5px] leading-[20px]" style={{ color: '#555' }}>
          {promo.body.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
        <PillButton className="absolute left-[20px] top-[193px] h-[43px] w-[304px]">
          {promo.cta}
          <Share size={15} strokeWidth={2.4} />
        </PillButton>
      </div>

      {/* sticky footer */}
      <div className="absolute inset-x-0 bottom-0 h-[103px] bg-white shadow-[0_-6px_12px_rgba(0,0,0,0.06)]">
        <PillButton className="absolute left-[22px] top-[22px] h-[43px] w-[343px]">{order.setup}</PillButton>
      </div>
    </AppScreen>
  )
}
