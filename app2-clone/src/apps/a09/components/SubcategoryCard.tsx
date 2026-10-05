import { ImagePlaceholder } from '../../../ui'

export function SubcategoryCard({ label }: { label: string }) {
  return (
    <div className="flex h-[105px] w-[137px] shrink-0 flex-col items-center rounded-[8px] border border-[#ececec] bg-white pt-[9px]">
      <ImagePlaceholder label="illustration" className="h-[48px] w-[48px] rounded-[4px]" />
      <div className="flex flex-1 items-center px-[6px] text-center text-[14px] leading-[16.5px] font-medium text-[#404145]">{label}</div>
    </div>
  )
}
