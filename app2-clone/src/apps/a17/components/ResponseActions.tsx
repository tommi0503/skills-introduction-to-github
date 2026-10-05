import { Copy, RotateCw, Share, ThumbsDown, ThumbsUp, Play } from 'lucide-react'

const actions = [Copy, Share, Play, ThumbsUp, ThumbsDown, RotateCw]

/** Row of response action icons (copy, share, read aloud, rate, retry). */
export function ResponseActions() {
  return (
    <div className="flex items-center gap-[13.5px] text-[#55544f]">
      {actions.map((Icon, i) => (
        <Icon key={i} size={18} strokeWidth={1.6} />
      ))}
    </div>
  )
}
