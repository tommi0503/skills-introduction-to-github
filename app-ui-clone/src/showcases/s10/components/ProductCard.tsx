import { Heart } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { Product } from '../data'

/** Geometry of a product card; lets the same card render big (home) or small (onboarding). */
export interface ProductCardMetrics {
  width: number
  height: number
  pad: number
  radius: number
  innerRadius: number
  imageHeight: number
  titleSize: number
  titleLeading: number
  /** Title position inside the image card. */
  titleInset: { x: number; y: number }
  heartSize: number
  heartInset: number
  priceLabelSize: number
  priceSize: number
  priceBottom: number
  button: { width: number; height: number; fontSize: number; right: number; bottom: number }
  /** Product photo box inside the image area (relative to the inner card). */
  photo: { left: number; top: number; width: number; height: number; radius?: number }
}

export interface ProductCardProps {
  product: Product
  metrics: ProductCardMetrics
  /** Colours of the decorative layers peeking out below the card. */
  stack?: { color: string; offset: number; inset: number }[]
  className?: string
}

export function ProductCard({ product, metrics: m, stack = [], className }: ProductCardProps) {
  return (
    <div className={cn('relative', className)} style={{ width: m.width, height: m.height }}>
      {[...stack].reverse().map((layer) => (
        <div
          key={layer.offset}
          className="absolute"
          style={{
            left: layer.inset,
            right: layer.inset,
            top: layer.offset,
            height: m.height,
            borderRadius: m.radius,
            background: layer.color,
          }}
        />
      ))}
      <div className="absolute inset-0" style={{ borderRadius: m.radius, background: product.frame }} />
      <div
        className="absolute overflow-hidden"
        style={{
          left: m.pad,
          right: m.pad,
          top: m.pad,
          height: m.imageHeight,
          borderRadius: m.innerRadius,
          background: product.tone,
        }}
      >
        <ImagePlaceholder
          label="snack bag"
          className="absolute"
          style={{ ...m.photo, borderRadius: m.photo.radius ?? 0 }}
        />
        <div
          className="absolute font-bold tracking-[-0.01em]"
          style={{ left: m.titleInset.x, top: m.titleInset.y, fontSize: m.titleSize, lineHeight: `${m.titleLeading}px` }}
        >
          {product.title.map((line) => (
            <div key={line}>{line}</div>
          ))}
        </div>
        <div
          className="absolute flex items-center justify-center rounded-full"
          style={{
            width: m.heartSize,
            height: m.heartSize,
            right: m.heartInset,
            top: m.heartInset,
            background: product.heartBg,
          }}
        >
          <Heart size={m.heartSize * 0.48} fill="currentColor" strokeWidth={1.5} />
        </div>
      </div>
      <div className="absolute" style={{ left: m.pad + 2, bottom: m.priceBottom }}>
        <div className="text-[#777]" style={{ fontSize: m.priceLabelSize, lineHeight: 1.3, marginBottom: m.priceLabelSize * 0.3 }}>
          Price
        </div>
        <div className="font-bold" style={{ fontSize: m.priceSize, lineHeight: 1.25 }}>
          {product.price}
        </div>
      </div>
      <button
        type="button"
        className="absolute rounded-full bg-black font-semibold text-white"
        style={{
          width: m.button.width,
          height: m.button.height,
          right: m.button.right,
          bottom: m.button.bottom,
          fontSize: m.button.fontSize,
        }}
      >
        Add To Cart
      </button>
    </div>
  )
}
