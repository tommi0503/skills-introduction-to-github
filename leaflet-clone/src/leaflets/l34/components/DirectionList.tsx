import { larana } from '../../shared-3435/theme'
import type { DirectionItem } from '../data'

export interface DirectionListProps {
  items: DirectionItem[]
  className?: string
}

/** Small blue caption over a value, repeated (주소 / 지하철 / 버스 / 주차). */
export function DirectionList({ items, className }: DirectionListProps) {
  return (
    <dl className={`m-0 flex flex-col gap-y-[24px] ${className ?? ''}`}>
      {items.map((it) => (
        <div key={it.label}>
          <dt className="text-[12px] font-bold leading-[16px]" style={{ color: larana.label }}>
            {it.label}
          </dt>
          <dd className="m-0 mt-[5px] text-[16.9px] font-medium leading-[25px]" style={{ color: larana.ink }}>
            {it.value}
          </dd>
        </div>
      ))}
    </dl>
  )
}
