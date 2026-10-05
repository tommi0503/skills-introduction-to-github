import { ArrowDown, ArrowLeft, ChevronDown, CreditCard, LoaderCircle, Shield } from 'lucide-react'
import { AppScreen, HomeIndicator, ImagePlaceholder, StatusBar } from '../../../ui'
import { PillButton } from '../components/WhiteButton'
import { addMoney } from '../data'
import { rv } from '../theme'

export function AddMoney() {
  const { source, target } = addMoney
  return (
    <AppScreen className="font-inter" background={rv.black}>
      <StatusBar color="#fff" />
      <div className="mt-[7px] flex h-[36px] items-center justify-between px-[16px] text-white">
        <ArrowLeft size={21} strokeWidth={2} />
        <Shield size={20} fill={rv.shield} color={rv.shield} />
      </div>
      <h1 className="mt-[8px] px-[17px] text-[27px] leading-[36px] font-bold text-white">{addMoney.title}</h1>

      <div className="relative mx-[17px] mt-[21px] text-white">
        <div className="flex h-[85px] items-center rounded-[14px] px-[16px]" style={{ background: rv.card }}>
          <span className="flex h-[40px] w-[40px] items-center justify-center rounded-full" style={{ background: '#2c3a5e' }}>
            <CreditCard size={18} strokeWidth={2.2} color="#7da0ff" />
          </span>
          <div className="ml-[16px] flex-1">
            <div className="text-[14px] font-medium">{source.name}</div>
            <div className="mt-[3px] text-[12.5px]" style={{ color: rv.muted }}>
              {source.detail}
            </div>
          </div>
          <span className="flex h-[39px] items-center rounded-full px-[16px] text-[13.5px] font-medium" style={{ background: rv.pill }}>
            {source.action}
          </span>
        </div>
        <div className="mt-[9px] flex h-[79px] items-start justify-between rounded-[14px] px-[16px] pt-[15px]" style={{ background: rv.card }}>
          <div>
            <div className="flex items-center gap-[6px] text-[15px] font-medium">
              <ImagePlaceholder className="h-[24px] w-[24px] rounded-full" label="SGD flag" />
              {target.currency}
              <ChevronDown size={14} strokeWidth={2.4} />
            </div>
            <div className="mt-[6px] text-[11px]" style={{ color: rv.muted }}>
              {target.balance}
            </div>
          </div>
          <div className="text-right">
            <div className="text-[19px] leading-[24px] font-bold">{target.amount}</div>
            <div className="mt-[6px] text-[11px]" style={{ color: rv.muted }}>
              {target.fee}
            </div>
          </div>
        </div>
        <span className="absolute top-[78px] left-1/2 flex h-[26px] w-[26px] -translate-x-1/2 items-center justify-center rounded-full bg-black">
          <ArrowDown size={13} strokeWidth={2.2} />
        </span>
      </div>

      <div className="absolute inset-x-[17px] top-[737px]">
        <PillButton background="#d6d6d6">
          <LoaderCircle size={17} strokeWidth={1.8} />
        </PillButton>
      </div>
      <HomeIndicator tone="light" />
    </AppScreen>
  )
}
