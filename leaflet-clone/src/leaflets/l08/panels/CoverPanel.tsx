import { Panel, Pill, Placed } from '../../../ui'
import { Lines, Shapes } from '../../shared-0812'
import { ArcText } from '../components/ArcText'
import { coverPanel as d } from '../data'
import { theme } from '../theme'

export function CoverPanel() {
  return (
    <Panel>
      <Placed x={57} y={54} width={368} height={44}>
        <Pill className="h-full w-full border-2 border-[#e2e0da] bg-[#f8f8f6] text-[14px] font-semibold text-[#333]">
          {d.handle}
        </Pill>
      </Placed>
      <Placed x={176} y={174}>
        <ArcText text={d.arc} width={128} height={44} radius={62} className="text-[16px] font-extrabold" color={theme.ink} />
      </Placed>
      <Placed x={0} y={224} width={480} className="text-center font-jua tracking-[9px] pl-[9px]" style={{ WebkitTextStroke: '3px currentColor' }}>
        <div className="text-[92px] leading-[100px]" style={{ color: theme.orange }}>
          {d.title[0]}
        </div>
        <div className="text-[92px] leading-[100px]" style={{ color: theme.ink }}>
          {d.title[1]}
        </div>
      </Placed>
      <Placed x={0} y={434} width={480}>
        <Lines lines={d.tagline} className="text-center text-[15px] leading-[24px] font-bold text-[#222]" />
      </Placed>
      <Shapes items={d.art} />
    </Panel>
  )
}
