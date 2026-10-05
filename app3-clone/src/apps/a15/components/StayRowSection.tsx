import { ChevronRight } from 'lucide-react'
import type { StayRow } from '../data'
import { palette as c } from '../theme'
import { StayCard } from './StayCard'

export function StayRowSection({ row }: { row: StayRow }) {
  return (
    <section>
      <h2 className="flex items-center gap-[3px] px-[24px] text-[17px] font-semibold tracking-[-0.2px]" style={{ color: c.text }}>
        {row.title}
        <ChevronRight size={15} strokeWidth={2.6} />
      </h2>
      <div className="mt-[12px] flex gap-[12px] px-[24px]">
        {row.stays.map((s) => (
          <StayCard key={s.id} stay={s} />
        ))}
      </div>
    </section>
  )
}
