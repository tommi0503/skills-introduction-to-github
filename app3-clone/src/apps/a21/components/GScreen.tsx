import type { ReactNode } from 'react'
import { AppScreen, HomeIndicator } from '../../../ui'
import { GStatusBar } from './GStatusBar'

/** Common shell: background, status bar, home indicator. */
export function GScreen({ background = '#fff', children }: { background?: string; children?: ReactNode }) {
  return (
    <AppScreen background={background} className="font-inter">
      <div className="absolute inset-x-0 top-0 z-40">
        <GStatusBar />
      </div>
      {children}
      <HomeIndicator width={140} bottom={7} />
    </AppScreen>
  )
}
