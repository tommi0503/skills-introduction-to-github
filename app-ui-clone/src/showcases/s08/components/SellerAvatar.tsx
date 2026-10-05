import { Check } from 'lucide-react'
import { Avatar } from '../../../ui'
import { theme } from '../theme'

/** Seller photo with a white ring and a green "verified" tick. */
export function SellerAvatar({ size, ring = 2.5, badgeSide = 'left' }: { size: number; ring?: number; badgeSide?: 'left' | 'right' }) {
  const badge = Math.round(size * 0.36)
  return (
    <div className="relative" style={{ width: size, height: size }}>
      <Avatar size={size} tone="#d4d0c8" className="rounded-full" ring={`${ring}px solid #fff`} />
      <span
        className="absolute flex items-center justify-center rounded-full text-white"
        style={{ width: badge, height: badge, [badgeSide]: -1, bottom: -1, background: theme.verified, boxShadow: '0 0 0 1.5px #fff' }}
      >
        <Check size={badge * 0.7} strokeWidth={3.5} />
      </span>
    </div>
  )
}
