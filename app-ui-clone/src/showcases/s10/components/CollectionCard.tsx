import { ImagePlaceholder } from '../../../ui'
import type { Collection } from '../data'

/** Coloured collection tile: title + dotted tags on the left, product photos on the right. */
export function CollectionCard({ collection }: { collection: Collection }) {
  return (
    <div className="relative h-[164px] overflow-hidden rounded-[26px]" style={{ background: collection.color }}>
      <ImagePlaceholder label="snacks" className="absolute bottom-0" style={{ ...collection.snacks }} />
      <ImagePlaceholder label="snack bags" className="absolute bottom-0" style={{ ...collection.bags }} />
      <div className="absolute top-[14px] left-[15px]">
        <div className="text-[17.5px] leading-[26px] font-bold text-black">{collection.title}</div>
        <div className="mt-[5px] text-[14px] text-[#5a5a5a]">{collection.tags.join(' • ')}</div>
      </div>
    </div>
  )
}
