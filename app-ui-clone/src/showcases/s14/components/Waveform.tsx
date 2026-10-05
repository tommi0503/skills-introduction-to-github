import { cn } from '../../../ui'

export interface WaveformProps {
  /** 'T' = tall bar, anything else = short bar. */
  pattern: string
  width: number
  height: number
  barWidth?: number
  /** Short bar height as a fraction of `height`. */
  shortRatio?: number
  /** Number of leading bars drawn in the "played" colour. */
  played?: number
  color?: string
  playedColor?: string
  className?: string
}

/** Evenly spaced vertical bars centred on one axis. */
export function Waveform({
  pattern,
  width,
  height,
  barWidth = 1.6,
  shortRatio = 0.5,
  played = 0,
  color = 'rgba(255,255,255,0.75)',
  playedColor = color,
  className,
}: WaveformProps) {
  const bars = pattern.split('')
  return (
    <div className={cn('flex items-center justify-between', className)} style={{ width, height }}>
      {bars.map((b, i) => (
        <span
          key={i}
          className="rounded-full"
          style={{
            width: barWidth,
            height: b === 'T' ? height : height * shortRatio,
            background: i < played ? playedColor : color,
          }}
        />
      ))}
    </div>
  )
}
