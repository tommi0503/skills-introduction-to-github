import { ImagePlaceholder } from '../../../ui'
import type { MiniBook } from '../data'

/** Compact cover + title pill. */
export function MiniBookCard({ book }: { book: MiniBook }) {
  return (
    <div className="flex h-[58px] w-[167px] items-center gap-[8px] rounded-[8px] bg-[#f7f7f8] px-[5px]">
      <ImagePlaceholder label={book.title} className="h-[48px] w-[48px] rounded-[3px]" />
      <span className="text-[12.5px] leading-[15px] font-medium whitespace-pre-line text-[#222]">{book.title}</span>
    </div>
  )
}
