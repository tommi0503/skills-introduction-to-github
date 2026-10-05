/** Small pie showing an instalment's share of the plan. */
export function PieProgress({
  progress,
  size = 30,
  fill = '#5b8def',
  track = '#e3e3e8',
}: {
  progress: number
  size?: number
  fill?: string
  track?: string
}) {
  const r = size / 2
  const a = progress * 2 * Math.PI
  const x = r + r * Math.sin(a)
  const y = r - r * Math.cos(a)
  const large = progress > 0.5 ? 1 : 0
  return (
    <svg width={size} height={size} viewBox={`0 0 ${size} ${size}`}>
      <circle cx={r} cy={r} r={r} fill={progress >= 1 ? fill : track} />
      {progress > 0 && progress < 1 && <path d={`M${r},${r} L${r},0 A${r},${r} 0 ${large} 1 ${x},${y} Z`} fill={fill} />}
    </svg>
  )
}
