import { ImagePlaceholder } from '../../../ui'
import type { Category } from '../data'

export function CategoryTile({ category }: { category: Category }) {
  return (
    <div className="flex w-[58px] shrink-0 flex-col items-center">
      <div className="flex h-[58px] w-[58px] items-center justify-center rounded-[16px] border border-[#f0f0f0] bg-white">
        <ImagePlaceholder label={`${category.label} icon`} className="h-[32px] w-[32px] rounded-[8px]" />
      </div>
      <span className="mt-[5px] whitespace-nowrap text-[13.5px] text-[#555]">{category.label}</span>
    </div>
  )
}
