import { BulletList, ImagePlaceholder } from '../../../ui'
import { growth } from '../../shared-3031/theme'
import type { ServiceItem } from '../data'

export interface ServiceItemViewProps {
  item: ServiceItem
  circle: number
  textOffset: { x: number; y: number }
}

/** Circular illustration (placeholder) with heading and bullet list beside it. */
export function ServiceItemView({ item, circle, textOffset }: ServiceItemViewProps) {
  return (
    <div className="relative" style={{ width: circle, height: circle }}>
      <ImagePlaceholder label={`${item.key} illustration`} className="h-full w-full rounded-full" />
      <div className="absolute top-0" style={{ left: textOffset.x, top: textOffset.y }}>
        <h3 className="m-0 whitespace-nowrap text-[16px] font-bold leading-[25px] tracking-[-0.3px]" style={{ color: growth.ink }}>
          {item.heading.map((h) => (
            <span key={h} className="block">
              {h}
            </span>
          ))}
        </h3>
        <BulletList
          items={item.bullets}
          className="mt-[11px] whitespace-nowrap text-[13px] leading-[21px] tracking-[-0.2px]"
          marker={<span className="mt-[8px] block h-[5px] w-[5px] rounded-full" style={{ background: growth.ink }} />}
          markerClassName="w-[18px] pl-[3px]"
          itemClassName=""
        />
      </div>
    </div>
  )
}
