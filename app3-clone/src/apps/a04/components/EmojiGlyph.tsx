import { ImagePlaceholder, cn } from '../../../ui'

/** Inline stand-in for a colour emoji (graphic → flat placeholder). */
export function EmojiGlyph({ size = 18, round, className }: { size?: number; round?: boolean; className?: string }) {
  return (
    <ImagePlaceholder
      className={cn('inline-block align-[-3px]', round ? 'rounded-full' : 'rounded-[3px]', className)}
      style={{ width: size, height: size * (round ? 1 : 0.85) }}
      label="emoji"
    />
  )
}
