import { cn } from '../../../ui'

/** Rounded-square compass mark used by the centre nav button (plain shapes, inherits currentColor). */
export function CompassGlyph({ size = 22, filled = false, className }: { size?: number; filled?: boolean; className?: string }) {
  const needle = size * 0.62
  return (
    <span
      className={cn('relative inline-flex items-center justify-center', className)}
      style={{
        width: size,
        height: size,
        borderRadius: size * 0.3,
        border: filled ? undefined : `${Math.max(1.6, size * 0.085)}px solid currentColor`,
        background: filled ? 'currentColor' : undefined,
      }}
    >
      <span
        className="absolute"
        style={{
          width: needle * 0.36,
          height: needle,
          borderRadius: needle,
          transform: 'rotate(45deg)',
          border: filled ? undefined : `${Math.max(1.4, size * 0.075)}px solid currentColor`,
          background: filled ? 'var(--needle, #1f1f1f)' : undefined,
        }}
      />
    </span>
  )
}
