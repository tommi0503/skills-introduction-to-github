import { ArrowLeft, ArrowRight } from 'lucide-react'
import { IconButton } from '../../../ui'
import type { portfolio } from '../data'

/** Paged transaction preview: prev / details / next. */
export function TransactionRow({ tx }: { tx: typeof portfolio.transaction }) {
  return (
    <div className="flex items-center gap-[19px]">
      <IconButton icon={ArrowLeft} size={54} iconSize={20} strokeWidth={2} className="bg-[#efeff0]" />
      <div className="flex-1">
        <div className="flex justify-between text-[14px] font-semibold leading-[18px]">
          <span>{tx.merchant}</span>
          <span>{tx.amount}</span>
        </div>
        <div className="mt-[4px] flex justify-between text-[11.5px] leading-[15px] text-[#8a8a8f]">
          <span>{tx.kind}</span>
          <span>{tx.date}</span>
        </div>
      </div>
      <IconButton icon={ArrowRight} size={54} iconSize={20} strokeWidth={2} className="ml-[1px] bg-[#efeff0]" />
    </div>
  )
}
