import { cn } from '../../../ui'
import type { Token } from '../data'
import { palette as c } from '../theme'

/** Tappable word tile with the 3D bottom edge; `used` tiles become flat grey slots. */
export function WordChip({ token, padX = 12, className }: { token: Token; padX?: number; className?: string }) {
  if (token.used)
    return (
      <span
        className={cn('flex h-[40px] items-center rounded-[12px] text-[16.5px] text-transparent', className)}
        style={{ background: c.used, paddingInline: padX + 2 }}
      >
        {token.word}
      </span>
    )
  return (
    <span
      className={cn('flex h-[41px] items-center rounded-[12px] bg-white pb-[2px] text-[16.5px]', className)}
      style={{ paddingInline: padX, color: c.text, border: `2px solid ${c.line}`, borderBottomWidth: 4 }}
    >
      {token.word}
    </span>
  )
}
