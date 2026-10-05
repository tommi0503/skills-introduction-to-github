import type { ReactNode } from 'react'
import { PhoneFrame } from '../../ui'
import { naver } from './theme'

export interface NaverPhoneProps {
  background?: string
  width?: number
  height?: number
  children?: ReactNode
}

/** Frameless screenshot "card" with the rounded corners used in every Naver Pay reference. */
export function NaverPhone({
  background = '#fff',
  width = naver.phoneWidth,
  height = naver.phoneHeight,
  children,
}: NaverPhoneProps) {
  return (
    <PhoneFrame
      width={width}
      height={height}
      logicalWidth={naver.logicalWidth}
      screenRadius={naver.screenRadius}
      screenBackground={background}
    >
      <div className="relative h-full w-full overflow-hidden font-pretendard">{children}</div>
    </PhoneFrame>
  )
}
