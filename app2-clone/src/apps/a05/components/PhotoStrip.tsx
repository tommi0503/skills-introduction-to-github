import { ImagePlaceholder, cn } from '../../../ui'

/** Horizontal row of photos that bleeds off the right edge. */
export function PhotoStrip({ widths, height, gap = 5, className, radius = 4 }: { widths: number[]; height: number; gap?: number; className?: string; radius?: number }) {
  return (
    <div className={cn('flex', className)} style={{ gap }}>
      {widths.map((w, i) => (
        <ImagePlaceholder key={i} label="place photo" style={{ width: w, height, borderRadius: radius }} />
      ))}
    </div>
  )
}
