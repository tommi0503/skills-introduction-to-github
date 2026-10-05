import type { Transaction } from '../data'
import { FlagPair } from './FlagPair'

export function TransactionRow({ tx }: { tx: Transaction }) {
  return (
    <div className="flex h-[76px] items-center px-[17px] text-white">
      <FlagPair />
      <div className="ml-[18px] flex-1">
        <div className="text-[14px] leading-[18px] font-medium">{tx.title}</div>
        <div className="mt-[4px] text-[12.5px] text-white/55">{tx.time}</div>
      </div>
      <div className="text-right">
        <div className="text-[14px] leading-[18px] font-medium">{tx.primary}</div>
        <div className="mt-[4px] text-[12.5px] text-white/55">{tx.secondary}</div>
      </div>
    </div>
  )
}
