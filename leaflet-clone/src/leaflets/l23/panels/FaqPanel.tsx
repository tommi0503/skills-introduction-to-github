import { Panel, Placed } from '../../../ui'
import { Blob } from '../../shared-2223/components/Blob'
import { BlobCard } from '../../shared-2223/components/BlobCard'
import { OutlineBar } from '../../shared-2223/components/OutlineBar'
import { SectionTitle } from '../../shared-2223/components/SectionTitle'
import { JustifiedLines } from '../components/JustifiedLines'
import { faqPanel as d } from '../data'

const FAQ_TOP = 155
const FAQ_STEP = 225

export function FaqPanel() {
  return (
    <Panel>
      <BlobCard x={22} y={40} width={418} height={936} radius="62px 66px 56px 48px / 56px 86px 44px 44px" />
      <SectionTitle top={82} centerX={240} className="text-[35px] text-[#62a871]">
        {d.heading}
      </SectionTitle>
      {d.faqs.map((f, i) => (
        <Placed key={f.q} x={68} y={FAQ_TOP + i * FAQ_STEP} width={340}>
          <OutlineBar className="text-[20px]">
            <span className="ml-[16px] font-dohyeon text-[#80bd8c]">Q. {f.q}</span>
          </OutlineBar>
          <div className="mt-[18px] flex">
            <span className="w-[27px] pl-[20px] font-dohyeon text-[19px] leading-[28.5px] text-[#76b282]">A.</span>
            <JustifiedLines lines={f.a} className="ml-[20px] w-[293px] text-[19.5px] font-semibold leading-[28.5px] tracking-[-0.05em] text-[#46484b]" />
          </div>
        </Placed>
      ))}
      {d.art.map((s) => (
        <Blob key={s.id} shape={s} />
      ))}
    </Panel>
  )
}
