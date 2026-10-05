import { Placed, cn } from '../../../ui'

export interface DisplayLineSpec {
  text: string
  x: number
  y: number
  size: number
  /** Vertical stretch to match the printed display face. */
  scaleY?: number
}

export interface DisplayLineProps {
  line: DisplayLineSpec
  color: string
  className?: string
}

/** One absolutely placed line of a stacked display title. */
export function DisplayLine({ line, color, className }: DisplayLineProps) {
  return (
    <Placed
      x={line.x}
      y={line.y}
      className={cn('m-0 whitespace-nowrap', className)}
      style={{
        color,
        fontSize: line.size,
        lineHeight: 1,
        transform: line.scaleY ? `scaleY(${line.scaleY})` : undefined,
        transformOrigin: 'top left',
      }}
    >
      {line.text}
    </Placed>
  )
}
