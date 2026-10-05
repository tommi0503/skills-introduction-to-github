import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { TextLines } from '../../shared-0407/components/TextLines'
import { cover } from '../data'
import { theme } from '../theme'

/** Front cover: tagline, island art + clouds, vertical two-tone title and opening hours. */
export function CoverPanel() {
  const titleClass = 'absolute font-pretendard text-[70px] font-black'
  return (
    <Panel style={{ color: theme.olive }}>
      <Placed x={57} y={78} className="whitespace-nowrap font-pretendard text-[22px] font-extrabold leading-[30px] tracking-[0.1em]">
        {cover.tagline}
      </Placed>
      {cover.art.map((a, i) => (
        <ImagePlaceholder key={i} label={a.label} className="absolute" style={a.style} />
      ))}
      <TextLines className={titleClass} style={{ left: 48, top: 726, color: theme.onField }} lines={cover.columns.light} lineClassName="leading-[78px]" />
      <TextLines className={titleClass} style={{ left: 136, top: 726 }} lines={cover.columns.dark} lineClassName="leading-[78px]" />
      <TextLines className="absolute font-pretendard text-[17px] font-extrabold" style={{ left: 262, top: 871 }} lines={cover.hours} lineClassName="leading-[28px]" />
    </Panel>
  )
}
