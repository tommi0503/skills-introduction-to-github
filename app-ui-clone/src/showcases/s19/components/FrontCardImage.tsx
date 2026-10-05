import { ImagePlaceholder } from '../../../ui'

/** Front card image (placeholder) with the black "signature + last digits" tag. */
export function FrontCardImage({ digits, style }: { digits: string; style?: React.CSSProperties }) {
  return (
    <div className="absolute" style={{ height: 192, ...style }}>
      <ImagePlaceholder label="credit card" tone="#d4d6db" className="h-full w-full" style={{ borderRadius: 13 }} />
      <div
        className="absolute flex items-center"
        style={{ left: 183.7, top: 143, width: 103, height: 32, borderRadius: 6, background: '#0d0d0f' }}
      >
        <ImagePlaceholder label="signature" tone="#5a5b5f" style={{ marginLeft: 12, width: 30, height: 18, borderRadius: 3 }} />
        <span style={{ marginLeft: 15, color: '#fff', fontSize: 16, fontWeight: 600, letterSpacing: 0 }}>{digits}</span>
      </div>
    </div>
  )
}
