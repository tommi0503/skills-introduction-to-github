interface ArcTextProps {
  text: string
  width: number
  height: number
  /** How far the arc apex rises above its ends. */
  rise: number
  className?: string
  color: string
}

/** Text set along an upward arc (오늘보다 더 나은 내일). */
export function ArcText({ text, width, height, rise, className, color }: ArcTextProps) {
  const id = `arc-${text.length}-${width}`
  return (
    <svg width={width} height={height} className={className} style={{ overflow: 'visible' }}>
      <path id={id} d={`M 0 ${height} Q ${width / 2} ${height - rise * 2} ${width} ${height}`} fill="none" />
      <text fill={color}>
        <textPath href={`#${id}`} startOffset="50%" textAnchor="middle">
          {text}
        </textPath>
      </text>
    </svg>
  )
}
