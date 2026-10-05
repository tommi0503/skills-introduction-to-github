import type { ReactNode } from 'react'
import { DynamicIsland, PhoneFrame, StatusBar } from '../../../ui'

/** Hardware side buttons, in stage px relative to the device top. */
const sideButtons = [
  { side: 'left', top: 82, height: 12 },
  { side: 'left', top: 112, height: 25 },
  { side: 'left', top: 149, height: 28 },
  { side: 'right', top: 132, height: 27 },
] as const

export interface InvestPhoneProps {
  background: string
  children?: ReactNode
}

/** iPhone 15-style black-bezel device with graphite rim (393pt logical). */
export function InvestPhone({ background, children }: InvestPhoneProps) {
  return (
    <div className="relative">
      {sideButtons.map((b) => (
        <span
          key={`${b.side}-${b.top}`}
          className="absolute w-[2px] rounded-[1px] bg-[#9a9a9f]"
          style={{ top: b.top, height: b.height, [b.side]: -1.5 }}
        />
      ))}
      <PhoneFrame
        width={200}
        height={414}
        logicalWidth={393}
        screenRadius={25}
        bezel={{ thickness: 8.5, color: '#050505', edgeColor: '#b4b4b9', edgeWidth: 1.6 }}
        screenBackground={background}
        className="shadow-[0_10px_24px_rgba(60,20,90,0.18)]"
      >
        <div className="absolute inset-0 font-inter text-[#1c1c1e]">
          <StatusBar time="19:27" fontSize={15} paddingTop={23} paddingX={28} height={56} />
          <DynamicIsland width={129} height={36} top={13} />
          {children}
        </div>
      </PhoneFrame>
    </div>
  )
}
