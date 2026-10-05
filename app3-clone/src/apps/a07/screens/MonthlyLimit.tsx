import { X } from 'lucide-react'
import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'
import { Keypad } from '../components/Keypad'
import { PillButton } from '../components/WhiteButton'
import { keypad, limit } from '../data'
import { rv } from '../theme'

export function MonthlyLimit() {
  return (
    <AppScreen className="font-inter" background={rv.black}>
      <StatusBar color="#fff" />
      <div className="absolute inset-x-[16px] top-[58px] h-[20px] rounded-t-[10px]" style={{ background: '#151517' }} />
      <div className="absolute inset-x-0 top-[70px] bottom-0 rounded-t-[12px] text-white" style={{ background: rv.sheet }}>
        <div className="relative flex h-[52px] items-center justify-center">
          <X size={19} strokeWidth={2.2} className="absolute left-[19px]" />
          <span className="text-[14px] font-medium">{limit.title}</span>
        </div>
        <div className="mt-[123px] flex items-center justify-center">
          <span className="text-[40px] leading-[46px] font-bold">{limit.amount}</span>
          <span className="ml-[1px] h-[40px] w-[2px]" style={{ background: rv.caret }} />
        </div>
        <p className="mt-[3px] text-center text-[11.5px]" style={{ color: rv.muted }}>
          {limit.spent}
        </p>
        <div className="mx-[16px] mt-[123px]">
          <PillButton>{limit.cta}</PillButton>
        </div>
        <div className="absolute inset-x-0 top-[438px] bottom-0" style={{ background: rv.keypadBg }}>
          <div className="flex h-[54px] items-center justify-around px-[24px] text-[16px] font-semibold">
            {limit.operators.map((o) => (
              <span key={o}>{o}</span>
            ))}
          </div>
          <Keypad keys={keypad} className="px-[7px]" keyHeight={46} gap={7} keyColor={rv.key} />
        </div>
      </div>
      <HomeIndicator tone="light" />
    </AppScreen>
  )
}
