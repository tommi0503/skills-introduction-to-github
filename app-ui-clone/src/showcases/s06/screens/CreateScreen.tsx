import { Sparkles, WandSparkles } from 'lucide-react'
import { OutlineChip } from '../components/OutlineChip'
import { PrimaryButton } from '../components/PrimaryButton'
import { QuickStartRow } from '../components/QuickStartRow'
import { ScreenTitle } from '../components/ScreenTitle'
import { SoftIconButton } from '../components/SoftIconButton'
import { create, quickStart } from '../data'
import { softShadow, theme } from '../theme'

export function CreateScreen() {
  return (
    <div className="absolute inset-0 bg-white font-inter">
      <ScreenTitle
        title={create.title}
        className="absolute left-[18px] right-[17px] top-[66px]"
        trailing={<SoftIconButton icon={Sparkles} color={theme.blue} iconSize={18} />}
      />
      <p className="absolute left-[18px] top-[137px] text-[14.5px] text-[#6a6a6a]">{create.prompt}</p>

      <div
        className="absolute left-[18px] top-[170px] h-[170px] w-[340px] rounded-[18px] border border-[#ececec] px-[19px] pt-[21px]"
        style={{ background: theme.card, boxShadow: softShadow }}
      >
        <p className="text-[12.5px] text-[#c2c2c2]">{create.placeholder}</p>
        <div className="absolute inset-x-[19px] bottom-[8px] flex items-center justify-between">
          <OutlineChip label={create.generate} icon={WandSparkles} className="h-[37px] w-[91px] text-[13px]" />
          <span className="text-[16px] text-[#b0b0b0]">{create.counter}</span>
        </div>
      </div>

      <div className="absolute left-[18px] top-[364px] h-[340px] w-[340px] rounded-[20px] px-[15px] pt-[16px]" style={{ background: theme.panel }}>
        <p className="pl-[4px] text-[15px] text-[#555]">{create.quickStart}</p>
        <div className="mt-[15px] flex flex-col gap-[8px]">
          {quickStart.map((q, i) => (
            <QuickStartRow key={q.key} item={q} selected={i === 0} />
          ))}
        </div>
      </div>

      <div className="absolute inset-x-0 top-[650px] h-[160px] bg-gradient-to-b from-white/0 via-white/90 to-white" />
      <PrimaryButton label={create.cta} icon={Sparkles} className="absolute left-[18px] top-[708px] w-[340px]" />
    </div>
  )
}
