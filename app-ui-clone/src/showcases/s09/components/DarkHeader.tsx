import type { ReactNode } from 'react'
import { theme } from '../theme'
import { BrandBar } from './BrandBar'
import { KitchenStatusBar } from './KitchenStatusBar'

export interface DarkHeaderProps {
  height: number
  cartCount: number
  /** Rounded bottom corners (sheet look). */
  rounded?: boolean
  /** Extra content under the brand row (e.g. search). */
  children?: ReactNode
}

/** Dark app header: status bar, brand row and optional extra content. */
export function DarkHeader({ height, cartCount, rounded = true, children }: DarkHeaderProps) {
  return (
    <div
      className="absolute inset-x-0 top-0 z-10"
      style={{ height, background: theme.dark, borderRadius: rounded ? '0 0 22px 22px' : undefined }}
    >
      <KitchenStatusBar />
      <div className="absolute inset-x-[21px] top-[61px]">
        <BrandBar cartCount={cartCount} />
      </div>
      {children}
    </div>
  )
}
