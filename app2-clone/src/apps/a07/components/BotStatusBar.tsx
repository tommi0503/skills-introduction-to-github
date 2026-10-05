import { HighlightChip, StatusBar } from '../../../ui'

/** Status bar with the recording's "Highlight" chip over the time. */
export function BotStatusBar() {
  return (
    <>
      <StatusBar className="absolute inset-x-0 top-0" paddingX={40} paddingTop={20} />
      <HighlightChip className="left-[23px]! top-[25px]! rounded-[9px]! px-[10px]! py-[8px]! text-[18px]!" />
    </>
  )
}
