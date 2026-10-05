import { Ellipsis } from 'lucide-react'
import { Avatar } from '../../../ui'
import type { FloatingCard } from '../data'

/** Small white "skeleton" card floating over the welcome collage. */
export function MiniProfileCard({ card }: { card: FloatingCard }) {
  return (
    <div
      className="absolute flex items-center gap-[8px] rounded-[6px] bg-white px-[7px] shadow-[0_2px_6px_rgba(0,0,0,0.08)]"
      style={{ left: card.x, top: card.y, width: card.width, height: 39 }}
    >
      <Avatar size={20} tone="#d1d5db" />
      <div className="flex flex-1 flex-col gap-[5px]">
        <span className="h-[4px] w-[70%] rounded-full bg-[#e8e8e8]" />
        <span className="h-[3px] w-[45%] rounded-full bg-[#ececec]" />
      </div>
      {card.width < 140 && card.x > 250 ? null : <Ellipsis size={12} strokeWidth={2.5} />}
    </div>
  )
}
