import { library } from '../../shared-2425/theme'
import { FramedPill } from '../../shared-2425/components/FramedPill'
import type { ProgramItem } from '../data'

interface ProgramRowProps {
  item: ProgramItem
  pillW: number
  pillH: number
  /** x of the description relative to the row. */
  descX: number
}

/** Yellow rounded-box label + two-line description. */
export function ProgramRow({ item, pillW, pillH, descX }: ProgramRowProps) {
  return (
    <div className="relative flex items-center" style={{ height: pillH }}>
      <FramedPill fill={library.yellow} width={pillW} height={pillH} radius={11} className="font-dohyeon text-[16px]" style={{ color: library.title }}>
        {item.label}
      </FramedPill>
      <div className="absolute text-[13px] font-semibold leading-[20px] tracking-[0.01em]" style={{ left: descX, color: '#4b4f72' }}>
        {item.desc.map((d) => (
          <p key={d} className="m-0 whitespace-nowrap">
            {d}
          </p>
        ))}
      </div>
    </div>
  )
}
