import { Panel, Placed } from '../../../ui'
import { growth } from '../../shared-3031/theme'
import { contact } from '../data'

/** Panel 2 — back cover with the support centre contact. */
export function ContactPanel() {
  return (
    <Panel background={growth.navyPanel}>
      <Placed x={0} y={829} width={490} className="text-center text-white">
        <p className="m-0 text-[17px] font-bold leading-[26px]">{contact.heading}</p>
        <div className="mt-[11px] text-[14.5px] leading-[22.5px]">
          {contact.lines.map((l) => (
            <p key={l} className="m-0">
              {l}
            </p>
          ))}
        </div>
      </Placed>
    </Panel>
  )
}
