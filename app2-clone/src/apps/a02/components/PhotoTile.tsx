import type { ReactNode } from 'react'
import { Heart, Plus } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { theme } from '../theme'

export interface PhotoTileProps {
  width: number
  height: number
  radius?: number
  className?: string
  /** Bottom-left overlay content (white text). */
  children?: ReactNode
  /** Heart + add buttons at the top-right. */
  actions?: boolean
  /** Top-right overlay (e.g. a menu button); overrides actions. */
  corner?: ReactNode
  tone?: string
}

/** Photo placeholder with optional overlay text and corner actions. */
export function PhotoTile({ width, height, radius = 14, className, children, actions, corner, tone = theme.photoDark }: PhotoTileProps) {
  return (
    <div className={`relative shrink-0 overflow-hidden ${className ?? ''}`} style={{ width, height, borderRadius: radius }}>
      <ImagePlaceholder tone={tone} className="absolute inset-0" label="photo" />
      {corner ?? (actions && (
        <div className="absolute top-[14px] right-[10px] flex gap-[6px] text-white">
          <Heart size={20} strokeWidth={1.8} />
          <span className="flex h-[19px] w-[19px] items-center justify-center rounded-full border-[1.8px] border-white">
            <Plus size={13} strokeWidth={2.4} />
          </span>
        </div>
      ))}
      {children && <div className="absolute inset-x-0 bottom-0 px-[12px] pt-[12px] pb-[8px] text-white">{children}</div>}
    </div>
  )
}
