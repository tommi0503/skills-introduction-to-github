import { Divider, ImagePlaceholder, Panel, Placed } from '../../../ui'
import { PanelTitle } from '../../shared-3435/components/PanelTitle'
import { larana } from '../../shared-3435/theme'
import { DirectionList } from '../components/DirectionList'
import { HoursTable } from '../components/HoursTable'
import { directions, hours } from '../data'

/** Middle outside panel: map, directions, opening hours. */
export function DirectionsPanel() {
  return (
    <Panel background={larana.paper}>
      <Placed x={0} y={52} width={488}>
        <PanelTitle>{directions.title}</PanelTitle>
      </Placed>
      <Placed x={65} y={114}>
        <ImagePlaceholder label="약도" className="rounded-[14px]" style={{ width: 376, height: 183 }} />
      </Placed>
      <Placed x={78} y={322} width={380}>
        <DirectionList items={directions.items} />
      </Placed>
      <Placed x={55} y={634} width={395}>
        <Divider color={larana.line} thickness={1.5} />
      </Placed>
      <Placed x={0} y={691} width={506}>
        <PanelTitle>{hours.title}</PanelTitle>
      </Placed>
      <Placed x={65} y={752} width={381}>
        <HoursTable rows={hours.rows} />
      </Placed>
      <Placed x={0} y={909} width={506} className="text-center text-[17px] font-bold leading-[24px]" style={{ color: larana.ink }}>
        {hours.note}
      </Placed>
    </Panel>
  )
}
