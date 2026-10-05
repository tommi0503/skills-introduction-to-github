import { BadgePercent } from 'lucide-react'

/** Purple 배민클럽 coupon badge in the header. */
export function ClubBadge({ size = 25 }: { size?: number }) {
  return <BadgePercent size={size} fill="#8c6cf2" color="#fff" strokeWidth={1.6} />
}
