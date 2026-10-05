import { ImagePlaceholder, cn } from '../../../ui'
import { fv } from '../theme'

/** Photo placeholder with the green "online" dot. */
export function OnlineAvatar({ size, dot = 8, className }: { size: number; dot?: number; className?: string }) {
  return (
    <span className={cn('relative block shrink-0', className)} style={{ width: size, height: size }}>
      <ImagePlaceholder label="avatar" className="h-full w-full rounded-full" />
      <span
        className="absolute rounded-full border-2 border-white"
        style={{ width: dot + 2, height: dot + 2, right: size * 0.02, bottom: size * 0.04, background: fv.online }}
      />
    </span>
  )
}
