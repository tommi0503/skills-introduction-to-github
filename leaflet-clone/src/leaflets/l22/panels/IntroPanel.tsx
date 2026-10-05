import { KeyValueList, Panel } from '../../../ui'
import { Blob } from '../../shared-2223/components/Blob'
import { BlobCard } from '../../shared-2223/components/BlobCard'
import { SectionTitle } from '../../shared-2223/components/SectionTitle'
import { introPanel as d } from '../data'

export function IntroPanel() {
  return (
    <Panel>
      <BlobCard x={26} y={42} width={424} height={938} radius="70px 60px 60px 60px / 60px 80px 50px 60px" />
      {d.heading.map((line, i) => (
        <SectionTitle key={line} top={78 + i * 42} centerX={238} className="text-[35px] text-[#6aae78]">
          {line}
        </SectionTitle>
      ))}
      {d.art.map((s) => (
        <Blob key={s.id} shape={s} />
      ))}
      <KeyValueList
        className="absolute left-[70px] top-[611px] w-[360px] gap-[14px]"
        labelWidth={102}
        rowClassName="min-h-[41px] items-start"
        renderLabel={(item) => (
          <span className="flex h-[29px] w-[85px] items-center justify-center rounded-full bg-[#76b282] text-[13.5px] font-semibold tracking-[-0.04em] text-white">
            {item.label}
          </span>
        )}
        valueClassName="flex flex-col text-[20.5px] font-medium leading-[28px] tracking-[-0.04em] text-[#46484b]"
        items={d.rows.map((r) => ({
          key: r.label,
          label: r.label,
          value: r.lines.map((l) => <span key={l}>{l}</span>),
        }))}
      />
    </Panel>
  )
}
