import { Wifi } from 'lucide-react'
import { Battery, SignalBars, StatusBar } from '../../../ui'

/** iOS status bar tuned to this board (light glyphs on dark headers, dark on maps). */
export function KitchenStatusBar({ tone = 'light' }: { tone?: 'light' | 'dark' }) {
  return (
    <StatusBar
      color={tone === 'light' ? '#fff' : '#111'}
      className="absolute inset-x-0 top-0"
      paddingTop={13}
      paddingX={30}
      fontSize={14.5}
      timeClassName="font-poppins font-medium"
      right={
        <div className="flex items-center gap-[5px] pt-[3px]">
          <SignalBars size={0.85} />
          <Wifi size={14} strokeWidth={2.8} />
          <Battery size={0.85} />
        </div>
      }
    />
  )
}
