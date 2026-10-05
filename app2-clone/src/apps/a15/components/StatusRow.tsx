import { HighlightChip, StatusBar } from '../../../ui'

/** Status bar with the recording's "Highlight" chip covering the time. */
export function StatusRow({ color = '#000' }: { color?: string }) {
  return (
    <>
      <StatusBar color={color} paddingX={41} paddingTop={19} className="absolute inset-x-0 top-0" />
      <HighlightChip className="left-[23px]! top-[24px]! rounded-[10px]! px-[10px]! py-[8px]! text-[18.5px]! tracking-[-0.2px]" />
    </>
  )
}
