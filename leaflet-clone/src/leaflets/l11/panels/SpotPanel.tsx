import { Panel, Placed } from '../../../ui'
import { SpotCard } from '../components/SpotCard'
import type { Spot } from '../data'
import { theme } from '../theme'

export interface SpotPanelProps {
  spot: Spot
  footer?: string
}

export function SpotPanel({ spot, footer }: SpotPanelProps) {
  return (
    <Panel background={theme.olive}>
      <Placed x={0} y={0} width={480} height={theme.bandHeight} style={{ background: theme.lime }} />
      <SpotCard spot={spot} />
      {footer && (
        <Placed x={0} y={892} width={480} className="text-center text-[19px] leading-[26px]" style={{ color: theme.footer }}>
          {footer}
        </Placed>
      )}
    </Panel>
  )
}
