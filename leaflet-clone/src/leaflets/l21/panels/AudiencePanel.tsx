import { Panel, Placed } from '../../../ui'
import { CardSheet } from '../../shared-2021/components/CardSheet'
import { CenteredRow } from '../../shared-2021/components/CenteredRow'
import { HeadPill } from '../../shared-2021/components/HeadPill'
import { WishRow } from '../components/WishRow'
import { audiencePanel as a, cards } from '../data'

const WISH_TOP = 143
const WISH_STEP = 171

export function AudiencePanel() {
  return (
    <Panel>
      <CardSheet insets={cards[1]} />
      <CenteredRow top={68} centerX={243}>
        <HeadPill variant="soft" className="h-[40px] w-[130px] text-[27px]">
          {a.heading}
        </HeadPill>
      </CenteredRow>
      {a.wishes.map((w, i) => (
        <Placed key={w.id} x={80} y={WISH_TOP + i * WISH_STEP}>
          <WishRow wish={w} />
        </Placed>
      ))}
    </Panel>
  )
}
