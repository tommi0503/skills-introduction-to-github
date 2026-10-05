import { Panel, Placed } from '../../../ui'
import { DisplayTitle } from '../../shared-3031/components/DisplayTitle'
import { growth } from '../../shared-3031/theme'
import { AudienceCardView } from '../components/AudienceCardView'
import { audience } from '../data'

/** Panel 1 — target audiences. */
export function AudiencePanel() {
  return (
    <Panel background={growth.paleBg}>
      <Placed x={0} y={103} width={490}>
        <DisplayTitle lines={audience.title} color={growth.ink} className="text-[33px] leading-[48px] tracking-[2.5px]" />
      </Placed>
      {audience.cards.map((c) => (
        <AudienceCardView key={c.key} card={c} />
      ))}
    </Panel>
  )
}
