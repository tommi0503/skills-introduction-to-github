import { HighlightChip, StatusBar } from '../../../ui'

/** Status bar + "Highlight" capsule over the time. */
export function Chrome({ chipClassName }: { chipClassName?: string }) {
  return (
    <>
      <StatusBar paddingX={54} paddingTop={19} className="absolute inset-x-0 top-0 !pr-[37px]" timeClassName="opacity-0" />
      <HighlightChip className={`!left-[23px] !top-[25px] rounded-[10px] !px-[11px] !py-[7px] font-inter text-[19px] tracking-[-0.2px] ${chipClassName ?? ''}`} />
    </>
  )
}
