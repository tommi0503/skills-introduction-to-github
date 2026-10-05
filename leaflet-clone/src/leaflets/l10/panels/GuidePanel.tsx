import { Panel, Placed } from '../../../ui'
import { GuideSection } from '../components/GuideSection'
import { guide } from '../data'

export function GuidePanel() {
  return (
    <Panel>
      <Placed x={46} y={158} className="flex flex-col gap-[29px]">
        {guide.map((s) => (
          <GuideSection key={s.title} section={s} />
        ))}
      </Placed>
    </Panel>
  )
}
