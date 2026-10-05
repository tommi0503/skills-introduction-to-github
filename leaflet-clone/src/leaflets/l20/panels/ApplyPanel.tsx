import { Divider, Panel, Placed } from '../../../ui'
import { CardSheet } from '../../shared-2021/components/CardSheet'
import { CenteredRow } from '../../shared-2021/components/CenteredRow'
import { HeadPill } from '../../shared-2021/components/HeadPill'
import { applyPanel, cards } from '../data'
import { MethodBlock } from '../components/MethodBlock'

const METHOD_TOPS = [140, 335, 543]
const DIVIDER_TOPS = [300, 508, 790]

export function ApplyPanel() {
  return (
    <Panel>
      <CardSheet insets={cards[0]} />
      <CenteredRow top={78}>
        <HeadPill className="h-[27px] w-[150px] text-[21px]">{applyPanel.heading}</HeadPill>
      </CenteredRow>
      {applyPanel.methods.map((m, i) => (
        <Placed key={m.id} x={30} y={METHOD_TOPS[i]} width={421}>
          <MethodBlock method={m} />
        </Placed>
      ))}
      {DIVIDER_TOPS.map((t) => (
        <Placed key={t} x={80} y={t} width={318}>
          <Divider color="#dcdfe3" thickness={2} />
        </Placed>
      ))}
      <CenteredRow top={830}>
        <HeadPill className="h-[28px] w-[150px] text-[21px]">{applyPanel.prepHeading}</HeadPill>
      </CenteredRow>
      <CenteredRow top={884} centerX={238}>
        <span className="text-[23px] font-bold tracking-[-0.02em] text-[#d9768a]">{applyPanel.prepNote}</span>
      </CenteredRow>
    </Panel>
  )
}
