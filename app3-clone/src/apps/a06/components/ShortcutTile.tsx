import { Play, UserRound } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { Shortcut } from '../data'
import { sp } from '../theme'

export function ShortcutTile({ item }: { item: Shortcut }) {
  return (
    <div className="flex h-[48px] items-center overflow-hidden rounded-[4px]" style={{ background: sp.tile }}>
      {item.iconOnly ? (
        <span className="flex h-[48px] w-[48px] items-center justify-center" style={{ background: '#333' }}>
          <UserRound size={22} strokeWidth={1.3} color={sp.muted} />
        </span>
      ) : (
        <ImagePlaceholder className="h-[48px] w-[48px]" label={`${item.title} artwork`} />
      )}
      <span className="line-clamp-2 flex-1 pr-[14px] pl-[8px] text-[13px] leading-[17.5px] font-bold" style={{ color: sp.white }}>
        {item.title}
      </span>
      {item.playing && <Play size={16} fill="#fff" strokeWidth={0} className="mr-[10px]" />}
      {item.unread && <span className="mr-[10px] h-[7px] w-[7px] rounded-full" style={{ background: sp.blue }} />}
    </div>
  )
}
