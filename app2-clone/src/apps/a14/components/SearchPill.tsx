import { SearchField, cn } from '../../../ui'

/** Rounded white "Search all locations" field. */
export function SearchPill({ label, className }: { label: string; className?: string }) {
  return (
    <SearchField
      placeholder={label}
      iconSize={17}
      iconStrokeWidth={1.6}
      className={cn('absolute h-[46px] rounded-full border border-[#ececee] bg-white pl-[15px] text-[#6a6a6f]', className)}
      textClassName="ml-[2px] text-[13px] text-[#77777c]"
    />
  )
}
