export interface ArcTextProps {
  text: string
  width: number
  height: number
  /** Radius of the arc the text follows. */
  radius: number
  className?: string
  color?: string
}

/** Text set along an upward arc (SVG textPath). */
export function ArcText({ text, width, height, radius, className, color = 'currentColor' }: ArcTextProps) {
  const cx = width / 2
  const cy = radius + 4
  const id = `arc-${text.length}-${radius}`
  const a = Math.asin(Math.min(1, cx / radius))
  const x0 = cx - radius * Math.sin(a)
  const y0 = cy - radius * Math.cos(a)
  const x1 = cx + radius * Math.sin(a)
  return (
    <svg width={width} height={height} className={className} style={{ overflow: 'visible' }}>
      <defs>
        <path id={id} d={`M ${x0} ${y0} A ${radius} ${radius} 0 0 1 ${x1} ${y0}`} />
      </defs>
      <text fill={color}>
        <textPath href={`#${id}`} startOffset="50%" textAnchor="middle">
          {text}
        </textPath>
      </text>
    </svg>
  )
}
