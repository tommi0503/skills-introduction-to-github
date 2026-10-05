export interface DimOverlayProps {
  /** Top edge (logical px); everything below is dimmed. */
  top?: number
  opacity?: number
  zIndex?: number
}

/** Black scrim drawn behind modal sheets. */
export function DimOverlay({ top = 0, opacity = 0.5, zIndex = 10 }: DimOverlayProps) {
  return <div className="absolute inset-x-0 bottom-0" style={{ top, zIndex, background: `rgba(0,0,0,${opacity})` }} />
}
