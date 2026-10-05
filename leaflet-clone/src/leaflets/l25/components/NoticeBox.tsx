import type { CSSProperties } from 'react'
import { BulletList, ImagePlaceholder } from '../../../ui'
import { library } from '../../shared-2425/theme'

interface NoticeBoxProps {
  title: string
  items: string[]
  style?: CSSProperties
}

/** Soft white card with title, monitor illustration and bullet notes. */
export function NoticeBox({ title, items, style }: NoticeBoxProps) {
  return (
    <div className="absolute box-border rounded-[14px] border-2 border-[#ece8dc] bg-[#f4f4f2]" style={style}>
      <p className="absolute left-[30px] top-[20px] m-0 font-dohyeon text-[22px] leading-none" style={{ color: library.title }}>
        {title}
      </p>
      <ImagePlaceholder label="monitor illustration" className="absolute right-[30px] top-[22px] h-[47px] w-[55px] rounded-[4px]" />
      <BulletList
        items={items}
        className="absolute left-[27px] top-[75px] gap-[6px] text-[11.5px] font-semibold leading-[17.5px] tracking-[-0.01em] text-[#45496b]"
        marker="•"
        markerClassName="w-[14px]"
      />
    </div>
  )
}
