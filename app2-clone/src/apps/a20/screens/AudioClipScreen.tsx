import { ChevronLeft, Ellipsis, Pause, RotateCcw, RotateCw, Search, SquareArrowOutUpRight } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { GnStatusBar } from '../components/GnStatusBar'
import { EditorChrome } from '../components/EditorChrome'
import { Grabber } from '../components/Grabber'
import { PillTabs } from '../components/PillTabs'
import { FeedbackIcons } from '../components/FeedbackIcons'
import { audioClip, editor } from '../data'

function SkipIcon({ forward }: { forward?: boolean }) {
  const Icon = forward ? RotateCw : RotateCcw
  return (
    <span className="relative flex h-[24px] w-[24px] items-center justify-center">
      <Icon size={23} strokeWidth={1.7} className="absolute" />
      <span className="mt-[2px] text-[7.5px] font-bold">10</span>
    </span>
  )
}

export function AudioClipScreen() {
  const a = audioClip
  return (
    <AppScreen className="font-dm">
      <EditorChrome tabs={editor.tabs} />
      <div className="absolute inset-0 bg-black/[0.23]" />
      <GnStatusBar color="#fff" chipClassName="[&>span]:!bg-[#6b6e75]" />

      <section className="absolute left-[8px] right-[8px] top-[407px] h-[430px] rounded-[36px] bg-white">
        <Grabber className="absolute left-1/2 top-[5px] -translate-x-1/2" />
        <ChevronLeft size={24} strokeWidth={1.8} className="absolute left-[24px] top-[24px]" />
        <div className="absolute inset-x-0 top-[26px] text-center text-[15.5px] font-semibold text-black">{a.title}</div>
        <Search size={18} strokeWidth={1.8} className="absolute left-[274px] top-[27px]" />
        <Ellipsis size={20} strokeWidth={1.8} className="absolute left-[327px] top-[26px]" />
        <PillTabs
          items={a.tabs}
          active="Summary"
          className="absolute left-[18px] top-[73px] h-[31px] w-[338px]"
          itemClassName="text-[12px] font-medium text-[#222]"
        />
        <div className="absolute inset-x-0 top-[199px] border-t border-[#f0f0f0]" />
        <div className="absolute left-[19px] top-[210px] flex h-[27px] items-center gap-[7px] rounded-full bg-[#edf1f6] px-[13px] text-[14px] text-[#3e72c8]">
          <SquareArrowOutUpRight size={17} strokeWidth={1.6} />
          {a.view}
        </div>
        <FeedbackIcons className="absolute left-[277px] top-[215px]" gap={14} size={16} />
        <div className="absolute inset-x-0 top-[247px] border-t border-[#f0f0f0]" />

        <div className="absolute left-[19px] top-[265px] flex h-[34px] w-[41px] items-center justify-center rounded-[9px] bg-[#ededed] text-[12.5px] font-medium">
          {a.speed}
        </div>
        <div className="absolute left-[132px] top-[265px] flex items-center gap-[13px]">
          <SkipIcon />
          <span className="flex h-[33px] w-[33px] items-center justify-center rounded-[9px] bg-[#ddeff7]">
            <Pause size={18} fill="#3f71ab" stroke="#3f71ab" strokeWidth={1} />
          </span>
          <SkipIcon forward />
        </div>
        <Ellipsis size={18} strokeWidth={1.8} className="absolute left-[333px] top-[272px] text-[#666]" />

        <div className="absolute left-[19px] right-[20px] top-[306px] h-[6px] rounded-full bg-[#e9e9e9]">
          <div className="h-full rounded-full bg-[#4e7be4]" style={{ width: `${a.progress * 100}%` }} />
          <span
            className="absolute top-1/2 h-[16px] w-[16px] -translate-x-1/2 -translate-y-1/2 rounded-full bg-white shadow-[0_1px_3px_rgba(0,0,0,0.3)]"
            style={{ left: `${a.progress * 100}%` }}
          />
        </div>
        <div className="absolute left-[19px] right-[20px] top-[321px] flex justify-between text-[10.5px] text-[#888]">
          <span>{a.elapsed}</span>
          <span>{a.title}</span>
          <span>{a.total}</span>
        </div>
        <div className="absolute inset-x-0 top-[350px] text-center text-[8px] text-[#999]">{a.disclaimer}</div>
      </section>
    </AppScreen>
  )
}
