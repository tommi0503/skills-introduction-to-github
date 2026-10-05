import { HighlightChip, StatusBar } from '../../../ui'

export function FvStatusBar({ color = '#000' }: { color?: string }) {
  return (
    <>
      <StatusBar className="absolute inset-x-0 top-0" color={color} paddingX={40} paddingTop={20} />
      <HighlightChip className="top-[25px]! left-[23px]! rounded-[9px]! px-[10px]! py-[8px]! text-[18px]!" />
    </>
  )
}
