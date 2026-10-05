import type { Swatch } from '../data'
import { SwatchDot } from './SwatchDot'

interface SwatchStackProps {
  colors: Swatch[]
}

/** Vertical white capsule listing colour options on a product photo. */
export function SwatchStack({ colors }: SwatchStackProps) {
  return (
    <div className="flex w-[16px] flex-col items-center gap-[5px] rounded-full bg-white py-[4px]">
      {colors.map((c) => (
        <SwatchDot key={c.color} swatch={c} size={8} />
      ))}
    </div>
  )
}
