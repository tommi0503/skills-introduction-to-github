import { Code2, Mic, NotebookPen, Video } from 'lucide-react'
import { cn } from '../../../ui'
import { accents, type Accent } from '../theme'

const icons = { mic: Mic, notes: NotebookPen, api: Code2, video: Video }
export type TileIcon = keyof typeof icons

export interface IconTileProps {
  accent: Accent
  icon: TileIcon
  size?: number
  className?: string
}

/** Small rounded colour tile holding a feature glyph. */
export function IconTile({ accent, icon, size = 22, className }: IconTileProps) {
  const Icon = icons[icon]
  return (
    <span
      className={cn('inline-flex shrink-0 items-center justify-center rounded-[3px]', className)}
      style={{ width: size, height: size, background: accents[accent].tile, boxShadow: 'inset 0 0 0 1px rgba(0,0,0,0.35)' }}
    >
      <Icon size={size * 0.62} strokeWidth={2} color="rgba(0,0,0,0.75)" />
    </span>
  )
}
