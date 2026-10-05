import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { HandLine } from '../components/HandLine'
import { PillHeading } from '../components/PillHeading'
import { transit } from '../data'
import { theme } from '../theme'

const CONTACT = { top: 775, pitch: 44, height: 33 }

/** Inside-middle on crumpled paper: transit tabs + contact boxes. */
export function TransitPanel() {
  return (
    <Panel style={{ color: theme.ink }}>
      <ImagePlaceholder label="crumpled paper texture" className="absolute inset-0" />
      <PillHeading x={107} y={92} width={271}>
        {transit.heading}
      </PillHeading>
      {transit.routes.map((r) => (
        <div key={r.label}>
          <Placed
            x={0}
            y={r.y}
            width={196}
            height={38}
            className="flex items-center rounded-r-full border-y-2 border-r-2 pl-[32px] font-gaegu text-[16px] font-bold tracking-[0.1em]"
            style={{ background: '#f1efec', borderColor: '#c3c3be' }}
          >
            {r.label}
          </Placed>
          <Placed x={50} y={r.y + 50} className="font-gaegu text-[16px] font-bold tracking-[0.06em]">
            {r.lines.map((l) => (
              <HandLine key={l} className="leading-[31px]">
                {l}
              </HandLine>
            ))}
          </Placed>
        </div>
      ))}
      <Placed x={0} y={731} width={490} className="text-center text-[11.5px] leading-[20px]" style={{ color: theme.muted }}>
        {transit.contactCaption}
      </Placed>
      {transit.contacts.map((c, i) => (
        <Placed key={i} x={30} y={CONTACT.top + i * CONTACT.pitch} height={CONTACT.height} className="flex gap-[7px] text-[12.5px]" style={{ color: theme.muted }}>
          {[
            { text: c.name, width: 105 },
            { text: c.info, width: 312 },
          ].map((cell) => (
            <div
              key={cell.width}
              className="flex h-full items-center justify-center border-2"
              style={{ width: cell.width, borderColor: theme.boxBorder, background: theme.boxFill }}
            >
              {cell.text}
            </div>
          ))}
        </Placed>
      ))}
    </Panel>
  )
}
