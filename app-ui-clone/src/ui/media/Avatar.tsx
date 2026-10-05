import type { ReactNode } from 'react'
import { cn } from '../core/cn'
import { ImagePlaceholder } from './ImagePlaceholder'

export interface AvatarProps {
  size: number
  /** Initials / text instead of a photo placeholder. */
  text?: string
  className?: string
  /** Ring around the avatar, e.g. "2px solid #fff". */
  ring?: string
  /** Element pinned to the bottom-right (status dot, badge...). */
  badge?: ReactNode
  rounded?: string
  tone?: string
}

export function Avatar({ size, text, className, ring, badge, rounded = 'rounded-full', tone }: AvatarProps) {
  return (
    <div className={cn('relative shrink-0', className)} style={{ width: size, height: size }}>
      {text ? (
        <div
          className={cn('flex h-full w-full items-center justify-center bg-neutral-200 text-neutral-500', rounded)}
          style={{ outline: ring, fontSize: size * 0.36 }}
        >
          {text}
        </div>
      ) : (
        <ImagePlaceholder tone={tone} className={cn('h-full w-full', rounded)} style={{ outline: ring }} label="avatar" />
      )}
      {badge && <div className="absolute -right-0.5 -bottom-0.5">{badge}</div>}
    </div>
  )
}
