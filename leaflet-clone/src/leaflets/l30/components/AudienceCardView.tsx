import { Placed } from '../../../ui'
import { ArtworkLayer } from '../../shared-3031/components/ArtworkLayer'
import { growth } from '../../shared-3031/theme'
import type { AudienceCard } from '../data'

/** White card with heading + description, overlapped by a character illustration. */
export function AudienceCardView({ card }: { card: AudienceCard }) {
  const { box, text } = card
  return (
    <>
      <Placed x={box.x} y={box.y} width={box.w} height={box.h} className="rounded-[12px]" style={{ background: growth.card }} />
      <ArtworkLayer items={[card.figure]} />
      <Placed x={text.x} y={text.y}>
        <h3 className="m-0 text-[19px] font-bold leading-[26px] tracking-[0px]" style={{ color: growth.ink }}>
          {card.heading.map((l) => (
            <span key={l} className="block whitespace-nowrap">
              {l}
            </span>
          ))}
        </h3>
        <div className="mt-[11px] text-[15px] leading-[20.6px] tracking-[0.2px]" style={{ color: growth.muted }}>
          {card.body.map((l) => (
            <p key={l} className="m-0 whitespace-nowrap">
              {l}
            </p>
          ))}
        </div>
      </Placed>
    </>
  )
}
