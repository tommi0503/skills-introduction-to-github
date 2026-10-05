import { ImagePlaceholder } from '../../../ui'
import { theme } from '../theme'

/** Overlapping 20px integration logos (placeholders). */
export function IconStack({ count }: { count: number }) {
  return (
    <span className="relative inline-block h-[20px]" style={{ width: 20 + (count - 1) * 14 }}>
      {Array.from({ length: count }, (_, i) => (
        <ImagePlaceholder
          key={i}
          label="Integration logo"
          tone={theme.tones.icon}
          className="absolute top-0 h-[20px] w-[20px] rounded-[5px] border border-white/60"
          style={{ left: i * 14 }}
        />
      ))}
    </span>
  )
}
