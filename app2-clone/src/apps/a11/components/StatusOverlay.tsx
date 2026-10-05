import { cn, HighlightChip, StatusBar } from '../../../ui'

/** Status bar with the recording's "Highlight" chip covering the time. */
export function StatusOverlay({ chipClassName }: { chipClassName?: string }) {
  return (
    <>
      <StatusBar color="#fff" className="absolute inset-x-0 top-0" paddingX={42} paddingTop={20} time="" />
      <HighlightChip className={cn('top-[25px]! left-[22px]! px-[10px]! py-[8px]! text-[17px]! bg-[#4a4a4a]!', chipClassName)} />
    </>
  )
}
