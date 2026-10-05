import { Panel, Placed } from '../../../ui'
import { seoul } from '../../shared-2627/theme'
import { Photo } from '../../shared-2627/components/Photo'
import { SectionNumber } from '../../shared-2627/components/SectionNumber'
import { Paragraphs } from '../components/Paragraphs'
import { tradition } from '../data'

/** Panel 2 — 02 햇살 아래 빛나는 서울의 전통. */
export function TraditionPanel() {
  return (
    <Panel background={seoul.paper}>
      <Placed x={0} y={88} width={486}>
        <SectionNumber number={tradition.number} title={tradition.title} layout="stacked" align="center" className="gap-[34px]" />
      </Placed>
      <Paragraphs items={tradition.texts} />
      {tradition.photos.map((p) => (
        <Photo key={p.label} box={p} />
      ))}
    </Panel>
  )
}
