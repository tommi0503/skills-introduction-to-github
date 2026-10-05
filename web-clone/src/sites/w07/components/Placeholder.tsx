import { ImagePlaceholder } from '../../../ui'
import type { Rect } from '../data'

/** Absolutely positioned ImagePlaceholder for a measured media rect. */
export function PlacedImage({ rect, label, tone }: { rect: Rect; label: string; tone?: string }) {
  return (
    <ImagePlaceholder
      label={label}
      tone={tone}
      className="absolute"
      style={{ left: rect.x, top: rect.y, width: rect.w, height: rect.h, borderRadius: rect.radius }}
    />
  )
}
