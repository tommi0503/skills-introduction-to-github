import { Divider, Panel, Placed } from '../../../ui'
import { ContactBand } from '../../shared-3435/components/ContactBand'
import { PanelTitle } from '../../shared-3435/components/PanelTitle'
import { clinic } from '../../shared-3435/data'
import { larana } from '../../shared-3435/theme'
import { DoctorCard } from '../components/DoctorCard'
import { doctors, greeting } from '../data'

/** Left outside panel: greeting, doctor introductions and the phone band. */
export function GreetingPanel() {
  return (
    <Panel background={larana.paper} style={{ color: larana.inkSoft }}>
      <Placed x={0} y={52} width={498}>
        <PanelTitle>{greeting.title}</PanelTitle>
      </Placed>
      <Placed x={66} y={124} className="flex flex-col gap-y-[27px] text-[17.4px] font-medium leading-[27px]">
        {greeting.paragraphs.map((p) => (
          <p key={p} className="m-0 whitespace-pre-line">
            {p}
          </p>
        ))}
      </Placed>
      <Placed x={48} y={332} width={404}>
        <Divider color={larana.line} thickness={1.5} />
      </Placed>
      <Placed x={0} y={378} width={498}>
        <PanelTitle>{doctors.title}</PanelTitle>
      </Placed>
      <Placed x={66} y={452} className="flex flex-col gap-y-[22px]">
        {doctors.list.map((d) => (
          <DoctorCard key={d.name} doctor={d} />
        ))}
      </Placed>
      <ContactBand name={clinic.name} phone={clinic.phone} height={60} />
    </Panel>
  )
}
