import { cn } from '../../../ui'

interface OutlinedTitleProps {
  text: string
  fill: string
  stroke: string
  halo: string
  className?: string
}

/** Display line with a coloured fill, navy outline and a white halo around it. */
export function OutlinedTitle({ text, fill, stroke, halo, className }: OutlinedTitleProps) {
  const layer = 'col-start-1 row-start-1 whitespace-nowrap [paint-order:stroke_fill]'
  return (
    <div className={cn('grid', className)}>
      <span aria-hidden className={layer} style={{ color: halo, WebkitTextStroke: `12px ${halo}`, strokeLinejoin: "round" }}>
        {text}
      </span>
      <span className={layer} style={{ color: fill, WebkitTextStroke: `6px ${stroke}` }}>
        {text}
      </span>
    </div>
  )
}
