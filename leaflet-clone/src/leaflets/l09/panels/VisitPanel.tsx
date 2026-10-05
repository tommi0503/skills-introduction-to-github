import { Divider, ImagePlaceholder, Panel, Placed } from '../../../ui'
import { Lines } from '../../shared-0812'
import { StackTitle } from '../components/StackTitle'
import { visitPanel as d } from '../data'
import { theme } from '../theme'

export function VisitPanel() {
  return (
    <Panel>
      <Placed x={53} y={62} width={270} height={388}>
        <ImagePlaceholder className="h-full w-full" label="map" />
      </Placed>
      <Placed x={411} y={50}>
        <StackTitle text={d.directions.heading} />
      </Placed>
      <Placed x={47} y={568}>
        <div className="text-[21px] leading-[28px] text-[#333]">{d.directions.address}</div>
        <div className="mt-[9px] text-[15px] leading-[18px] text-[#444]">{d.directions.note}</div>
      </Placed>
      <Placed x={25} y={665} width={423}>
        <Divider color={theme.rule} thickness={2} />
      </Placed>
      <Placed x={411} y={692}>
        <StackTitle text={d.hours.heading} />
      </Placed>
      <Placed x={45} y={847}>
        <Lines lines={d.hours.lines} className="text-[21.5px] leading-[35px] text-[#333]" />
      </Placed>
      <Placed x={25} y={934} width={423}>
        <Divider color={theme.rule} thickness={2} />
      </Placed>
      <Placed x={47} y={955} className="text-[16.5px] leading-[20px] text-[#555]">
        {d.contact}
      </Placed>
    </Panel>
  )
}
