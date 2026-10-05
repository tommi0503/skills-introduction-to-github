import type { CSSProperties, ReactNode } from 'react'

export interface ScaledProps {
  /** Logical (design) size of the content. */
  logicalWidth: number
  logicalHeight: number
  /** Uniform scale applied to the logical box. */
  scale: number
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/**
 * Lays content out at a logical size (e.g. a 390pt iPhone screen) and
 * scales it into the space it occupies in the reference image.
 */
export function Scaled({ logicalWidth, logicalHeight, scale, className, style, children }: ScaledProps) {
  return (
    <div style={{ width: logicalWidth * scale, height: logicalHeight * scale, ...style }} className={className}>
      <div
        style={{
          width: logicalWidth,
          height: logicalHeight,
          transform: `scale(${scale})`,
          transformOrigin: 'top left',
          position: 'relative',
        }}
      >
        {children}
      </div>
    </div>
  )
}
