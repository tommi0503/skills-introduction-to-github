import type { CSSProperties } from 'react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { BotShape } from '../data'
import { theme } from '../theme'

export interface BotAvatarProps {
  shape: BotShape
  size?: number
  online?: boolean
  className?: string
}

/** Mascot silhouette shapes (flat placeholders — the mascots themselves are artwork). */
function Silhouette({ shape, size }: { shape: BotShape; size: number }) {
  const s = (v: number) => (v / 42) * size
  const abs = (style: CSSProperties, className?: string) => (
    <ImagePlaceholder label="bot mascot" className={cn('absolute', className)} style={style} />
  )
  switch (shape) {
    case 'triangle':
      return abs({ left: 0, top: s(1), width: size, height: s(38), clipPath: 'polygon(50% 0, 100% 100%, 0 100%)', borderRadius: s(8) })
    case 'pill':
      return abs({ left: 0, top: s(8), width: size, height: s(26) }, 'rounded-[12px]')
    case 'circle':
      return abs({ left: 0, top: 0, width: size, height: size }, 'rounded-full')
    case 'square':
      return abs({ left: 0, top: 0, width: size, height: size }, 'rounded-[10px]')
    case 'drop':
      return abs({ left: s(5), top: s(9), width: s(32), height: s(32), borderRadius: '50% 0 50% 50%', transform: 'rotate(-45deg)' })
    case 'group':
      return (
        <>
          {abs({ left: s(9), top: s(-4), width: s(24), height: s(15) }, 'rounded-[7px]')}
          {abs({ left: s(-3), top: s(15), width: s(24), height: s(24) }, 'rounded-full')}
          {abs({ left: s(26), top: s(19), width: s(18), height: s(18), borderRadius: '50% 0 50% 50%', transform: 'rotate(-45deg)' })}
        </>
      )
  }
}

export function BotAvatar({ shape, size = 42, online, className }: BotAvatarProps) {
  return (
    <div className={cn('relative shrink-0', className)} style={{ width: size, height: size }}>
      <Silhouette shape={shape} size={size} />
      {online && (
        <span
          className="absolute rounded-full border-2 border-white"
          style={{ right: -4, bottom: -4, width: 13, height: 13, background: theme.online }}
        />
      )}
    </div>
  )
}
