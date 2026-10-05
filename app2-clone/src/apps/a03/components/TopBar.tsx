import { HighlightChip, StatusBar } from '../../../ui'

export function TopBar({ color = '#000' }: { color?: string }) {
  return (
    <>
      <StatusBar color={color} paddingX={34} paddingTop={20} className="absolute inset-x-0 top-0" />
      <HighlightChip className="!left-[22px] !top-[25px] rounded-[10px] px-[10px] py-[7px] text-[18px] tracking-[-0.2px]" />
    </>
  )
}
