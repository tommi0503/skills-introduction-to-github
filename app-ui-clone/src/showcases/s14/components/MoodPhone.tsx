import type { ReactNode } from 'react'
import { HomeIndicator, PhoneFrame, StatusBar } from '../../../ui'
import type { MoodTheme } from '../theme'
import { BottomNav } from './BottomNav'

export interface MoodPhoneProps {
  theme: MoodTheme
  children?: ReactNode
}

/** White-edged device shell shared by every mood screen (390pt logical). */
export function MoodPhone({ theme, children }: MoodPhoneProps) {
  return (
    <PhoneFrame
      width={220}
      height={476}
      logicalWidth={390}
      screenRadius={17}
      bezel={{ thickness: 3, color: '#ffffff' }}
      screenBackground={theme.background}
      className="shadow-[0_6px_16px_rgba(0,0,0,0.10),0_0_0_0.5px_rgba(0,0,0,0.06)]"
    >
      <div className="absolute inset-0 font-inter text-white">
        <StatusBar color="#fff" fontSize={17} paddingTop={15} paddingX={50} height={48} battery={{ level: 0.45 }} />
        {children}
        <div className="absolute left-[36px] top-[762px]">
          <BottomNav />
        </div>
        <HomeIndicator tone="light" width={142} bottom={6} />
      </div>
    </PhoneFrame>
  )
}
