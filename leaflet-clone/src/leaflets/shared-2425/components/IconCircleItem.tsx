import type { LucideIcon } from 'lucide-react'
import { IconBadge, cn } from '../../../ui'

interface IconCircleItemProps {
  icon: LucideIcon
  title: string
  lines: string[]
  /** Diameter of the navy circle. */
  size: number
  iconSize: number
  circleClassName?: string
  /** Horizontal space between circle and text block. */
  gap: number
  className?: string
  titleClassName?: string
  lineClassName?: string
}

/** Navy circle icon followed by a bold title and detail lines (운영 기간 / 신청 방법 …). */
export function IconCircleItem({
  icon,
  title,
  lines,
  size,
  iconSize,
  circleClassName,
  gap,
  className,
  titleClassName,
  lineClassName,
}: IconCircleItemProps) {
  return (
    <div className={cn('flex items-center', className)} style={{ gap }}>
      <IconBadge icon={icon} size={size} iconSize={iconSize} strokeWidth={2} className={cn('rounded-full text-white', circleClassName)} />
      <div className="flex min-w-0 flex-col">
        <p className={cn('m-0 whitespace-nowrap', titleClassName)}>{title}</p>
        {lines.map((l) => (
          <p key={l} className={cn('m-0 whitespace-nowrap', lineClassName)}>
            {l}
          </p>
        ))}
      </div>
    </div>
  )
}
