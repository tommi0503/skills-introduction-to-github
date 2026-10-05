import type { ReactNode } from 'react'
import { AppScreen, cn, HomeIndicator, StatusBar, type StatusBarProps } from '../../../ui'

export interface SheetScreenProps {
  /** The page underneath the sheet (rendered then dimmed). */
  backdrop: ReactNode
  background: string
  /** Black overlay opacity over the backdrop. */
  dim: number
  sheetTop: number
  sheetClassName?: string
  status?: StatusBarProps
  /** Render the status bar beneath the dim overlay (it gets dimmed too). */
  statusDimmed?: boolean
  /** Elements that sit above the dim overlay but outside the sheet. */
  overlay?: ReactNode
  className?: string
  children: ReactNode
}

/** Modal bottom-sheet over a dimmed page — the shared shape of all four screens. */
export function SheetScreen({
  backdrop,
  background,
  dim,
  sheetTop,
  sheetClassName,
  status,
  statusDimmed,
  overlay,
  className,
  children,
}: SheetScreenProps) {
  const bar = (
    <div className="absolute inset-x-0 top-0">
      <StatusBar paddingTop={15} fontSize={15.5} className="!pr-[19px]" {...status} />
    </div>
  )
  return (
    <AppScreen background={background} className={className}>
      <div className="absolute inset-0">
        {backdrop}
        {statusDimmed && bar}
      </div>
      <div className="absolute inset-0" style={{ background: `rgba(0,0,0,${dim})` }} />
      {!statusDimmed && bar}
      {overlay}
      <div className={cn('absolute inset-x-0 bottom-0 overflow-hidden', sheetClassName)} style={{ top: sheetTop }}>
        {children}
      </div>
      <HomeIndicator bottom={5} width={138} />
    </AppScreen>
  )
}
