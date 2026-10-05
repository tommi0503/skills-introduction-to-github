import type { ReactNode } from 'react'
import { cn } from '../../../ui'
import { meshBackground, type MeshGradient } from '../theme'

interface GradientCardProps {
  gradient: MeshGradient
  className?: string
  children?: ReactNode
}

/** Hero card with a pastel four-corner mesh background. */
export function GradientCard({ gradient, className, children }: GradientCardProps) {
  return (
    <div className={cn('relative overflow-hidden rounded-[24px]', className)} style={{ background: meshBackground(gradient) }}>
      {children}
    </div>
  )
}
