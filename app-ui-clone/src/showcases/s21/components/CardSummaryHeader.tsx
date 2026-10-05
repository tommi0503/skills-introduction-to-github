import { ImagePlaceholder } from '../../../ui'

export interface CardSummaryHeaderProps {
  issuer: string
  name: string
}

/** Issuer caption, card product name and a small vertical card image. */
export function CardSummaryHeader({ issuer, name }: CardSummaryHeaderProps) {
  return (
    <div className="relative" style={{ height: 70, padding: '0 20px' }}>
      <div style={{ fontSize: 15.5, lineHeight: '18px', color: '#7b7b7b', letterSpacing: -0.3, paddingTop: 4 }}>{issuer}</div>
      <div
        style={{ fontSize: 24, lineHeight: '28px', fontWeight: 700, color: '#151419', letterSpacing: -0.65, marginTop: 1 }}
      >
        {name}
      </div>
      <ImagePlaceholder label="card image" className="absolute" style={{ right: 20.5, top: 0, width: 33, height: 54, borderRadius: 2 }} />
    </div>
  )
}
