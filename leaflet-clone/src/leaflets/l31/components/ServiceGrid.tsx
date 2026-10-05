import { Placed } from '../../../ui'
import { growth } from '../../shared-3031/theme'
import { serviceGrid } from '../data'
import { ServiceItemView } from './ServiceItemView'

/** Translucent card spanning panels 2–3 with a 2×3 grid of services (column-major order). */
export function ServiceGrid() {
  const { card, columns, rows, circle, textOffset, items } = serviceGrid
  return (
    <>
      <Placed x={card.x} y={card.y} width={card.w} height={card.h} className="rounded-[16px]" style={{ background: growth.card }} />
      {items.map((item, i) => (
        <Placed key={item.key} x={columns[Math.floor(i / rows.length)]} y={rows[i % rows.length]} style={{ color: growth.muted }}>
          <ServiceItemView item={item} circle={circle} textOffset={textOffset} />
        </Placed>
      ))}
    </>
  )
}
