import { ArrowRight, Brain, UserPlus } from 'lucide-react'
import { AppScreen, cn, ImagePlaceholder } from '../../../ui'
import { BottomNav } from '../components/BottomNav'
import { ImprovementCard } from '../components/ImprovementCard'
import { NeoBox } from '../components/NeoBox'
import { StatusOverlay } from '../components/StatusOverlay'
import { improvementFilters, improvements, momentum } from '../data'

export function MomentumScreen() {
  return (
    <AppScreen background="#dbb882" className="font-sora text-white">
      <div
        className="absolute rounded-full"
        style={{ left: 83, top: 115, width: 226, height: 226, background: 'radial-gradient(circle, #ebd3a6 0%, #e4c897 60%, rgba(219,184,130,0) 72%)' }}
      />
      <StatusOverlay chipClassName="bg-[#9c8c70]!" />
      <div className="absolute top-[78px] left-[20px] text-[14.5px] tracking-[-0.2px] text-white/90">{momentum.intro}</div>
      <div className="absolute top-[108px] left-[20px] flex items-baseline gap-[11px]">
        {momentum.timer.map((t) => (
          <span key={t.unit} className="text-[29px] leading-[34px] font-bold tracking-[0.3px]">
            {t.value}
            <span className="text-[13px] font-semibold">{t.unit}</span>
          </span>
        ))}
      </div>
      <ImagePlaceholder tone="#efe3cc" label="sunburst logo" className="absolute top-[168px] left-[148px] h-[70px] w-[97px] rounded-[6px]" />
      <div className="absolute top-[252px] left-0 w-full text-center text-[34px] leading-[40px] font-bold tracking-[0px]">{momentum.level}</div>
      <p className="absolute top-[302px] left-0 w-full px-[110px] text-center text-[10.5px] leading-[14px] tracking-[-0.2px] text-white/85">
        <b className="font-bold text-white">{momentum.note.strong}</b>
        {momentum.note.rest}
      </p>
      <div className="absolute top-[351px] left-[95px] flex h-[31px] w-[200px] items-center justify-center gap-[7px] rounded-[8px] bg-[#ea712c] text-[12px] font-medium">
        <Brain size={15} strokeWidth={2} />
        {momentum.cta}
        <ArrowRight size={13} strokeWidth={2.2} />
      </div>
      <div className="absolute inset-x-0 top-[413px] bottom-0 rounded-t-[28px] bg-white text-[#111]">
        <div className="mx-auto mt-[9px] h-[4px] w-[36px] rounded-full bg-[#9a9a9a]" />
        <div className="mt-[19px] flex items-center gap-[9px] pl-[20px]">
          <UserPlus size={16} strokeWidth={2.4} />
          <span className="text-[18.5px] font-bold tracking-[-0.4px]">Your Improvements</span>
        </div>
        <div className="mt-[15px] flex gap-[9px] pl-[17px] whitespace-nowrap">
          {improvementFilters.map((f, i) => (
            <NeoBox
              key={f}
              shadow={i === 0 ? '#111' : '#cfcfcf'}
              className={cn(
                'h-[33px] shrink-0 rounded-[5px] px-[14px] text-[11px]',
                i === 0 ? 'bg-[#1c1c1c] font-bold text-white' : 'border-[#999] bg-white text-[#777]',
              )}
            >
              {f}
            </NeoBox>
          ))}
        </div>
        <div className="mt-[19px] flex flex-col gap-[19px] px-[22px]">
          {improvements.map((it) => (
            <ImprovementCard key={it.id} {...it} />
          ))}
          <ImprovementCard title="" text="" tone="#3d3a36" />
        </div>
      </div>
      <BottomNav active="stats" />
    </AppScreen>
  )
}
