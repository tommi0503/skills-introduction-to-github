import { ImagePlaceholder, PANEL, Placed } from '../../../ui'

export interface WaveBandProps {
  x: number
  width: number
  /** y of crests and troughs (sheet px). */
  top: number
  bottom: number
  period: number
  /** x of one crest, to phase the sine. */
  crestX: number
}

/** Wave artwork silhouette: flat placeholder clipped by a sine top edge. */
export function WaveBand({ x, width, top, bottom, period, crestX }: WaveBandProps) {
  const height = PANEL.height - top
  const amp = (bottom - top) / 2
  const pts: string[] = []
  for (let px = 0; px <= width; px += 6) {
    const y = amp - amp * Math.cos((2 * Math.PI * (x + px - crestX)) / period)
    pts.push(`${px}px ${y.toFixed(1)}px`)
  }
  pts.push(`${width}px ${height}px`, `0px ${height}px`)
  return (
    <Placed x={x} y={top} width={width} height={height}>
      <ImagePlaceholder className="h-full w-full" label="waves" style={{ clipPath: `polygon(${pts.join(',')})` }} />
    </Placed>
  )
}
