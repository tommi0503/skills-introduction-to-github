import { Panel, Placed } from '../../../ui'
import { Blob } from '../../shared-2223/components/Blob'
import { SectionTitle } from '../../shared-2223/components/SectionTitle'
import { theme2223 } from '../../shared-2223/theme'
import { ArcText } from '../components/ArcText'
import { coverPanel as d } from '../data'

export function CoverPanel() {
  return (
    <Panel>
      <Placed x={78} y={62}>
        <ArcText text={d.kicker} width={340} height={80} rise={38} fontSize={28} color="#e6ec96" />
      </Placed>
      <SectionTitle top={150} centerX={245} className="text-[92px] tracking-[0.01em] text-[#eef08f]">
        {d.title}
      </SectionTitle>
      <SectionTitle top={236} centerX={245} className="text-[92px] tracking-[0.01em] text-[#f7f5ea]">
        {d.subtitle}
      </SectionTitle>
      {d.art.map((s) => (
        <Blob key={s.id} shape={s} />
      ))}
      <Placed
        x={85}
        y={898}
        width={324}
        height={47}
        className="flex items-center justify-center rounded-full bg-[#f7f7f5] font-jua text-[29px] tracking-[0.02em]"
        style={{ color: theme2223.heading }}
      >
        {d.dates}
      </Placed>
    </Panel>
  )
}
