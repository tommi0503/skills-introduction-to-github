import { Children, type CSSProperties, type ReactNode } from 'react'
import { cn } from '../core/cn'
import { PANEL, sheetWidth, type PanelCount } from '../core/geometry'

export interface LeafletProps {
  /** Number of panels; must match the number of <Panel> children. */
  panels: PanelCount
  /** Sheet-wide background (colour/gradient) painted under every panel. */
  background?: string
  /**
   * Elements that span several panels (a band across the bottom, a map over two panels...).
   * Rendered absolutely over the whole sheet, in sheet pixel coordinates.
   */
  underlay?: ReactNode
  overlay?: ReactNode
  /** Draw faint fold lines between panels. */
  folds?: boolean
  foldColor?: string
  className?: string
  style?: CSSProperties
  children: ReactNode
}

/**
 * Flat, unfolded leaflet sheet made of equal-size panels laid side by side.
 * It owns only geometry; panel contents come from children (Open/Closed).
 */
export function Leaflet({
  panels,
  background = '#fff',
  underlay,
  overlay,
  folds = false,
  foldColor = 'rgba(0,0,0,0.06)',
  className,
  style,
  children,
}: LeafletProps) {
  const count = Children.count(children)
  if (count !== panels) {
    throw new Error(`Leaflet expects ${panels} <Panel> children, got ${count}`)
  }
  return (
    <div
      data-stage
      className={cn('relative overflow-hidden', className)}
      style={{ width: sheetWidth(panels), height: PANEL.height, background, ...style }}
    >
      {underlay && <div className="pointer-events-none absolute inset-0">{underlay}</div>}
      <div className="relative flex">{children}</div>
      {overlay && <div className="absolute inset-0">{overlay}</div>}
      {folds &&
        Array.from({ length: panels - 1 }, (_, i) => (
          <div
            key={i}
            className="pointer-events-none absolute top-0 bottom-0 w-px"
            style={{ left: PANEL.width * (i + 1), background: foldColor }}
          />
        ))}
    </div>
  )
}
