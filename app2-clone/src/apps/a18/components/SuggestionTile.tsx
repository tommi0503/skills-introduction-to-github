import { ImagePlus } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import type { Suggestion } from '../data'

/** Editor suggestion preview with a label band along the bottom. */
export function SuggestionTile({ item }: { item: Suggestion }) {
  return (
    <div className={cn('relative h-[88px] flex-1 overflow-hidden rounded-[20px]', item.active ? 'bg-[#cfd8ef]' : 'bg-[#f0f0f0]')}>
      <ImagePlaceholder
        label={`${item.label} preview`}
        tone={item.active ? '#c4cde4' : undefined}
        className="absolute inset-x-[14px] top-[8px] h-[60px] rounded-[6px]"
      />
      {item.active && <ImagePlus size={20} strokeWidth={1.8} className="absolute top-[30px] left-1/2 -translate-x-1/2 text-[#3b4a6b]" />}
      <span
        className={cn(
          'absolute inset-x-0 bottom-0 flex h-[27px] items-center justify-center text-[15px] text-white',
          item.active ? 'bg-[#3e63d8]' : 'bg-[#7d7d7d]',
        )}
      >
        {item.label}
      </span>
    </div>
  )
}
