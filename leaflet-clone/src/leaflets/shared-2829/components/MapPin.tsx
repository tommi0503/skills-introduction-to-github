import { cn } from '../../../ui'

export interface MapPinProps {
  color: string
  label?: string
  /** Width of the pin head in px; the tail adds ~40%. */
  size?: number
  className?: string
}

/** Teardrop location marker with a white disc holding a number. */
export function MapPin({ color, label = '1', size = 46, className }: MapPinProps) {
  const disc = Math.round(size * 0.64)
  return (
    <div className={cn('relative', className)} style={{ width: size, height: size * 1.38 }}>
      <div
        className="absolute left-0 top-0"
        style={{
          width: size,
          height: size,
          background: color,
          borderRadius: '50% 50% 50% 0',
          transform: 'translateY(8%) rotate(-45deg) scale(0.92)',
          transformOrigin: '50% 50%',
        }}
      />
      <div
        className="absolute flex items-center justify-center rounded-full bg-white font-bold leading-none"
        style={{ width: disc, height: disc, left: (size - disc) / 2, top: size * 0.5 - disc / 2 + size * 0.04, fontSize: size * 0.42, color: '#2f2b2a' }}
      >
        {label}
      </div>
    </div>
  )
}
