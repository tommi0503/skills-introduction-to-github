import { CircleCheck, Star, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { PhoneStatus } from '../components/PhoneStatus'
import { Sheet } from '../components/Sheet'
import { paywall, type PaywallPlan } from '../data'
import { theme } from '../theme'

function PlanOption({ plan }: { plan: PaywallPlan }) {
  const on = 'selected' in plan && plan.selected
  return (
    <div
      className={cn('relative flex h-[102px] w-[169px] flex-col items-center justify-center rounded-[14px]', on ? 'border-2 border-white/90 bg-[#1e2442]' : 'border border-white/25')}
    >
      {'badge' in plan && (
        <span className="absolute top-[-13px] rounded-full px-[11px] text-[12px] leading-[22px] font-semibold text-white" style={{ background: theme.badge }}>
          {plan.badge}
        </span>
      )}
      <div className="flex items-center gap-[9px]">
        {on ? (
          <CircleCheck size={21} fill="#fff" color="#1e2442" strokeWidth={2.4} />
        ) : (
          <span className="h-[20px] w-[20px] rounded-full bg-[#5f6378]" />
        )}
        <span className={cn('text-[17px] font-semibold', on ? 'text-white' : 'text-[#c8cad6]')}>{plan.name}</span>
      </div>
      <span className="mt-[5px] text-[14px] leading-[20px] font-bold text-white">{plan.price}</span>
      <span className="text-[11px] leading-[16px] text-[#9aa0b8]">{plan.trial}</span>
    </div>
  )
}

export function PaywallScreen() {
  return (
    <AppScreen background={theme.sheetBackdrop} className="font-jakarta">
      <PhoneStatus />
      <Sheet style={{ background: `linear-gradient(to bottom, ${theme.navyTop}, ${theme.navyBottom})` }}>
        <div className="absolute top-[17px] left-[342px] flex h-[30px] w-[30px] items-center justify-center rounded-full bg-white/25 text-white">
          <X size={16} strokeWidth={2.4} />
        </div>
        <ImagePlaceholder tone="#d8d8d4" label="Fixtured 3D mark" className="absolute top-[57px] left-[177px] h-[54px] w-[46px] rounded-[10px]" />
        <h1 className="absolute inset-x-0 top-[103px] text-center font-condensed text-[45px] leading-[54px] font-black tracking-[-1.5px] text-white">
          {paywall.title}
        </h1>
        <p className="absolute top-[163px] left-[55px] w-[280px] text-center text-[14.5px] leading-[20px] font-medium text-[#a9afc6]">{paywall.subtitle}</p>
        <div className="absolute top-[224px] left-[253px] h-[284px] w-[54px] rounded-[10px]" style={{ background: theme.freeCol }} />
        <div
          className="absolute top-[224px] left-[315px] h-[284px] w-[55px] rounded-[10px]"
          style={{ background: 'linear-gradient(to bottom, #121580 0%, #2a32b4 40%, #b3d6f8 100%)' }}
        />
        <span className="absolute top-[234px] left-[253px] w-[54px] text-center text-[12px] font-medium text-[#9aa0b8]">Free</span>
        <span className="absolute top-[234px] left-[315px] w-[55px] text-center text-[12px] font-bold text-white">Plus</span>
        <div className="absolute top-[258px] left-[19px] flex w-[351px] flex-col">
          {paywall.features.map((f) => (
            <div key={f} className="flex h-[41.8px] items-center">
              <span className="flex-1 text-[14.5px] font-semibold tracking-[0.3px] text-white">{f}</span>
              <span className="flex w-[54px] justify-center text-[#4a506a]">
                <X size={15} strokeWidth={1.5} />
              </span>
              <span className="ml-[8px] flex w-[55px] justify-center">
                <CircleCheck size={17} fill="#fff" color="#1f2a90" strokeWidth={2.6} />
              </span>
            </div>
          ))}
        </div>
        <div className="absolute top-[528px] left-[-6px] h-[60px] w-[14px] rounded-[14px] border border-white/15" />
        <div className="absolute top-[528px] left-[382px] h-[60px] w-[14px] rounded-[14px] border border-white/15" />
        <div className="absolute top-[528px] left-[23px] flex h-[70px] w-[344px] items-start justify-between rounded-[14px] border border-white/15 px-[20px] pt-[19px]">
          <span className="text-[13.5px] font-semibold text-white">{paywall.review}</span>
          <span className="flex gap-[1px]">
            {Array.from({ length: 5 }, (_, i) => (
              <Star key={i} size={14} fill={theme.stars} color={theme.stars} />
            ))}
          </span>
        </div>
        <div className="absolute inset-x-0 top-[565px] bottom-0 rounded-t-[22px] border-t border-white/10 bg-[#0a1130]">
          <div className="absolute top-[26px] left-[19px] flex gap-[13px]">
            {paywall.plans.map((p) => (
              <PlanOption key={p.key} plan={p} />
            ))}
          </div>
          <button className="absolute top-[144px] left-[19px] flex h-[46px] w-[351px] items-center justify-center rounded-full bg-white text-[15px] font-semibold text-[#222]">
            {paywall.cta}
          </button>
        </div>
      </Sheet>
    </AppScreen>
  )
}
