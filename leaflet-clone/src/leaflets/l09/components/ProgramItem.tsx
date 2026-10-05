import { ImagePlaceholder, VerticalText } from '../../../ui'
import { Lines } from '../../shared-0812'
import type { Program } from '../data'

/** Title, description, photo with a rotated schedule note beside it. */
export function ProgramItem({ item }: { item: Program }) {
  return (
    <article>
      <h3 className="m-0 ml-[8px] text-[21.5px] leading-[28px] text-[#333]">{item.title}</h3>
      <Lines lines={item.desc} className="mt-[22px] ml-[8px] text-[16.8px] leading-[29px] text-[#444]" />
      <div className="mt-[15px] flex items-start gap-[14px]">
        <ImagePlaceholder className="h-[143px] w-[273px]" label={item.title} />
        <VerticalText mode="rotate" className="text-[15px] leading-[16px] text-[#444] [text-orientation:sideways]">
          {item.schedule}
        </VerticalText>
      </div>
    </article>
  )
}
