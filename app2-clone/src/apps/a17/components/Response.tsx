import { Droplet } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { ResponseBlock } from '../data'

/** Inline glyph used after a list item (emoji stand-ins). */
function Trailing({ kind }: { kind: NonNullable<Extract<ResponseBlock, { kind: 'li' }>['trailing']> }) {
  return kind === 'droplet' ? (
    <Droplet size={16} fill="#7cc0f2" stroke="#4a9be0" strokeWidth={1.4} className="ml-[6px] inline -translate-y-[2px]" />
  ) : (
    <ImagePlaceholder label="broccoli emoji" className="ml-[6px] inline-block size-[19px] -translate-y-[-3px] rounded-full" />
  )
}

/** Renders assistant response blocks in Claude's serif reading style. */
export function Response({ blocks, className }: { blocks: ResponseBlock[]; className?: string }) {
  return (
    <div className={cn('font-times text-[19px] leading-[27.5px] text-[#141413]', className)}>
      {blocks.map((b, i) => {
        if (b.kind === 'p') return <p key={i} className="mb-[18px]">{b.text}</p>
        if (b.kind === 'h') return <p key={i} className="mb-[18px] font-bold">{b.text}</p>
        return (
          <div key={i} className="mb-[16px] flex">
            <span className="w-[24px] shrink-0 pl-[10px]">•</span>
            <p className="w-[322px]">
              {b.lead && <b>{b.lead} </b>}
              {b.text}
              {b.trailing && <Trailing kind={b.trailing} />}
            </p>
          </div>
        )
      })}
    </div>
  )
}
