import { Placed } from '../../../ui'
import { ArtworkLayer } from '../../shared-2829/components/ArtworkLayer'
import { MapPin } from '../../shared-2829/components/MapPin'
import { NumberDot } from '../../shared-2829/components/NumberDot'
import { autumn } from '../../shared-2829/theme'
import { areaMap } from '../data'

const PIN = 46

/** Festival area map spanning panels 2–3: white card, artwork zones, pins and legend card. */
export function AreaMap() {
  const { card, legendCard, zones, pins, legend } = areaMap
  return (
    <>
      <Placed x={card.x} y={card.y} width={card.w} height={card.h} className="rounded-[26px]" style={{ background: autumn.card }} />
      <ArtworkLayer items={zones} />
      {pins.map((p, i) => (
        <Placed key={i} x={p.cx - PIN / 2} y={p.cy - PIN / 2 - 2}>
          <MapPin color={autumn.pin[p.color]} size={PIN} />
        </Placed>
      ))}
      <Placed x={legendCard.x} y={legendCard.y} width={legendCard.w} height={legendCard.h} className="rounded-[20px]" style={{ background: autumn.card }} />
      {legend.map((e, i) => (
        <Placed key={i} x={e.x - 7.5} y={e.y - 10} className="flex h-[20px] items-center gap-[9px]">
          <NumberDot label={e.number} color={e.primary ? autumn.legendRed : autumn.legendOrange} />
          <span
            className={e.primary ? 'text-[13px] font-bold tracking-[-0.5px]' : 'text-[14.5px] font-bold tracking-[0.3px]'}
            style={{ color: autumn.legendText }}
          >
            {e.label}
          </span>
        </Placed>
      ))}
    </>
  )
}
