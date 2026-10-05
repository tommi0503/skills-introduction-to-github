import { Panel, Placed } from '../../../ui'
import { seoul } from '../../shared-2627/theme'
import { Photo } from '../../shared-2627/components/Photo'
import { SectionNumber } from '../../shared-2627/components/SectionNumber'
import { TextCard } from '../../shared-2627/components/TextCard'
import { tips } from '../data'

/** Panel 1 — 04 서울 여행자를 위한 안내서. */
export function TipsPanel() {
  return (
    <Panel background={seoul.paper}>
      <Placed x={28} y={86}>
        <SectionNumber number={tips.number} title={tips.title} layout="inline" />
      </Placed>
      {tips.items.map((t) => (
        <TextCard key={t.y} lines={t.lines} className="flex flex-col justify-center" style={{ left: 27, top: t.y, width: 428, height: t.h }} />
      ))}
      <Photo box={tips.photo} />
    </Panel>
  )
}
