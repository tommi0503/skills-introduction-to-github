import { Volume2 } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Book } from '../data'

/** Book cover (placeholder) with play badge and centered metadata. */
export function BookTile({ book }: { book: Book }) {
  return (
    <div className="w-[167px]">
      <div className="relative h-[251px] overflow-hidden rounded-[3px] shadow-[0_4px_12px_rgba(0,0,0,0.12)]">
        <ImagePlaceholder label={`${book.title} cover`} className="absolute inset-0" />
        <span className="absolute top-[212px] left-[12px] flex size-[35px] items-center justify-center rounded-full bg-[#8b8b8b]/80 text-white">
          <Volume2 size={17} fill="currentColor" strokeWidth={2} />
        </span>
      </div>
      {book.author && (
        <div className="mt-[22px] text-center">
          <p className="text-[16px] leading-[22px] font-medium text-[#111]">{book.title}</p>
          <p className="text-[14px] leading-[20px] text-[#6b6b70]">{book.author}</p>
          <p className="text-[14px] leading-[20px] text-[#c4c4c8]">{book.duration}</p>
          <p className="flex items-center justify-center gap-[6px] text-[14px] leading-[20px] text-[#c4c4c8]">
            {book.price ?? 'Only with Ultra'}
            {book.ultra && (
              <ImagePlaceholder label="Ultra badge" className="size-[18px] rounded-full" />
            )}
          </p>
        </div>
      )}
    </div>
  )
}
