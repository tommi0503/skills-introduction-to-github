import { Grip } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import type { SplitFeature as SplitFeatureData } from '../data'
import { colors, fonts } from '../theme'
import { Text } from '../components/primitives'

export interface SplitFeatureProps {
  data: SplitFeatureData
  height: number
  /** Top of the media block, relative to the section. */
  mediaTop: number
  /** Top of the text column, relative to the section. */
  textTop: number
}

/** Two-column feature: copy beside a framed illustration (placeholder). */
export function SplitFeature({ data, height, mediaTop, textTop }: SplitFeatureProps) {
  const mediaLeft = data.mediaSide === 'right'
  return (
    <section className={`relative ${fonts.sans}`} style={{ height }}>
      <ImagePlaceholder
        label="feature illustration"
        className="absolute rounded-[16px]"
        style={{ top: mediaTop, left: mediaLeft ? 733 : 140, width: 567, height: 341 }}
      />
      <div className="absolute w-[529px]" style={{ top: textTop, left: mediaLeft ? 140 : 771 }}>
        {data.badge && (
          <div
            className="mb-[16px] ml-[7px] inline-flex h-[32px] items-center rounded-full border pl-[4px] pr-[8px]"
            style={{ background: colors.subtle, borderColor: '#f2f2f1' }}
          >
            <span className="rounded-full px-[7px] text-[12px] leading-[19.2px] font-semibold text-white" style={{ background: colors.orange }}>
              {data.badge.label}
            </span>
            <span className={`ml-[7px] text-[14px] leading-[18.2px] font-semibold tracking-[-0.28px] ${fonts.mono}`} style={{ color: colors.orange }}>
              {data.badge.value}
            </span>
            <Grip className="ml-[4px]" size={10} color="#e0a582" />
          </div>
        )}
        <Text role="h2" as="h2" className={data.badge ? '' : 'pr-[10px]'}>
          {data.title}
        </Text>
        <Text role="lead" className="mt-[16px] pr-[10px]">
          {data.text}
        </Text>
      </div>
    </section>
  )
}
