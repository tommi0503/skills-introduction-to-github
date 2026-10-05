import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../core/cn'

export interface BezelSpec {
  /** Thickness of the device body around the screen, in stage px. */
  thickness: number
  /** Body colour (e.g. '#1c1c1e', '#3a3540'). */
  color: string
  /** Optional outer ring colour (metal edge). */
  edgeColor?: string
  edgeWidth?: number
}

export interface PhoneFrameProps {
  /** Outer size in stage px (includes the bezel when present). */
  width: number
  height: number
  /** Logical width the screen content is designed at (e.g. 390). Scale = screenWidth / logicalWidth. */
  logicalWidth: number
  /** Screen corner radius in stage px. */
  screenRadius: number
  bezel?: BezelSpec
  screenBackground?: string
  /** Extra classes for the outer element (shadows, borders...). */
  className?: string
  screenClassName?: string
  style?: CSSProperties
  children?: ReactNode
}

/**
 * Generic device mockup. It only owns geometry (bezel, radius, scaling);
 * the screen content is fully supplied by children (Open/Closed).
 */
export function PhoneFrame({
  width,
  height,
  logicalWidth,
  screenRadius,
  bezel,
  screenBackground = '#fff',
  className,
  screenClassName,
  style,
  children,
}: PhoneFrameProps) {
  const t = bezel?.thickness ?? 0
  const screenW = width - t * 2
  const screenH = height - t * 2
  const scale = screenW / logicalWidth
  const logicalHeight = screenH / scale

  return (
    <div
      className={cn('relative', className)}
      style={{
        width,
        height,
        borderRadius: screenRadius + t,
        background: bezel?.color,
        boxShadow: bezel?.edgeColor ? `inset 0 0 0 ${bezel.edgeWidth ?? 1.5}px ${bezel.edgeColor}` : undefined,
        padding: t,
        ...style,
      }}
    >
      <div
        className={cn('relative overflow-hidden', screenClassName)}
        style={{ width: screenW, height: screenH, borderRadius: screenRadius, background: screenBackground }}
      >
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
    </div>
  )
}
