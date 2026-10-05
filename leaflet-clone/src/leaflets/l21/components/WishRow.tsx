import { ImagePlaceholder, cn } from '../../../ui'
import { SpeechBubble } from '../../shared-2021/components/SpeechBubble'
import type { AudienceWish } from '../data'

export interface WishRowProps {
  wish: AudienceWish
  className?: string
}

/** A speech bubble with an illustration beside it; the tail points at the illustration. */
export function WishRow({ wish, className }: WishRowProps) {
  const bubbleLeft = wish.side === 'left'
  return (
    <div className={cn('relative h-[110px] w-[330px]', className)}>
      <SpeechBubble
        tail={bubbleLeft ? 'right' : 'left'}
        width={210}
        height={110}
        className={cn('absolute top-0', bubbleLeft ? 'left-0' : 'left-[118px]')}
      >
        <div className="absolute left-[21px] top-[27px] flex flex-col text-[18.5px] font-bold leading-[28px] tracking-[-0.03em] text-[#3b5c80]">
          {wish.lines.map((l) => (
            <span key={l}>{l}</span>
          ))}
        </div>
      </SpeechBubble>
      <ImagePlaceholder
        label={wish.illustration}
        className={cn('absolute top-0 h-[110px] w-[92px]', bubbleLeft ? 'left-[238px]' : 'left-[5px]')}
      />
    </div>
  )
}
