export interface ArcTextProps {
  text: string
  width: number
  height: number
  /** How far the arc's middle rises above its ends (px). */
  rise: number
  fontSize: number
  color: string
  className?: string
}

/** Text set along a gentle upward arc (SVG textPath). */
export function ArcText({ text, width, height, rise, fontSize, color, className }: ArcTextProps) {
  const id = `arc-${text.length}-${width}-${rise}`
  const base = height - 4
  return (
    <svg width={width} height={height} className={className} aria-label={text}>
      <defs>
        <path id={id} d={`M 0 ${base} Q ${width / 2} ${base - rise * 2} ${width} ${base}`} />
      </defs>
      <text fill={color} fontSize={fontSize} textAnchor="middle" className="font-jua">
        <textPath href={`#${id}`} startOffset="50%">
          {text}
        </textPath>
      </text>
    </svg>
  )
}
