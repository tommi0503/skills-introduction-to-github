import { Bookmark, ThumbsDown, ThumbsUp } from 'lucide-react'
import { cn } from '../../../ui'
import { dislikeStat, saveStats, savers, type Saver } from '../data'
import { OvalPhoto } from './OvalPhoto'

function SaverBadge({ kind }: { kind: NonNullable<Saver['badge']> }) {
  return kind === 'bookmark' ? (
    <span className="flex h-[17px] w-[14px] items-center justify-center bg-white">
      <Bookmark size={14} fill="#3a7bf2" color="#3a7bf2" strokeWidth={1} />
    </span>
  ) : (
    <span className="flex h-[17px] w-[16px] items-center justify-center">
      <ThumbsUp size={16} fill="#a9c6ec" color="#fff" strokeWidth={1.4} />
    </span>
  )
}

/** Outlined card listing reaction counts and who saved the place. */
export function SavedByCard({ className }: { className?: string }) {
  return (
    <div className={cn('overflow-hidden rounded-[8px] border-[1.5px] border-[#3b3b3d] bg-white/60', className)}>
      <div className="flex items-center justify-between pl-[12px] pr-[12px] pt-[10px]">
        <span className="a05-wide text-[12.5px] font-extrabold tracking-[-0.5px] text-[#111]">SAVED BY</span>
        <div className="flex items-center gap-[10px] text-[14px] text-[#444]">
          {saveStats.map((s) => (
            <span key={s.key} className="flex items-center gap-[4px]">
              <s.icon size={11} fill={s.color} color={s.color} strokeWidth={1.4} />
              {s.value}
            </span>
          ))}
          <span className="flex items-center gap-[3px]">
            <ThumbsDown size={11} fill="#e2423b" color="#e2423b" strokeWidth={1.4} />
            <span className="h-[9px] w-[9px] rounded-full border border-[#ccc] bg-[#eee]" />
            {dislikeStat.value}
          </span>
        </div>
      </div>
      <div className="mt-[6px] flex gap-[18px] pl-[10px]">
        {savers.map((s) => (
          <div key={s.key} className="flex w-[63px] shrink-0 flex-col items-center">
            <OvalPhoto className="h-[76px] w-[63px]" badge={s.badge && <SaverBadge kind={s.badge} />} />
            <span className="mt-[2px] text-[13px] text-[#8b8b8f]">{s.name}</span>
          </div>
        ))}
      </div>
    </div>
  )
}
