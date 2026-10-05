import { Ellipsis } from 'lucide-react'
import { IconButton } from '../../../ui'
import type { Basket } from '../data'
import { theme } from '../theme'
import { AvatarStack } from './AvatarStack'
import { BasketButton } from './BasketButton'

export function BasketCard({ basket }: { basket: Basket }) {
  return (
    <article className="rounded-[12px] bg-white px-[14px] pt-[15px] pb-[15px]" style={{ border: `1.5px solid ${theme.border}` }}>
      <div className="flex items-center gap-[12px]">
        <AvatarStack count={basket.avatars} />
        <div className="min-w-0 flex-1">
          <div className="text-[15px] leading-[19px] font-medium">{basket.title}</div>
          {basket.lines.map((l) => (
            <div
              key={l.text}
              className="mt-[1.5px] text-[13px] leading-[16.5px]"
              style={{ color: l.tone === 'accent' ? theme.accent : theme.muted }}
            >
              {l.text}
            </div>
          ))}
        </div>
        {basket.showMore && (
          <IconButton icon={Ellipsis} size={36} iconSize={18} strokeWidth={2.4} className="bg-[#f3f3f3] text-black" />
        )}
      </div>
      <div className="mt-[12px] flex flex-col gap-[8px]">
        {basket.actions.map((a) => (
          <BasketButton key={a.label} action={a} />
        ))}
      </div>
    </article>
  )
}
