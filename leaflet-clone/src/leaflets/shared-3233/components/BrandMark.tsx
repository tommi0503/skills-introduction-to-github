import { ImagePlaceholder } from '../../../ui'

export interface BrandMarkProps {
  /** Outer size of the (rotated) mark in px. */
  size: number
  tone?: string
}

/** The diamond logo symbol — a logo, so it stays a flat placeholder in the diamond silhouette. */
export function BrandMark({ size, tone }: BrandMarkProps) {
  return (
    <ImagePlaceholder
      label="휴텍 미디어 로고"
      tone={tone}
      style={{ width: size, height: size, clipPath: 'polygon(50% 0, 100% 50%, 50% 100%, 0 50%)' }}
    />
  )
}
