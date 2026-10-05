import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface StageCaptionProps {
  align?: 'left' | 'right'
  className?: string
  children: ReactNode
}

/** Small studio caption printed on the stage under the phones. */
export function StageCaption({ align = 'left', className, children }: StageCaptionProps) {
  return (
    <p className={cn('whitespace-nowrap', align === 'right' && 'text-right', className)}>{children}</p>
  )
}
