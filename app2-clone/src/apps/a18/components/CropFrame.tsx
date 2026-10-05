import { cn } from '../../../ui'

export interface CropFrameProps {
  className?: string
  /** Bracket arm length and thickness. */
  arm?: number
  thickness?: number
  radius?: number
  color?: string
}

/** Four corner brackets framing a selection (editor crop / Lens selection). */
export function CropFrame({ className, arm = 18, thickness = 3, radius = 0, color = '#fff' }: CropFrameProps) {
  const corners = [
    { top: 0, left: 0, borderTopWidth: thickness, borderLeftWidth: thickness, borderTopLeftRadius: radius },
    { top: 0, right: 0, borderTopWidth: thickness, borderRightWidth: thickness, borderTopRightRadius: radius },
    { bottom: 0, left: 0, borderBottomWidth: thickness, borderLeftWidth: thickness, borderBottomLeftRadius: radius },
    { bottom: 0, right: 0, borderBottomWidth: thickness, borderRightWidth: thickness, borderBottomRightRadius: radius },
  ]
  return (
    <div className={cn('pointer-events-none absolute', className)}>
      {corners.map((c, i) => (
        <span key={i} className="absolute border-solid" style={{ width: arm, height: arm, borderColor: color, borderWidth: 0, ...c }} />
      ))}
    </div>
  )
}
