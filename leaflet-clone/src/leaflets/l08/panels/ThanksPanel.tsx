import { Divider, Panel, Placed } from '../../../ui'
import { Lines, Shapes } from '../../shared-0812'
import { CornerBrackets } from '../components/CornerBrackets'
import { InfoList } from '../components/InfoList'
import { RoundCard } from '../components/RoundCard'
import { SectionHeading } from '../components/SectionHeading'
import { thanksPanel as d } from '../data'
import { theme } from '../theme'

export function ThanksPanel() {
  return (
    <Panel>
      <Shapes items={d.art} />
      <Placed x={0} y={234} width={480}>
        <SectionHeading
          title={d.title}
          body={d.body}
          titleClassName="text-[37px] leading-[48px]"
          bodyClassName="mt-[9px] text-[14px] leading-[23px] tracking-[-0.3px]"
        />
      </Placed>
      <Placed x={29} y={418} width={428}>
        <Divider color={theme.rule} thickness={2} />
      </Placed>
      <Placed x={42} y={462} width={430}>
        <InfoList rows={d.info} />
      </Placed>
      <RoundCard x={30} y={657} width={168} height={168} className="flex items-center justify-center">
        <CornerBrackets size={118} arm={38} thickness={5} />
      </RoundCard>
      <Placed x={215} y={672}>
        <Lines lines={d.cta.lines} className="text-[19px] leading-[26px] font-black text-[#1c1c1c]" />
        <div className="mt-[4px] text-[12.5px] font-semibold text-[#333]">{d.cta.note}</div>
      </Placed>
    </Panel>
  )
}
