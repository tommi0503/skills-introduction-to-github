import { StatusBar } from '../../../ui'

export interface HighlightStatusBarProps {
  /** Fill of the screen-recorder "Highlight" chip covering the clock. */
  chipColor?: string
  /** Clock text (mostly hidden behind the chip). */
  time?: string
}

/** iOS status bar with the clock hidden behind the "Highlight" chip. */
export function HighlightStatusBar({ time = '', chipColor = '#ababab' }: HighlightStatusBarProps) {
  return (
    <div className="absolute inset-x-0 top-0 z-40">
      <StatusBar time={time} color="#000" paddingX={44} paddingTop={22} fontSize={16} />
      <div
        className="absolute z-50 flex items-center justify-center rounded-[11px] font-inter font-semibold text-white"
        style={{ left: 23, top: 24.8, width: 97, height: 34.4, background: chipColor, fontSize: 17, letterSpacing: -0.2 }}
      >
        Highlight
      </div>
    </div>
  )
}
