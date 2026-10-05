import { ChevronLeft, TextAlignStart } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { FeatureLine } from '../components/FeatureLine'
import { PillButton } from '../components/PillButton'
import { PriceTag } from '../components/PriceTag'
import { SoftCircleButton } from '../components/SoftCircleButton'
import { artworkScreen as d } from '../data'

/** Hanging wire from the pin to both top corners of the frame. */
function HangingWire() {
  return (
    <svg className="absolute top-[262px] left-[84px]" width="222" height="44" viewBox="0 0 222 44" fill="none">
      <path d="M0 43 L112 1 L222 43" stroke="#d2d2d2" strokeWidth="1.2" />
    </svg>
  )
}

export function ArtworkScreen() {
  return (
    <div className="absolute inset-0">
      <div className="absolute top-[51px] right-[20px] left-[19px] flex justify-between">
        <SoftCircleButton icon={ChevronLeft} />
        <SoftCircleButton icon={TextAlignStart} iconSize={20} />
      </div>

      <div className="absolute top-[111px] right-0 left-0 text-center text-[49.5px] leading-[51px] font-semibold text-[#111]">
        {d.name.map((line) => (
          <div key={line}>{line}</div>
        ))}
      </div>
      <div className="absolute top-[223px] right-0 left-0 text-center text-[13px] text-[#8a8a8a]">{d.meta}</div>

      <HangingWire />
      <span className="absolute top-[258px] left-[192px] h-[8px] w-[9px] rounded-full bg-[#c4161c]" />

      <ImagePlaceholder
        className="absolute top-[307px] left-[68px] h-[322px] w-[248px]"
        style={{ boxShadow: '14px 18px 24px rgba(0,0,0,0.16)' }}
        label="framed portrait"
      />
      <div className="absolute top-[300px] left-[228px]">
        <PriceTag label={d.price} />
      </div>

      <div className="absolute top-[648px] right-0 left-0 flex flex-col gap-[8px]">
        {d.features.map((f) => (
          <FeatureLine key={f.key} icon={f.icon} label={f.label} />
        ))}
      </div>
      <div className="absolute top-[699px] right-0 left-0 text-center text-[7.4px] leading-[13px] text-[#7a7a7a]">
        {d.specs.map((s) => (
          <div key={s}>{s}</div>
        ))}
      </div>

      <PillButton label={d.cta} variant="solid" className="absolute top-[749px] left-[85px] h-[49px] w-[220px] text-[21px] font-normal" />
    </div>
  )
}
