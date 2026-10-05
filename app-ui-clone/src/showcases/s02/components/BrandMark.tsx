import { ImagePlaceholder } from '../../../ui'

/** App logo: black disc holding the brand glyph (glyph itself is a placeholder). */
export function BrandMark({ size = 46 }: { size?: number }) {
  return (
    <div className="flex items-center justify-center rounded-full bg-[#1d1d1d]" style={{ width: size, height: size }}>
      <ImagePlaceholder className="rounded-[3px]" style={{ width: size * 0.44, height: size * 0.4 }} label="Travio logo" />
    </div>
  )
}
