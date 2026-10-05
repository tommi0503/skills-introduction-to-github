import { ImagePlaceholder } from '../../../ui'
import { Lines } from '../../shared-0812'
import type { Sight } from '../data'

/** Bulleted sight name, justified-looking body lines and a photo. */
export function SightItem({ sight }: { sight: Sight }) {
  return (
    <article>
      <h3 className="m-0 flex items-center pl-[14px] text-[19px] leading-[28px] font-bold text-[#232323]">
        <span className="mr-[16px] inline-block h-[7px] w-[7px] rounded-full bg-[#232323]" />
        {sight.name}
      </h3>
      <Lines lines={sight.body} className="mt-[9px] text-[13.5px] leading-[27px] tracking-[-0.2px] text-[#4a4a4a]" />
      <ImagePlaceholder className="mt-[12px] h-[253px] w-[401px]" label={sight.photoLabel} />
    </article>
  )
}
