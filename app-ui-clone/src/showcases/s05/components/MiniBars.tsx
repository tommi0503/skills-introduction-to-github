export interface MiniBarsProps {
  heights: number[]
  highlight: number
  color: string
  base: string
  barWidth?: number
  gap?: number
}

/** Tiny bottom-aligned bar chart with one highlighted bar. */
export function MiniBars({ heights, highlight, color, base, barWidth = 20, gap = 3.5 }: MiniBarsProps) {
  return (
    <div className="flex items-end" style={{ gap }}>
      {heights.map((h, i) => (
        <span
          key={i}
          className="rounded-[4px]"
          style={{ width: barWidth, height: h, background: i === highlight ? color : base }}
        />
      ))}
    </div>
  )
}
