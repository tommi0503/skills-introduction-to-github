import type { ReactNode } from 'react'
import { RefreshCw } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'

function RoundIcon({ children }: { children: ReactNode }) {
  return (
    <span
      className="flex items-center justify-center rounded-full"
      style={{ width: 21.7, height: 21.7, border: '1px solid #dcdcdc', color: '#555' }}
    >
      {children}
    </span>
  )
}

/** White payment-code card: Npay mark, region switch, help/refresh, QR (placeholder) and the card stack slot. */
export function PayCodeCard({ children }: { children?: ReactNode }) {
  return (
    <div className="relative bg-white" style={{ height: 476.5, borderRadius: 16 }}>
      <ImagePlaceholder label="Npay logo" className="absolute" style={{ left: 19.6, top: 18.5, width: 63, height: 23, borderRadius: 11.5 }} />
      <span className="absolute flex items-center" style={{ left: 89.5, top: 22, height: 15, fontSize: 13.5, color: '#9a9a9a' }}>
        국내
        <span
          style={{
            marginLeft: 5,
            width: 0,
            height: 0,
            borderLeft: '3.8px solid transparent',
            borderRight: '3.8px solid transparent',
            borderTop: '4.6px solid #8a8a8a',
          }}
        />
      </span>
      <span className="absolute flex" style={{ right: 16.5, top: 19.5, gap: 15 }}>
        <RoundIcon>
          <span style={{ fontSize: 14, fontWeight: 600, lineHeight: 1, color: '#666' }}>?</span>
        </RoundIcon>
        <RoundIcon>
          <RefreshCw size={12} strokeWidth={2.4} color="#555" />
        </RoundIcon>
      </span>
      <ImagePlaceholder label="QR / barcode" className="absolute" style={{ left: 88.8, top: 57.8, width: 164, height: 165 }} />
      {children}
    </div>
  )
}
