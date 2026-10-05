import { Check } from 'lucide-react'
import type { DayStatus } from '../data'

const fills: Record<DayStatus, string> = {
  done: 'bg-[#18171c] text-white',
  missed: 'bg-[#e6e6e9]',
  upcoming: 'bg-[#e6e6e9]',
  today: 'bg-white ring-[1.5px] ring-inset ring-[#18171c]',
}

/** 29pt day circle; completed days carry a check mark. */
export function DayDot({ status }: { status: DayStatus }) {
  return (
    <span className={`flex h-[29px] w-[29px] items-center justify-center rounded-full ${fills[status]}`}>
      {status === 'done' && <Check size={13} strokeWidth={3.2} />}
    </span>
  )
}
