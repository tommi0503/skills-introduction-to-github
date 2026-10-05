import { StatusBar } from '../../../ui'

export interface HighlightStatusBarProps {
  /** Background of the translucent "Highlight" chip that covers the clock. */
  chipColor?: string
  color?: string
}

/** iOS status bar whose clock is covered by the screen-recorder "Highlight" chip. */
export function HighlightStatusBar({ chipColor = '#a5a5a5', color = '#000' }: HighlightStatusBarProps) {
  return (
    <div className="absolute inset-x-0 top-0 z-40">
      <StatusBar color={color} paddingX={40} paddingTop={18} fontSize={16} />
      <div
        className="absolute z-50 flex items-center justify-center rounded-[11px] font-semibold text-white"
        style={{ left: 23, top: 25, width: 98, height: 33, background: chipColor, fontSize: 17, letterSpacing: -0.2 }}
      >
        Highlight
      </div>
    </div>
  )
}
