import type { ReactNode } from 'react'
import { AppScreen, HomeIndicator, StatusBar } from '../../../ui'

export interface ShellProps {
  background: string
  statusColor: string
  children?: ReactNode
}

/** Screen frame with the iOS status bar and home indicator on top of the content. */
export function Shell({ background, statusColor, children }: ShellProps) {
  return (
    <AppScreen background={background} className="font-inter">
      {children}
      <div className="absolute inset-x-0 top-0 z-40">
        <StatusBar color={statusColor} paddingTop={15} paddingX={33} fontSize={15.5} />
      </div>
      <HomeIndicator width={138} bottom={8} />
    </AppScreen>
  )
}
