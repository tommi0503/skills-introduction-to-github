import { ImagePlaceholder, KeyValueList, Panel, Placed } from '../../../ui'
import { birds, contacts, message } from '../data'
import { CtaCircle } from '../components/CtaCircle'

const birdShape = 'polygon(0% 55%, 25% 50%, 40% 0%, 55% 45%, 85% 0%, 75% 60%, 100% 65%, 60% 100%, 30% 90%)'

/** Panel 2 — message, QR call-to-action and contact details. */
export function MessagePanel() {
  return (
    <Panel>
      {birds.map((b, i) => (
        <Placed key={i} x={b.x} y={b.y} width={b.w} height={b.h}>
          <ImagePlaceholder label="bird illustration" className="h-full w-full" style={{ clipPath: birdShape }} />
        </Placed>
      ))}
      <Placed x={0} y={95} width={456} className="flex flex-col items-center gap-[51px] text-center">
        {message.paragraphs.map((p) => (
          <p key={p[0]} className="m-0 text-[30px] font-normal leading-[49px] tracking-[-0.04em] text-[#1d1d1d]">
            {p.map((l) => (
              <span key={l} className="block">{l}</span>
            ))}
          </p>
        ))}
      </Placed>
      <Placed x={93} y={427}>
        <CtaCircle label={message.cta} size={279} qrSize={112} />
      </Placed>
      <Placed x={60} y={818} width={400}>
        <KeyValueList
          items={contacts}
          labelWidth={86}
          className="gap-[14px]"
          rowClassName="text-[17.5px] leading-[22px] text-[#1d1d1d]"
          labelClassName="font-bold"
          valueClassName="font-normal tracking-[-0.01em]"
        />
      </Placed>
    </Panel>
  )
}
