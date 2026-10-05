import type { ReactNode } from 'react'
import { Bike, House } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'
import { ClubMark } from './Tag'

export interface DeliveryInfoProps {
  eta: string
  etaIcon: 'blue' | 'teal'
  /** extra runs after "배달팁 무료" (distance, min order…) */
  extra?: ReactNode
  className?: string
}

/** "약 N분 · 배달팁 무료" line. */
export function DeliveryInfo({ eta, etaIcon, extra, className }: DeliveryInfoProps) {
  return (
    <p className={cn('flex items-center whitespace-nowrap tracking-[-0.3px]', className)}>
      {etaIcon === 'blue' ? (
        <span className="mr-[3px] inline-flex h-[14px] w-[14px] items-center justify-center rounded-full bg-[#3b82f6]">
          <Bike size={10} color="#fff" strokeWidth={2.2} />
        </span>
      ) : (
        <House size={15} color="#21b3a3" fill="#21b3a3" strokeWidth={2} className="mr-[2px]" />
      )}
      <span className="text-[#333]">{eta}</span>
      <span className="ml-[10px] mr-[3px]">
        <ClubMark size={12} />
      </span>
      <b className="font-bold" style={{ color: theme.deliver }}>배달팁 무료</b>
      {extra}
    </p>
  )
}
