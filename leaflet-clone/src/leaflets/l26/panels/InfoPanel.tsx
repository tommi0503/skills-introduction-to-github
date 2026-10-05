import { Panel, Placed } from '../../../ui'
import { seoul } from '../../shared-2627/theme'
import { Photo } from '../../shared-2627/components/Photo'
import { information } from '../data'

/** Panel 2 — quote mark, slogan, INFORMATION photo and contacts. */
export function InfoPanel() {
  return (
    <Panel background={seoul.paper}>
      <Placed x={0} y={120} width={480} className="text-center font-montserrat text-[96px] font-extrabold leading-none" style={{ color: seoul.sky }}>
        ,
      </Placed>
      <Placed x={0} y={221} width={480} className="text-center text-[16.5px] font-semibold leading-[27px] tracking-[-0.02em]" style={{ color: seoul.sky }}>
        {information.quote.map((q) => (
          <p key={q} className="m-0">
            {q}
          </p>
        ))}
      </Placed>
      <Placed x={0} y={385} width={480} className="text-center font-montserrat text-[24px] font-bold leading-none" style={{ color: seoul.slate }}>
        {information.heading}
      </Placed>
      <Photo box={information.photo} />
      <Placed x={0} y={890} width={480} className="text-center text-[14px] font-medium leading-[22px]" style={{ color: seoul.muted }}>
        {information.contacts.map((c) => (
          <p key={c} className="m-0">
            {c}
          </p>
        ))}
      </Placed>
    </Panel>
  )
}
