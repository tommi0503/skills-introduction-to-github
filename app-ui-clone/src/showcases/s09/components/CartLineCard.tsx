import { ImagePlaceholder } from '../../../ui'
import type { CartLine } from '../data'
import { theme } from '../theme'
import { Stepper } from './Stepper'

/** Cart row: dish photo, name, quantity and price. */
export function CartLineCard({ line }: { line: CartLine }) {
  return (
    <div className="relative h-[116px] rounded-[16px] bg-white">
      <ImagePlaceholder label={line.key} className="absolute top-[14px] left-[14px] h-[88px] w-[88px] rounded-full" />
      <div className="absolute top-[13px] left-[126px] font-poppins text-[14.5px] leading-[20px] font-medium" style={{ color: theme.ink }}>
        {line.name}
      </div>
      <div className="absolute bottom-[14px] left-[126px] h-[34px] w-[100px]">
        <Stepper value={1} />
      </div>
      <div className="absolute right-[20px] bottom-[19px] font-poppins text-[17px] font-semibold" style={{ color: theme.ink }}>
        {line.price}
      </div>
    </div>
  )
}
