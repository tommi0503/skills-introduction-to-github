import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export function SandCard({ title, className, children }: { title: string; className?: string; children?: ReactNode }) {
  return (
    <section className={cn('absolute rounded-[12px] px-[15px] pt-[18px]', className)} style={{ background: theme.sand }}>
      <h3 className="text-[17px] font-semibold leading-none">{title}</h3>
      {children}
    </section>
  )
}
