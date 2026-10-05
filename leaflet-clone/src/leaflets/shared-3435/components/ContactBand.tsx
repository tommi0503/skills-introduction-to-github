import { cn } from '../../../ui'
import { larana } from '../theme'

export interface ContactBandProps {
  name: string
  phone: string
  height?: number
  className?: string
}

/** Solid blue footer band with the clinic name and phone number. */
export function ContactBand({ name, phone, height = 60, className }: ContactBandProps) {
  return (
    <div
      className={cn('absolute right-0 bottom-0 left-0 flex items-center justify-center gap-[14px] text-[21px] font-medium', className)}
      style={{ height, background: larana.band, color: larana.onBand }}
    >
      <span>{name}</span>
      <span className="tracking-[0.02em]">{phone}</span>
    </div>
  )
}
