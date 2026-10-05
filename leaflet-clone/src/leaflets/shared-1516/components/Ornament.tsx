import { ImagePlaceholder } from '../../../ui'

export interface OrnamentProps {
  /** Total width and the width of the central flourish (artwork → placeholder). */
  width: number
  flourishWidth: number
  flourishHeight: number
  lineColor: string
  className?: string
}

/** Horizontal rule with a decorative flourish in the middle. */
export function Ornament({ width, flourishWidth, flourishHeight, lineColor, className }: OrnamentProps) {
  return (
    <div className={className} style={{ width, height: flourishHeight, display: 'flex', alignItems: 'center' }}>
      <div className="flex-1" style={{ height: 2, background: lineColor }} />
      <ImagePlaceholder style={{ width: flourishWidth, height: flourishHeight, borderRadius: flourishHeight / 2 }} tone="#c9ccd1" label="flourish" />
      <div className="flex-1" style={{ height: 2, background: lineColor }} />
    </div>
  )
}
