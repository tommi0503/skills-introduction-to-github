import type { ReactNode } from 'react'
import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'

export interface ShellProps {
  background: string
  statusColor?: string
  className?: string
  homeTone?: 'dark' | 'light'
  showHome?: boolean
  children?: ReactNode
}

export function Shell({ background, statusColor = '#000', className, homeTone = 'dark', showHome = false, children }: ShellProps) {
  return (
    <AppScreen background={background} className={className ?? 'font-inter'}>
      {children}
      <div className="absolute inset-x-0 top-0 z-40">
        <StatusBar color={statusColor} paddingTop={20} paddingX={54} fontSize={15.5} className="pr-[35px]! font-inter" />
      </div>
      {showHome && <HomeIndicator tone={homeTone} width={138} bottom={8} />}
    </AppScreen>
  )
}
