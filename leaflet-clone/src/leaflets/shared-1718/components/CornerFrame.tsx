import type { ReactNode } from 'react'

export interface CornerFrameProps {
  size: number
  arm: number
  stroke: number
  color: string
  children?: ReactNode
  className?: string
}

/** Square frame drawn only at its four corners (QR code target). */
export function CornerFrame({ size, arm, stroke, color, children, className }: CornerFrameProps) {
  const corners = [
    { top: 0, left: 0, borderTop: true, borderLeft: true },
    { top: 0, right: 0, borderTop: true, borderRight: true },
    { bottom: 0, left: 0, borderBottom: true, borderLeft: true },
    { bottom: 0, right: 0, borderBottom: true, borderRight: true },
  ]
  const line = `${stroke}px solid ${color}`
  return (
    <div className={className} style={{ position: 'relative', width: size, height: size }}>
      {corners.map(({ borderTop, borderLeft, borderRight, borderBottom, ...pos }, i) => (
        <span
          key={i}
          className="absolute"
          style={{
            ...pos,
            width: arm,
            height: arm,
            borderTop: borderTop ? line : undefined,
            borderLeft: borderLeft ? line : undefined,
            borderRight: borderRight ? line : undefined,
            borderBottom: borderBottom ? line : undefined,
          }}
        />
      ))}
      <div className="absolute inset-0 flex items-center justify-center">{children}</div>
    </div>
  )
}
