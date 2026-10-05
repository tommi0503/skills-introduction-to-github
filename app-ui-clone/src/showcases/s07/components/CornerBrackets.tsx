export interface CornerBracketsProps {
  length: number
  thickness: number
  color: string
}

const corners = [
  { top: 0, left: 0, borderTop: true, borderLeft: true },
  { top: 0, right: 0, borderTop: true, borderRight: true },
  { bottom: 0, left: 0, borderBottom: true, borderLeft: true },
  { bottom: 0, right: 0, borderBottom: true, borderRight: true },
] as const

/** Four L-shaped viewfinder corners filling the parent box. */
export function CornerBrackets({ length, thickness, color }: CornerBracketsProps) {
  return (
    <>
      {corners.map((c, i) => {
        const b = `${thickness}px solid ${color}`
        return (
          <span
            key={i}
            className="absolute"
            style={{
              width: length,
              height: length,
              top: 'top' in c ? c.top : undefined,
              bottom: 'bottom' in c ? c.bottom : undefined,
              left: 'left' in c ? c.left : undefined,
              right: 'right' in c ? c.right : undefined,
              borderTop: 'borderTop' in c ? b : undefined,
              borderBottom: 'borderBottom' in c ? b : undefined,
              borderLeft: 'borderLeft' in c ? b : undefined,
              borderRight: 'borderRight' in c ? b : undefined,
            }}
          />
        )
      })}
    </>
  )
}
