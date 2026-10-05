import { ImagePlaceholder } from '../../../ui'
import type { Feature } from '../data'
import { Pill } from './Pill'

/** Tall colourful feature tile: illustration on top, tag + title + copy at the bottom. */
export function FeatureCard({ feature }: { feature: Feature }) {
  return (
    <div className="relative h-[460px] w-[323px] shrink-0 overflow-hidden rounded-[22px]" style={{ background: feature.color }}>
      <ImagePlaceholder label="illustration" className="absolute top-[29px] left-[1px] h-[270px] w-[312px]" />
      <div className="absolute top-[303px] left-[28px] w-[250px] text-white">
        <Pill tone="outline" width={73} height={23}>
          {feature.tag}
        </Pill>
        <div className="mt-[16px] text-[20px] leading-[24px] font-medium tracking-[-0.02em]">{feature.title}</div>
        <p className="mt-[10px] text-[12.5px] leading-[17.5px] tracking-[-0.01em] text-white/85">{feature.body}</p>
      </div>
    </div>
  )
}
