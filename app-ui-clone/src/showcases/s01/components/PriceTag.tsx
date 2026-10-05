import { cn } from '../../../ui'

interface PriceTagProps {
  price: string
  unit?: string
  className?: string
  unitClassName?: string
}

/** "$21.70 /day" price with a lighter unit suffix. */
export function PriceTag({ price, unit = '/day', className, unitClassName }: PriceTagProps) {
  return (
    <div className={cn('flex items-baseline gap-[4px]', className)}>
      <span>{price}</span>
      <span className={cn('font-normal', unitClassName)}>{unit}</span>
    </div>
  )
}
