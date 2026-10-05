import { ArrowLeft } from 'lucide-react'
import { Divider, ImagePlaceholder, Panel, Placed } from '../../../ui'
import { SectionTitle } from '../../shared-2223/components/SectionTitle'
import { StepRow } from '../components/StepRow'
import { applyPanel as d } from '../data'

const STEP_TOPS = [235, 320, 405, 500]
const STEP_HEIGHTS = [65, 65, 82, 63]

export function ApplyPanel() {
  return (
    <Panel>
      <SectionTitle top={82} centerX={245} className="text-[34px] text-white">
        {d.heading}
      </SectionTitle>
      <Placed x={55} y={148} width={390} height={70} className="flex items-center rounded-[30px] bg-[#f7f7f5]">
        <ImagePlaceholder label="QR code" className="ml-[75px] h-[54px] w-[54px]" />
        <ArrowLeft size={18} strokeWidth={2.4} className="ml-[12px] text-[#6aa675]" />
        <span className="ml-[6px] font-dohyeon text-[17.5px] text-[#6aa675]">{d.qrCta}</span>
      </Placed>
      {d.steps.map((s, i) => (
        <Placed key={s.lines[0]} x={55} y={STEP_TOPS[i]}>
          <StepRow index={i} step={s} height={STEP_HEIGHTS[i]} />
        </Placed>
      ))}
      <Placed x={58} y={591} width={376}>
        <Divider color="rgba(255,255,255,0.85)" thickness={3} className="rounded-full" />
      </Placed>
      <SectionTitle top={638} centerX={245} className="text-[34px] text-white">
        {d.periodHeading}
      </SectionTitle>
      <Placed x={0} y={682} width={490} className="text-center text-[18.5px] font-medium tracking-[-0.03em] text-white/90">
        {d.period}
      </Placed>
      <Placed x={58} y={743} width={376}>
        <Divider color="rgba(255,255,255,0.85)" thickness={3} />
      </Placed>
      <SectionTitle top={778} centerX={245} className="text-[34px] text-white">
        {d.contactHeading}
      </SectionTitle>
      <div className="absolute left-0 top-[829px] flex w-[490px] flex-col items-center gap-[7px] text-[18px] leading-[28px] tracking-[-0.03em] text-white/90">
        {d.contacts.map((c) => (
          <span key={c.label}>
            <b className="font-bold text-white">{c.label}</b> : {c.value}
          </span>
        ))}
      </div>
    </Panel>
  )
}
