import type { ReactNode } from 'react'
import { ChevronRight, X } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { CartItem } from '../data'
import { CheckDot, Stepper } from './Primitives'

export interface CartItemRowProps {
  item: CartItem
}

/** One selectable product row: check · thumbnail · name/stock · remove, then stepper + price. */
export function CartItemRow({ item }: CartItemRowProps) {
  return (
    <div className="relative pt-[17px] pr-[17px] pl-[14.5px]">
      <div className="flex items-start">
        <CheckDot />
        <div className="ml-[8px] flex h-[77px] w-[77px] items-center justify-center rounded-[12px] border border-[#ededed] bg-white">
          <ImagePlaceholder label={`${item.name} photo`} className="h-[56px] w-[60px] rounded-[8px]" />
        </div>
        <div className="ml-[16px] flex-1 pt-[0px]">
          <p className="text-[16.5px] leading-[20px] text-[#222]">{item.name}</p>
          <p className="mt-[7px] text-[12.5px] font-semibold text-[#222]">{item.stock}</p>
        </div>
        <X size={20} strokeWidth={1.4} className="mt-[0px] text-[#444]" />
      </div>
      <div className="mt-[8px] ml-[28px] flex items-center justify-between">
        <Stepper value={item.qty} />
        <p className="flex items-baseline gap-[6px]">
          {item.listPrice && <span className="text-[14px] text-[#b5b5b5] line-through">{item.listPrice}</span>}
          <span className="text-[18px] font-bold text-[#1a1a1a]">{item.price}</span>
        </p>
      </div>
    </div>
  )
}

export function GiftSummary({ caption, order, keep }: { caption: string; order: number; keep: number }) {
  const num = (n: number): ReactNode => <span className="font-semibold text-[#5fd34b]">{n}</span>
  return (
    <div className="mx-[18px] mt-[15px] flex items-center justify-between border-t border-[#f0f0f0] pt-[14px] pb-[14px] text-[13px] text-[#666]">
      <span>{caption}</span>
      <span className="flex items-center gap-[3px]">
        주문 {num(order)} · 키핑 {num(keep)}
        <ChevronRight size={15} strokeWidth={1.8} className="text-[#333]" />
      </span>
    </div>
  )
}
