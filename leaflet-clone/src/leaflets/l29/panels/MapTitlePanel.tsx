import { Panel, Placed } from '../../../ui'
import { LeafHeading } from '../../shared-2829/components/LeafHeading'
import { areaMap } from '../data'

/** Panel 2 — carries the map heading; the map itself spans panels 2–3 (sheet overlay). */
export function MapTitlePanel() {
  return (
    <Panel>
      <Placed x={57} y={63}>
        <LeafHeading title={areaMap.title} titleClassName="text-[24px]" />
      </Placed>
    </Panel>
  )
}
