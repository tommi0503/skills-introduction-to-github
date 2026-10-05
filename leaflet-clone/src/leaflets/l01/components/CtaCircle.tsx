import { ImagePlaceholder, cn } from '../../../ui'

interface CtaCircleProps {
  label: string
  size: number
  qrSize: number
  className?: string
}

/** Circular card with a QR code (placeholder) and a call-to-action label. */
export function CtaCircle({ label, size, qrSize, className }: CtaCircleProps) {
  return (
    <div
      className={cn('flex flex-col items-center rounded-full border-2 border-[#1f1f1f] bg-[#f4f4f4]', className)}
      style={{ width: size, height: size }}
    >
      <ImagePlaceholder label="QR code" style={{ width: qrSize, height: qrSize, marginTop: 64 }} />
      <span className="mt-[33px] text-[22px] font-bold leading-none tracking-[0.04em] text-[#1a1a1a]">{label}</span>
    </div>
  )
}
