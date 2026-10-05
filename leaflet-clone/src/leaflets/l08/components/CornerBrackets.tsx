export interface CornerBracketsProps {
  size: number
  arm: number
  thickness: number
  color?: string
}

/** Four L-shaped corner marks framing a square (the "scan me" frame). */
export function CornerBrackets({ size, arm, thickness, color = '#1c1c1c' }: CornerBracketsProps) {
  const corners = [
    { top: 0, left: 0, borderTop: true, borderLeft: true },
    { top: 0, right: 0, borderTop: true, borderRight: true },
    { bottom: 0, left: 0, borderBottom: true, borderLeft: true },
    { bottom: 0, right: 0, borderBottom: true, borderRight: true },
  ]
  const line = `${thickness}px solid ${color}`
  return (
    <div className="relative" style={{ width: size, height: size }}>
      {corners.map(({ borderTop, borderLeft, borderRight, borderBottom, ...pos }, i) => (
        <div
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
    </div>
  )
}
