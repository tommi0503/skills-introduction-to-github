import { EllipsisVertical, Heart, MessageCircle } from 'lucide-react'
import type { ReactNode } from 'react'
import { ImagePlaceholder } from '../../../ui'
import type { Listing } from '../data'
import { kr } from '../theme'
import { EmojiGlyph } from './EmojiGlyph'

export interface ListingRowProps {
  item: Listing
  /** Extra content under the row (e.g. action buttons). */
  footer?: ReactNode
  showCounters?: boolean
}

function Counter({ icon: Icon, value }: { icon: typeof Heart; value: number }) {
  return (
    <span className="flex items-center gap-[2px]">
      <Icon size={14} strokeWidth={1.5} fill={kr.faint} stroke="#fff" />
      {value}
    </span>
  )
}

/** Marketplace list row: square thumbnail, two-line title, meta, bold price, counters. */
export function ListingRow({ item, footer, showCounters = true }: ListingRowProps) {
  return (
    <div className="border-b px-[16px] pt-[16px] pb-[17px]" style={{ borderColor: kr.line }}>
      <div className="relative flex gap-[16px]">
        <ImagePlaceholder className="h-[106px] w-[106px] rounded-[8px]" label={item.title} />
        <div className="flex min-h-[106px] min-w-0 flex-1 flex-col" style={{ paddingRight: item.menu ? 28 : 20 }}>
          <div className="line-clamp-2 text-[15px] leading-[22px] tracking-[-0.2px] break-keep">
            {item.emoji && <EmojiGlyph className="mr-[5px]" />}
            {item.title}
          </div>
          <p className="text-[12.5px] leading-[22px]" style={{ color: kr.faint }}>
            {item.meta}
          </p>
          <p className="text-[15px] leading-[24px] font-bold">{item.price}</p>
          {showCounters && (item.comments || item.likes) ? (
            <div
              className="mt-auto flex justify-end gap-[6px] pt-[3px] text-[12.5px]"
              style={{ color: kr.sub, marginRight: item.menu ? -28 : -20 }}
            >
              {item.comments ? <Counter icon={MessageCircle} value={item.comments} /> : null}
              {item.likes ? <Counter icon={Heart} value={item.likes} /> : null}
            </div>
          ) : null}
        </div>
        {item.menu && <EllipsisVertical size={18} strokeWidth={2} className="absolute top-[1px] right-[-2px]" style={{ color: kr.faint }} />}
      </div>
      {footer}
    </div>
  )
}
