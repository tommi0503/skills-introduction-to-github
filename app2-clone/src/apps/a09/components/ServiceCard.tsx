import { ImagePlaceholder } from '../../../ui'

export function ServiceCard({ label }: { label: string }) {
  return (
    <div className="w-[127px] shrink-0 overflow-hidden rounded-[6px] bg-white">
      <ImagePlaceholder label={label} className="h-[96px] w-full" />
      <div className="flex h-[74px] items-center px-[10px] pt-[5px] text-[14.5px] font-medium whitespace-nowrap text-[#222325]">{label}</div>
    </div>
  )
}
