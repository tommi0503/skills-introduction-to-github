import { ImagePlaceholder } from '../../../ui'
import { FadeText } from '../components/FadeText'
import { PillButton } from '../components/PillButton'
import { museumScreen as d } from '../data'
import { theme } from '../theme'

export function MuseumScreen() {
  return (
    <div className="absolute inset-0">
      <div
        className="absolute top-[50px] left-[64px] h-[41px] w-[265px]"
        style={{ background: 'linear-gradient(90deg, rgba(240,240,240,0), #f0f0f0 25%, #f0f0f0 75%, rgba(240,240,240,0))' }}
      />
      <div className="absolute top-[56px] right-0 left-0 text-center">
        <FadeText
          gradient="linear-gradient(90deg, #c8c8c8 0%, #b4b4b4 17%, #111 31%, #111 76%, #c4c4c4 100%)"
          className="text-[21px] leading-[28px] font-medium"
        >
          {d.venue}
        </FadeText>
      </div>

      <ImagePlaceholder className="absolute top-[177px] left-[40px] h-[383px] w-[258px] rounded-[48px]" label="marble statue" />

      <div className="absolute top-[581px] left-[20px] text-[49px] leading-[51px] font-semibold tracking-[-0.3px] text-[#111]">
        {d.headline.line1}
        <br />
        <span className="font-normal" style={{ color: theme.faint }}>
          {d.headline.faded}
        </span>{' '}
        {d.headline.rest}
      </div>
      <div className="absolute top-[698px] left-[19px] text-[12.8px] tracking-[-0.1px] text-[#6c6c6c]">{d.subtitle}</div>

      <div className="absolute top-[749px] right-[18px] left-[19px] flex gap-[9px]">
        {d.actions.map((a) => (
          <PillButton key={a.key} label={a.label} variant={a.variant} className="h-[48px] flex-1 text-[21.5px] font-medium" />
        ))}
      </div>
    </div>
  )
}
