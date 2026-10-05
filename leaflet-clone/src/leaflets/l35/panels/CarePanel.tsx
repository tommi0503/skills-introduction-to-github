import { Panel, Placed } from '../../../ui'
import { ContactBand } from '../../shared-3435/components/ContactBand'
import { PanelTitle } from '../../shared-3435/components/PanelTitle'
import { clinic } from '../../shared-3435/data'
import { larana } from '../../shared-3435/theme'
import { CheckList } from '../components/CheckList'
import { ServiceCard } from '../components/ServiceCard'
import { SubHeading } from '../components/SubHeading'
import { care } from '../data'

/** Inside left panel: care service cards, symptom checklist, phone band. */
export function CarePanel() {
  return (
    <Panel background={larana.paper}>
      <Placed x={0} y={50} width={476}>
        <PanelTitle>{care.title}</PanelTitle>
      </Placed>
      <Placed x={56} y={129} width={365} className="flex flex-col gap-y-[22px]">
        {care.services.map((s) => (
          <ServiceCard key={s.title} service={s} />
        ))}
      </Placed>
      <Placed x={65} y={665}>
        <SubHeading>{care.symptomsTitle}</SubHeading>
        <CheckList
          items={care.symptoms}
          className="mt-[28px] gap-y-[19px] text-[17px] font-medium leading-[24px]"
          style={{ color: larana.inkSoft }}
        />
      </Placed>
      <ContactBand name={clinic.name} phone={clinic.phone} height={63} />
    </Panel>
  )
}
