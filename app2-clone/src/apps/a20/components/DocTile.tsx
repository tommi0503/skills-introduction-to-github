import { ChevronDown, Star, UserCheck } from 'lucide-react'
import type { DocItem } from '../data'
import { DocThumb } from './DocThumb'

/** One documents-grid entry: thumbnail, star, optional shared badge, title + date. */
export function DocTile({ item, center }: { item: DocItem; center: number }) {
  return (
    <>
      <DocThumb thumb={item.thumb} />
      {item.star && (
        <Star
          size={19}
          strokeWidth={1.3}
          className="absolute -translate-x-1/2 -translate-y-1/2"
          style={{ left: item.star.x, top: item.star.y }}
          fill={item.starred ? '#c9473a' : 'rgba(255,255,255,0.7)'}
          stroke={item.starred ? '#c9473a' : '#9a9a9a'}
        />
      )}
      {item.shared && (
        <span
          className="absolute flex h-[30px] w-[30px] -translate-x-1/2 items-center justify-center rounded-full bg-white shadow-[0_1px_4px_rgba(0,0,0,0.15)]"
          style={{ left: center, top: item.labelTop - 25 }}
        >
          <UserCheck size={15} strokeWidth={2.4} className="text-[#3f6fd0]" fill="#3f6fd0" />
        </span>
      )}
      <div className="absolute w-[120px] -translate-x-1/2 text-center" style={{ left: center, top: item.labelTop - 2 }}>
        <div className="relative inline-block text-[14.5px] leading-[20px] text-[#222]">
          {item.title.map((t) => (
            <div key={t}>{t}</div>
          ))}
          <ChevronDown size={11} strokeWidth={1.6} className="absolute -right-[16px] text-[#aaa]" style={{ top: (item.title.length - 1) * 10 + 4 }} />
        </div>
        {item.date && <div className="text-[10.5px] leading-[14px] text-[#9a9a9a]">{item.date}</div>}
      </div>
    </>
  )
}
