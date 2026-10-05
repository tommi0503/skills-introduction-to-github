import { cn } from '../../../ui'
import { serifStyle, theme } from '../theme'

export interface TwoToneProps {
  muted: string
  strong: string
  /** Put the strong phrase on its own line. */
  stacked?: boolean
  mutedFirst?: boolean
  className?: string
}

/** Serif heading with a faded lead phrase and a solid ink phrase. */
export function TwoTone({ muted, strong, stacked, mutedFirst = true, className }: TwoToneProps) {
  const a = <span style={{ color: theme.faded }}>{muted}</span>
  const b = <span style={{ color: theme.ink }}>{strong}</span>
  return (
    <h2 className={cn(theme.fonts.serif, 'font-normal', className)} style={serifStyle(26)}>
      {mutedFirst ? a : b}
      {stacked ? <br /> : ' '}
      {mutedFirst ? b : a}
    </h2>
  )
}
