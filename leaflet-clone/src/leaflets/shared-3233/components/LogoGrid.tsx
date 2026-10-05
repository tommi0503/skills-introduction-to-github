import { ImagePlaceholder, cn } from '../../../ui'

export interface LogoGridProps {
  count: number
  columns: number
  logoWidth: number
  logoHeight: number
  columnGap: number
  rowGap: number
  className?: string
}

/** Grid of partner logos — logos are artwork, so each is a flat placeholder of the logo's footprint. */
export function LogoGrid({ count, columns, logoWidth, logoHeight, columnGap, rowGap, className }: LogoGridProps) {
  return (
    <div
      className={cn('grid', className)}
      style={{ gridTemplateColumns: `repeat(${columns}, ${logoWidth}px)`, columnGap, rowGap }}
    >
      {Array.from({ length: count }, (_, i) => (
        <ImagePlaceholder key={i} label="partner logo" style={{ width: logoWidth, height: logoHeight }} />
      ))}
    </div>
  )
}
