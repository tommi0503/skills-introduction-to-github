import { Panel, Placed } from '../../../ui'
import { seoul } from '../../shared-2627/theme'
import { Photo } from '../../shared-2627/components/Photo'
import { SectionNumber } from '../../shared-2627/components/SectionNumber'
import { Paragraphs } from '../components/Paragraphs'
import { night } from '../data'

/** Panel 3 — 03 반짝이는 서울의 로맨틱한 밤. */
export function NightPanel() {
  return (
    <Panel background={seoul.paper}>
      {night.photos.map((p) => (
        <Photo key={p.label} box={p} />
      ))}
      <Placed x={33} y={408}>
        <SectionNumber number={night.number} title={night.title} layout="inline" inlineAlign="center" className="gap-[20px]" />
      </Placed>
      <Paragraphs items={night.texts} />
    </Panel>
  )
}
