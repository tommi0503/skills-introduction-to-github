import { ArrowLeft, Sparkles } from 'lucide-react'
import { AppScreen, HomeIndicator, ImagePlaceholder, StatusBar } from '../../../ui'
import { PillButton } from '../components/WhiteButton'
import { cardPicker } from '../data'
import { rv } from '../theme'

export function CardPicker() {
  return (
    <AppScreen className="font-inter" background={rv.black} style={{ background: rv.cardGradient }}>
      <StatusBar color="#fff" />
      <div className="relative mt-[7px] flex h-[36px] items-center justify-center text-white">
        <ArrowLeft size={21} strokeWidth={2} className="absolute left-[16px]" />
        <span className="flex h-[22px] items-center gap-[5px] rounded-full bg-black/55 px-[11px] text-[10.5px] font-medium">
          <Sparkles size={9} fill="#fff" />
          {cardPicker.badge}
        </span>
      </div>
      <ImagePlaceholder tone="#8a8a8e" className="absolute top-[137px] left-[80px] h-[364px] w-[230px] rounded-[12px]" label="Revolut card" />
      <ImagePlaceholder tone="#cfcfd3" className="absolute top-[140px] left-[378px] h-[360px] w-[40px] rounded-[10px]" label="next card" />
      <div className="absolute inset-x-[30px] top-[541px] text-center text-white">
        <div className="text-[13.5px] font-semibold">{cardPicker.title}</div>
        <p className="mt-[10px] text-[12.5px] leading-[19px] text-white/65">{cardPicker.body}</p>
      </div>
      <div className="absolute top-[650px] left-[172px] flex items-center gap-[17px]">
        {cardPicker.swatches.map((s) => {
          const on = s.key === cardPicker.selected
          return (
            <span
              key={s.key}
              className="flex items-center justify-center rounded-full"
              style={{ width: 46, height: 46, border: on ? '2px solid rgba(255,255,255,0.55)' : 'none' }}
            >
              <span className="rounded-full" style={{ width: on ? 36 : 40, height: on ? 36 : 40, background: s.color }} />
            </span>
          )
        })}
      </div>
      <div className="absolute inset-x-[16px] top-[738px]">
        <PillButton>{cardPicker.cta}</PillButton>
      </div>
      <HomeIndicator tone="light" />
    </AppScreen>
  )
}
