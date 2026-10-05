import { ImagePlaceholder } from '../../../ui'
import type { Collection } from '../data'

/** Recommended collection: artwork block (placeholder) with label + caption below. */
export function CollectionCard({ item }: { item: Collection }) {
  return (
    <div className="w-[311px] shrink-0">
      <div className="relative h-[166px] overflow-hidden rounded-[10px]">
        <ImagePlaceholder tone={item.tone} label={`${item.title} artwork`} className="absolute inset-0" />
        {/* book covers stacked on the right */}
        <div className="absolute top-[-6px] left-[162px] flex flex-col gap-[8px]">
          <ImagePlaceholder className="h-[78px] w-[62px] rounded-[4px]" />
          <ImagePlaceholder className="h-[80px] w-[62px] rounded-[4px]" />
        </div>
        <div className="absolute top-[-14px] left-[237px] flex flex-col gap-[8px]">
          <ImagePlaceholder className="h-[36px] w-[62px] rounded-[4px]" />
          <ImagePlaceholder className="h-[94px] w-[62px] rounded-[4px]" />
          <ImagePlaceholder className="h-[40px] w-[62px] rounded-[4px]" />
        </div>
        {item.label && (
          <span className="absolute top-[100px] left-[10px] text-[34px] leading-none font-medium text-white">{item.label}</span>
        )}
      </div>
      <p className="mt-[13px] text-[16.5px] font-medium text-[#111]">{item.title}</p>
      <p className="mt-[1px] text-[16px] leading-[24px] text-[#6b6b70]">{item.description}</p>
    </div>
  )
}
