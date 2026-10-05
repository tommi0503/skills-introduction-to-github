import { StatusBar } from '../../../ui'

export interface HighlightStatusBarProps {
  /** Fill of the screen-recorder "Highlight" chip covering the clock. */
  chipColor?: string
}

/** iOS status bar with the clock hidden behind the "Highlight" chip. */
export function HighlightStatusBar({ chipColor = '#ababab' }: HighlightStatusBarProps) {
  return (
    <div className="absolute inset-x-0 top-0 z-40">
      <StatusBar color="#000" paddingX={40} paddingTop={18} fontSize={16} />
      <div
        className="absolute z-50 flex items-center justify-center rounded-[11px] font-inter font-semibold text-white"
        style={{ left: 23, top: 25, width: 98, height: 34, background: chipColor, fontSize: 17, letterSpacing: -0.2 }}
      >
        Highlight
      </div>
    </div>
  )
}
