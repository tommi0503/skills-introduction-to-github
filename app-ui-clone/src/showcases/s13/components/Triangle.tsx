import { cn } from '../../../ui'

export type TriangleDir = 'left' | 'right' | 'up' | 'down'

const sides: Record<TriangleDir, [string, string]> = {
  left: ['borderRight', 'y'],
  right: ['borderLeft', 'y'],
  up: ['borderBottom', 'x'],
  down: ['borderTop', 'x'],
}

/** Small solid CSS triangle in currentColor (play / caret glyph). */
export function Triangle({ dir, size = 5, className }: { dir: TriangleDir; size?: number; className?: string }) {
  const [solid, axis] = sides[dir]
  const transparent =
    axis === 'y'
      ? { borderTop: `${size}px solid transparent`, borderBottom: `${size}px solid transparent` }
      : { borderLeft: `${size}px solid transparent`, borderRight: `${size}px solid transparent` }
  return (
    <span
      className={cn('block h-0 w-0', className)}
      style={{ ...transparent, [solid]: `${size * 1.4}px solid currentColor` }}
    />
  )
}
