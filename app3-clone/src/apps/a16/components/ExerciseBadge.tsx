import { ImagePlaceholder } from '../../../ui'
import type { Badge } from '../data'

export function ExerciseBadge({ badge }: { badge: Badge }) {
  const Icon = badge.icon
  return (
    <div className="flex items-center gap-[10px]">
      {Icon ? (
        <span className="flex h-[23px] w-[23px] items-center justify-center rounded-full" style={{ background: badge.color }}>
          <Icon size={13} strokeWidth={2.6} color="#fff" />
        </span>
      ) : (
        <ImagePlaceholder className="rounded-[4px]" style={{ width: 22, height: 21 }} label="badge icon" />
      )}
      <span className="text-[14px] font-bold tracking-[0.6px]" style={{ color: badge.color }}>
        {badge.label}
      </span>
    </div>
  )
}
