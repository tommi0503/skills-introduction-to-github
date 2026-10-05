import { cn, HighlightChip, StatusBar } from '../../../ui'

/** Status bar with the recording's "Highlight" chip covering the time. */
export function StatusOverlay({ color = '#fff', chipClassName }: { color?: string; chipClassName?: string }) {
  return (
    <>
      <StatusBar color={color} className="absolute inset-x-0 top-0" paddingX={42} paddingTop={20} time="" />
      <HighlightChip className={cn('top-[25px]! left-[23px]! px-[10px]! py-[8px]! text-[17px]!', chipClassName)} />
    </>
  )
}
