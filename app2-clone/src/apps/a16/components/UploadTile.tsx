import type { IconItem } from '../data'

/** Square-ish action tile with an icon above a two-line label. */
export function UploadTile({ item }: { item: IconItem }) {
  const Icon = item.icon
  return (
    <div className="flex h-[103px] w-[78px] flex-col items-center rounded-[10px] bg-[#f2f2f3] pt-[16px]">
      <Icon size={21} strokeWidth={1.9} className="text-[#111]" />
      <span className="mt-[10px] text-center text-[14px] leading-[20px] whitespace-pre-line text-[#111]">{item.label}</span>
    </div>
  )
}
