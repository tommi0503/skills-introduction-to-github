import { Send, Sparkles, TextAlignStart, ThumbsDown, ThumbsUp } from 'lucide-react'
import { OutlineChip } from '../components/OutlineChip'
import { PrimaryButton } from '../components/PrimaryButton'
import { ScoreRing } from '../components/ScoreRing'
import { ScreenTitle } from '../components/ScreenTitle'
import { SoftIconButton } from '../components/SoftIconButton'
import { draft } from '../data'
import { theme } from '../theme'

const feedback = [ThumbsUp, ThumbsDown]

export function DraftScreen() {
  return (
    <div className="absolute inset-0 bg-white font-inter">
      <ScreenTitle title={draft.title} className="absolute left-[18px] right-[17px] top-[66px]" trailing={<SoftIconButton icon={TextAlignStart} />} />
      <p className="absolute left-[18px] top-[137px] text-[14.5px] text-[#6a6a6a]">{draft.subtitle}</p>

      <div className="absolute left-[42px] top-[177px]">
        <ScoreRing value={draft.score} label={draft.scoreLabel} />
      </div>

      <div className="absolute left-[18px] top-[497px] h-[175px] w-[340px] rounded-[20px] px-[14px] pt-[13px]" style={{ background: theme.panel }}>
        <div className="flex h-[85px] items-center rounded-[16px] bg-[#fcfcfc] pl-[15px] shadow-[0_2px_6px_rgba(0,0,0,0.03)]">
          <span className="flex h-[52px] w-[52px] items-center justify-center rounded-[12px] bg-[#f6f6f2]">
            <Sparkles size={19} strokeWidth={1.6} color={theme.blue} />
          </span>
          <div className="ml-[13px] pt-[4px]">
            <p className="text-[15.5px] font-semibold tracking-[-0.2px] text-[#111]">{draft.tipTitle}</p>
            <p className="mt-[5px] text-[11px] tracking-[-0.2px] text-[#b3b3b3]">{draft.tipBody}</p>
          </div>
        </div>
        <div className="mt-[13px] flex items-center gap-[10px]">
          {feedback.map((Icon, i) => (
            <span key={i} className="flex h-[50px] w-[50px] items-center justify-center rounded-[12px] bg-white">
              <Icon size={20} strokeWidth={1.6} color="#222" />
            </span>
          ))}
          <OutlineChip label={draft.tipAction} className="ml-auto h-[49px] w-[103px] text-[15px]" />
        </div>
      </div>

      <PrimaryButton label={draft.cta} icon={Send} className="absolute left-[18px] top-[705px] w-[340px]" />
    </div>
  )
}
