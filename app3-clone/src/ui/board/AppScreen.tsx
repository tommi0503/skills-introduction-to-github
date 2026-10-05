import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../core/cn'
import { SCREEN } from './geometry'

export interface AppScreenProps {
  background?: string
  className?: string
  style?: CSSProperties
  children?: ReactNode
}

/** One phone screen — always SCREEN size with the iPhone corner radius. Content is free. */
export function AppScreen({ background = '#fff', className, style, children }: AppScreenProps) {
  return (
    <section
      className={cn('relative shrink-0 overflow-hidden', className)}
      style={{ width: SCREEN.width, height: SCREEN.height, borderRadius: SCREEN.radius, background, ...style }}
    >
      {children}
    </section>
  )
}
