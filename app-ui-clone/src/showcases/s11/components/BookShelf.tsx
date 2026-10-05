import { ChevronLeft, ChevronRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Shelf } from '../data'

const BOOK = { width: 90, height: 133, gap: 13 }

/** Section header + row of book covers resting on a translucent coloured shelf. */
export function BookShelf({ shelf }: { shelf: Shelf }) {
  return (
    <section className="relative h-[220px]">
      <header className="flex h-[24px] items-center justify-between pr-[42px] pl-[41px]">
        <h2 className="font-inter text-[14.3px] font-semibold tracking-[-0.01em] text-[#111]">{shelf.title}</h2>
        <div className="flex items-center gap-[10px] text-[#a3a2a0]">
          <span className="font-inter text-[13.5px]">{shelf.count}</span>
          <ChevronLeft size={16} strokeWidth={1.8} />
          <ChevronRight size={16} strokeWidth={1.8} />
        </div>
      </header>
      <div className="absolute top-[37px] left-[41px] flex" style={{ gap: BOOK.gap }}>
        {Array.from({ length: shelf.books }, (_, i) => (
          <ImagePlaceholder
            key={i}
            label="book cover"
            className="shadow-[0_2px_6px_rgba(0,0,0,0.12)]"
            style={{ width: BOOK.width, height: BOOK.height }}
          />
        ))}
      </div>
      {shelf.shelf && (
        <div
          className="absolute top-[122px] left-[8px] h-[64px] w-[378px] rounded-[9px] shadow-[0_6px_12px_rgba(0,0,0,0.12)]"
          style={{ background: shelf.shelf }}
        >
          {[15, 357].map((x) => (
            <span
              key={x}
              className="absolute top-[27px] size-[11px] rounded-full border border-white/70 bg-[#c9ccd8]"
              style={{ left: x }}
            />
          ))}
        </div>
      )}
    </section>
  )
}
