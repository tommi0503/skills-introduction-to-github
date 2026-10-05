import { cn } from '../../../ui'
import type { Token } from '../data'
import { palette as c } from '../theme'

/** Tappable word tile with the 3D bottom edge; `used` tiles become flat grey slots. */
export function WordChip({ token, className }: { token: Token; className?: string }) {
  if (token.used)
    return (
      <span
        className={cn('flex h-[40px] items-center rounded-[12px] px-[16px] text-[16.5px] font-medium text-transparent', className)}
        style={{ background: c.used }}
      >
        {token.word}
      </span>
    )
  return (
    <span
      className={cn('flex h-[41px] items-center rounded-[12px] bg-white px-[12px] pb-[2px] text-[16.5px] font-medium', className)}
      style={{ color: c.text, border: `2px solid ${c.line}`, borderBottomWidth: 4 }}
    >
      {token.word}
    </span>
  )
}
