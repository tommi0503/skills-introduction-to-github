import { Panel, Placed } from '../../../ui'
import { DisplayTitle } from '../../shared-3031/components/DisplayTitle'
import { RichLines } from '../../shared-3031/components/RichLines'
import { growth } from '../../shared-3031/theme'
import { services } from '../data'

/** Panel 2 — services heading; the service grid itself spans panels 2–3 (sheet overlay). */
export function ServicesPanel() {
  return (
    <Panel>
      <Placed x={0} y={103} width={470}>
        <DisplayTitle lines={services.title} color={growth.ink} className="text-[33px] leading-[50px] tracking-[2.5px]" />
      </Placed>
      <Placed x={80} y={255}>
        <RichLines lines={services.lead} className="text-[17.5px] font-medium leading-[24.5px] tracking-[-0.4px]" strongClassName="font-bold text-[var(--ink)]" />
      </Placed>
    </Panel>
  )
}
