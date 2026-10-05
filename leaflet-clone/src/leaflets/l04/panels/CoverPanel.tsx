import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { DottedText } from '../../shared-0407/components/DottedText'
import { NotchedFrame } from '../../shared-0407/components/NotchedFrame'
import { TextLines } from '../../shared-0407/components/TextLines'
import { content, taglineDots } from '../data'
import { theme } from '../theme'

const BOX = { x: 52, y: 265, width: 376, height: 398, gap: 9 }

/** Front cover: sea photo, tagline, swirl art and the double-framed title block. */
export function CoverPanel() {
  return (
    <Panel style={{ color: theme.ink }}>
      <ImagePlaceholder label="sea and cruise ship photo" tone={theme.photoTone} className="absolute inset-0" />
      <Placed x={0} y={34} width={480} className="text-center font-noto-sans text-[19px] font-bold leading-[28px] tracking-[0.28em]">
        <DottedText text={content.tagline} dotted={taglineDots} dotSize={4} dotOffset={1} />
      </Placed>
      <ImagePlaceholder label="swirl line art" className="absolute" style={{ left: 0, top: 84, width: 258, height: 154 }} />
      <Placed x={BOX.x} y={BOX.y}>
        <NotchedFrame width={BOX.width} height={BOX.height} notch={20} color={theme.ink} strokeWidth={2} />
      </Placed>
      <Placed x={BOX.x + BOX.gap} y={BOX.y + BOX.gap}>
        <NotchedFrame width={BOX.width - BOX.gap * 2} height={BOX.height - BOX.gap * 2} notch={15} color={theme.ink} strokeWidth={1.5} />
      </Placed>
      <TextLines
        className="absolute inset-x-0 text-center font-hahmlet font-bold text-[84px] tracking-[-0.02em]"
        style={{ top: 303 }}
        lines={content.title}
        lineClassName="leading-[92px]"
      />
      <Placed x={0} y={505} width={480} className="text-center font-noto-sans text-[29px] font-medium leading-[40px] tracking-[0.3em] indent-[0.3em]">
        {content.subtitle}
      </Placed>
      <TextLines
        className="absolute inset-x-0 text-center font-noto-sans text-[19px] font-bold"
        style={{ top: 570 }}
        lines={content.english}
        lineClassName="leading-[27px]"
      />
    </Panel>
  )
}
