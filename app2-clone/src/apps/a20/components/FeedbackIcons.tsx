import { Copy, Share, ThumbsDown, ThumbsUp } from 'lucide-react'
import { cn } from '../../../ui'

/** Copy / (share) / thumbs feedback icon row. */
export function FeedbackIcons({ share, gap = 16, size = 16, className }: { share?: boolean; gap?: number; size?: number; className?: string }) {
  const icons = share ? [Copy, Share, ThumbsUp, ThumbsDown] : [Copy, ThumbsUp, ThumbsDown]
  return (
    <div className={cn('flex items-center text-[#8a8a8a]', className)} style={{ gap }}>
      {icons.map((I, i) => (
        <I key={i} size={size} strokeWidth={1.4} />
      ))}
    </div>
  )
}
