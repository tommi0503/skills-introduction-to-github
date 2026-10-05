import { Pencil } from 'lucide-react'
import { Placed } from '../../../ui'
import { library } from '../../shared-2425/theme'

export interface TabGeometry {
  x: number
  y: number
  width: number
  height: number
  /** x of the dot that ends the rule. */
  lineEnd: number
}

interface SectionTabProps {
  title: string
  geo: TabGeometry
}

/** Navy folder tab with a pencil, sitting on a rule that ends in a dot. */
export function SectionTab({ title, geo }: SectionTabProps) {
  const { x, y, width, height, lineEnd } = geo
  const lineY = y + height
  return (
    <>
      <Placed x={x} y={lineY - 2} width={lineEnd - x} height={2.5} style={{ background: library.navy }} />
      <Placed x={lineEnd - 6} y={lineY - 7} width={12} height={12} className="rounded-full" style={{ background: library.navy }} />
      <Placed
        x={x}
        y={y}
        width={width}
        height={height}
        className="flex items-center justify-center rounded-t-[12px] font-dohyeon text-[19px] leading-none text-white"
        style={{ background: library.navy, paddingLeft: 22, paddingTop: 2 }}
      >
        {title}
      </Placed>
      <Placed x={x + 8} y={y - 13} className="leading-none" style={{ color: library.ink }}>
        <Pencil size={44} strokeWidth={1.6} fill="#f2cd5c" />
      </Placed>
    </>
  )
}
