import { HighlightChip, StatusBar } from '../../../ui'

/** Status bar with the "Highlight" capsule over the time. */
export function TopBar({ color = '#000', dot }: { color?: string; dot?: boolean }) {
  return (
    <>
      <StatusBar
        color={color}
        paddingX={34}
        paddingTop={20}
        className="absolute inset-x-0 top-0"
      />
      {dot && <span className="absolute z-50 h-[6px] w-[6px] rounded-full bg-[#ff9500]" style={{ left: 212, top: 26 }} />}
      <HighlightChip className="!left-[24px] !top-[25px] rounded-[10px] px-[10px] py-[7px] text-[18px] tracking-[-0.2px]" />
    </>
  )
}
