import { ScanQrCode } from 'lucide-react'
import { cn } from '../../../ui'

export interface QrIconBoxProps {
  size: number
  className?: string
}

/** Rounded outlined square holding a "scan QR" glyph (an icon, not a real code). */
export function QrIconBox({ size, className }: QrIconBoxProps) {
  return (
    <span
      className={cn('inline-flex items-center justify-center rounded-[9px] border-[3px] border-[#4677ae] bg-white text-[#6f8fb3]', className)}
      style={{ width: size, height: size }}
    >
      <ScanQrCode size={size * 0.72} strokeWidth={1.7} />
    </span>
  )
}
