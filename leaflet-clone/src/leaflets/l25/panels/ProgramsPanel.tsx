import { Divider, Panel, Placed } from '../../../ui'
import { library } from '../../shared-2425/theme'
import { HeadingCapsule } from '../components/HeadingCapsule'
import { ProgramRow } from '../components/ProgramRow'
import { programGroups } from '../data'
import { layout, panelBg } from '../theme'

const L = layout.programs
const PILL_X = 55

/** Panel 1 — three programme groups. */
export function ProgramsPanel() {
  return (
    <Panel background={panelBg.programs}>
      {programGroups.map((g, gi) => {
        const top = L.headingYs[gi]
        return (
          <div key={g.title}>
            <HeadingCapsule title={g.title} style={{ left: L.x, top, width: L.width, height: L.headingH }} />
            {g.items.map((it, ii) => (
              <Placed key={it.label} x={PILL_X} y={top + L.headingH + L.firstItemGap + ii * L.itemPitch}>
                <ProgramRow item={it} pillW={L.pillW} pillH={L.pillH} descX={L.descX - PILL_X} />
              </Placed>
            ))}
            <Placed x={L.descX} y={top + L.headingH + L.firstItemGap + L.pillH + 11} width={237}>
              <Divider dashed color={library.rule} thickness={1.5} />
            </Placed>
          </div>
        )
      })}
    </Panel>
  )
}
