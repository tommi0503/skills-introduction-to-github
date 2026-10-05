import { cn } from '../../../ui'

export interface BigAmountProps {
  value: string
  currency?: string
  className?: string
}

/** Hero balance: small grey currency sign + oversized figure. */
export function BigAmount({ value, currency = '$', className }: BigAmountProps) {
  return (
    <div className={cn('flex items-baseline justify-center', className)}>
      <span className="mr-[4px] translate-y-[6px] text-[42px] font-light text-[#77777c]">{currency}</span>
      <span className="text-[76px] font-medium leading-none tracking-[-3.5px]">{value}</span>
    </div>
  )
}
