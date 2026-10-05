import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** Centered section title + muted lead used by every Cloudflare section. */
export function SectionHeading({
  title,
  body,
  size = 48,
  gap,
  className,
}: {
  title: ReactNode
  body: ReactNode
  size?: 48 | 56
  gap: number
  className?: string
}) {
  return (
    <div className={cn('text-center', className)}>
      <h2
        className="font-medium text-[#262626]"
        style={{ fontSize: size, lineHeight: `${size}px`, letterSpacing: size === 56 ? '-1.4px' : '-1.2px' }}
      >
        {title}
      </h2>
      <p className="text-[19.2px] leading-[23.04px] tracking-[-0.48px] text-[#262626]/70" style={{ marginTop: gap }}>
        {body}
      </p>
    </div>
  )
}
