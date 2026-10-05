import { Panel, Placed } from '../../../ui'
import { InfoBlockList } from '../../shared-1314/components/InfoBlock'
import { RuledHeading } from '../../shared-1314/components/RuledHeading'
import { WaveBand } from '../../shared-1314/components/WaveBand'
import { fairTheme as t } from '../../shared-1314/theme'
import type { ListSection } from '../data'

export interface ListPanelProps {
  section: ListSection
  /** Left edge of the heading rule (panel coordinates). */
  ruleX: number
  /** Horizontal phase of the wave band so it continues across panels. */
  waveOffset: number
  /** Left edge of the entries. */
  itemX: number
}

/** Inside panel with a ruled heading and a list of titled entries (부스 소개 / 프로그램). */
export function ListPanel({ section, ruleX, waveOffset, itemX }: ListPanelProps) {
  return (
    <Panel background={t.cream} className="font-nanum-gothic">
      <RuledHeading
        x={ruleX}
        y={89}
        width={480 - ruleX - 42}
        ruleY={157}
        ruleThickness={3}
        ruleColor={t.rule}
        className="text-right text-[43px] font-extrabold leading-none tracking-[0.03em]"
      >
        <span style={{ color: t.ink }}>{section.title}</span>
      </RuledHeading>

      <Placed x={itemX} y={232} width={440 - itemX + 30}>
        <InfoBlockList
          items={section.items}
          titleGap={20}
          itemGap={70}
          titleClassName="text-[22px] font-extrabold leading-[30px]"
          titleStyle={{ color: t.ink }}
          bodyClassName="text-[22px] leading-[34px] text-[#5e5e5e]"
        />
      </Placed>

      <WaveBand x={0} y={960} width={480} height={58} scallop={{ size: 80, period: 80, offset: waveOffset }} />
    </Panel>
  )
}
