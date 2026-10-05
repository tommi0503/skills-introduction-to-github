import { ImagePlaceholder } from '../../../ui'
import type { Note } from '../data'
import { nd } from '../theme'

/** Grid card: photo with tag pill, date, divider, title and two-line excerpt. */
export function NoteCard({ note }: { note: Note }) {
  return (
    <div className="h-[217px] overflow-hidden rounded-[14px] bg-white p-[4px]">
      <div className="relative">
        <ImagePlaceholder className="h-[110px] w-full rounded-[12px]" label={note.title} />
        <span className="absolute top-[8px] right-[7px] rounded-full bg-white px-[9px] py-[3px] text-[8.5px] leading-[11px]">
          {note.tag}
        </span>
      </div>
      <div className="px-[6px]">
        <p className="mt-[9px] text-[7.5px]" style={{ color: nd.muted }}>
          {note.date}
        </p>
        <div className="mt-[4px] h-px bg-[#efefef]" />
        <p className="mt-[8px] truncate pr-[6px] text-[15px] font-medium tracking-[0.1px]">{note.title}</p>
        <p className="mt-[3px] line-clamp-2 pr-[4px] text-[10px] leading-[17px]" style={{ color: nd.muted }}>
          {note.excerpt}
        </p>
      </div>
    </div>
  )
}
