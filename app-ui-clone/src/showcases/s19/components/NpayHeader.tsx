import { Bell, Menu } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'

/** Top app bar: Npay mark (placeholder), 결제내역 outline button, bell with badge and menu. */
export function NpayHeader({ top = 71 }: { top?: number }) {
  return (
    <div className="absolute inset-x-0" style={{ top, height: 29 }}>
      <ImagePlaceholder label="Npay logo" tone="#e5e7eb" className="absolute" style={{ left: 23.7, top: 4.3, width: 63, height: 22, borderRadius: 11 }} />
      <span
        className="absolute flex items-center justify-center"
        style={{
          left: 208.4,
          top: 1,
          width: 64,
          height: 27,
          borderRadius: 4,
          border: '1px solid #4a4f55',
          fontSize: 13,
          color: '#d8d8d8',
          letterSpacing: -0.4,
        }}
      >
        결제내역
      </span>
      <span className="absolute" style={{ left: 299, top: 1 }}>
        <Bell size={22} strokeWidth={1.5} fill="#fff" color="#fff" />
        <span className="absolute rounded-full" style={{ right: -3, top: -1.5, width: 5, height: 5, background: '#ff3b30' }} />
      </span>
      <Menu size={24} strokeWidth={1.8} color="#fff" className="absolute" style={{ left: 345.5, top: 2.5 }} />
    </div>
  )
}
