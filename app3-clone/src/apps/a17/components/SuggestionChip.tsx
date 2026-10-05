import { ImagePlaceholder } from '../../../ui'

export function SuggestionChip({ label }: { label: string }) {
  return (
    <div className="flex h-[39px] shrink-0 items-center gap-[9px] rounded-full bg-[#f0f0f0] pr-[14px] pl-[12px] text-[14px] whitespace-nowrap text-[#222]">
      <ImagePlaceholder className="h-[19px] w-[19px] rounded-[5px]" label="emoji" />
      {label}
    </div>
  )
}
