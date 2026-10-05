import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { library } from '../../shared-2425/theme'
import { FramedPill } from '../../shared-2425/components/FramedPill'
import { ArcText } from '../components/ArcText'
import { OutlinedTitle } from '../components/OutlinedTitle'
import { cover } from '../data'
import { layout, panelBg } from '../theme'

const L = layout.cover

/** Panel 3 — cover: arc slogan, outlined display title, slogan pill. */
export function CoverPanel() {
  return (
    <Panel background={panelBg.cover}>
      <Placed x={135} y={L.arcY}>
        <ArcText text={cover.arc} width={210} height={40} rise={36} color={library.title} className="font-dohyeon text-[25px]" />
      </Placed>
      <Placed x={219} y={150} width={46} height={56}>
        <ImagePlaceholder label="globe with graduation cap" className="h-full w-full rounded-full" />
      </Placed>
      <Placed x={0} y={L.titleY} width={480} className="flex flex-col items-center font-blackhan text-[68px] leading-[73px] tracking-[-0.01em] [word-spacing:-8px]">
        <OutlinedTitle text={cover.title[0]} fill="#f2d978" stroke={library.ink} halo="#ffffff" />
        <OutlinedTitle text={cover.title[1]} fill="#ffffff" stroke={library.ink} halo="#ffffff" />
      </Placed>
      <Placed x={67} y={L.sloganY}>
        <FramedPill fill={library.yellow} width={350} height={56} borderWidth={2.5} className="text-[19.5px] font-bold tracking-[-0.03em]" style={{ color: library.title }}>
          {cover.slogan}
        </FramedPill>
      </Placed>
      <Placed x={0} y={L.centerY} width={480} className="text-center font-montserrat text-[15.5px] font-bold leading-none tracking-[0.02em] text-[#2c3049]">
        {cover.center}
      </Placed>
    </Panel>
  )
}
