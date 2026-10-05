import { Panel, Placed } from '../../../ui'
import { PanelTitle } from '../../shared-3435/components/PanelTitle'
import { larana } from '../../shared-3435/theme'
import { FaqList } from '../components/FaqList'
import { NoticeBox } from '../components/NoticeBox'
import { ReserveCard } from '../components/ReserveCard'
import { SubHeading } from '../components/SubHeading'
import { guide } from '../data'

/** Inside right panel: reservation methods grid, first-visit notice, FAQ. */
export function GuidePanel() {
  return (
    <Panel background={larana.paper}>
      <Placed x={0} y={50} width={482}>
        <PanelTitle>{guide.title}</PanelTitle>
      </Placed>
      <Placed x={51} y={132}>
        <SubHeading>{guide.reserveTitle}</SubHeading>
      </Placed>
      <Placed x={51} y={185} width={383} className="grid grid-cols-2 gap-[15px]">
        {guide.methods.map((m) => (
          <ReserveCard key={m.label} method={m} />
        ))}
      </Placed>
      <Placed x={51} y={475} width={383} height={163}>
        <NoticeBox title={guide.notice.title} body={guide.notice.body} className="h-full" />
      </Placed>
      <Placed x={51} y={685}>
        <SubHeading>{guide.faqTitle}</SubHeading>
      </Placed>
      <Placed x={56} y={736} width={380}>
        <FaqList faqs={guide.faqs} />
      </Placed>
    </Panel>
  )
}
