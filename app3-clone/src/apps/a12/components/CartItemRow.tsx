import { Ellipsis } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { CartItem } from '../data'
import { theme } from '../theme'
import { QuantityStepper } from './QuantityStepper'

export function CartItemRow({ item }: { item: CartItem }) {
  return (
    <div className="flex h-[112px] gap-[16px]">
      <ImagePlaceholder className="h-[112px] w-[111px] rounded-[6px]" label={item.title} />
      <div className="relative flex-1">
        <div className="flex items-start justify-between pt-[1px]">
          <p className="text-[13.5px] leading-[18px] font-medium tracking-[-0.1px] text-[#111]">{item.title}</p>
          <p className="text-[13.5px] leading-[18px] tracking-[-0.1px]" style={{ color: theme.price }}>
            {item.price}
          </p>
        </div>
        <p className="mt-[2px] text-[13.5px] leading-[18px]" style={{ color: theme.variant }}>
          {item.variant}
        </p>
        <div className="absolute inset-x-0 bottom-0 flex items-end justify-between">
          <QuantityStepper quantity={item.quantity} />
          <div className="flex h-[32px] w-[32px] items-center justify-center rounded-[7px]" style={{ background: theme.field }}>
            <Ellipsis size={18} strokeWidth={2.2} className="text-[#111]" />
          </div>
        </div>
      </div>
    </div>
  )
}
