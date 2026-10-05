import { ImagePlaceholder } from '../../../ui'
import { feature } from '../data'
import { theme } from '../theme'

/** Sticky copy column + stacked product panels. */
export function Feature() {
  return (
    <>
      <div className="absolute left-[33px] top-[2062px] w-[440px] text-[#e9ebdf]">
        <h3 className="m-0 font-inter text-[48px] leading-[50.4px] font-light tracking-[-1.6px]">{feature.title}</h3>
        <p className="m-0 mt-[16px] w-[380px] font-geist text-[16px] leading-[24px] tracking-[0.75px]">{feature.body}</p>
        <a className="mt-[18px] inline-block font-geist text-[16px] leading-[21px] tracking-[0.75px] underline underline-offset-4">{feature.link}</a>
      </div>
      {feature.panels.map((y) => (
        <ImagePlaceholder
          key={y}
          label="Product panel"
          tone={theme.tones.panel}
          className="absolute left-[633px] h-[760px] w-[760px] rounded-[16px]"
          style={{ top: y }}
        />
      ))}
    </>
  )
}
