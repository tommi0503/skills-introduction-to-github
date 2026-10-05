import type { CSSProperties } from 'react'

export interface ArcTextProps {
  text: string
  width: number
  height: number
  /** How far the arc's middle rises above its ends (px). */
  rise: number
  fontSize: number
  color: string
  className?: string
  style?: CSSProperties
  letterSpacing?: number
}

/** Text laid along a gentle upward arc (SVG textPath), centred in its box. */
export function ArcText({ text, width, height, rise, fontSize, color, className, style, letterSpacing = 0 }: ArcTextProps) {
  const id = `arc-${text.length}-${width}-${rise}`
  const base = height - 4
  const d = `M 0 ${base} Q ${width / 2} ${base - rise * 2} ${width} ${base}`
  return (
    <svg width={width} height={height} className={className} style={{ overflow: 'visible', ...style }}>
      <defs>
        <path id={id} d={d} fill="none" />
      </defs>
      <text fill={color} fontSize={fontSize} letterSpacing={letterSpacing} textAnchor="middle">
        <textPath href={`#${id}`} startOffset="50%">
          {text}
        </textPath>
      </text>
    </svg>
  )
}
