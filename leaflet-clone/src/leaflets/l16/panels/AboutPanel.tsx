import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { EyebrowHeading } from '../../shared-1516/components/EyebrowHeading'
import { Lines } from '../../shared-1516/components/Lines'
import { concertTheme as t } from '../../shared-1516/theme'
import { about as d } from '../data'

/** Inside left panel: concert introduction and a photo filling the lower half. */
export function AboutPanel() {
  return (
    <Panel background={t.burgundy} style={{ color: t.onDarkMuted }}>
      <Placed x={68} y={79}>
        <EyebrowHeading eyebrow={d.eyebrow} title={d.title} eyebrowColor={t.onDark} titleColor={t.onDark} />
      </Placed>
      <Placed x={68} y={186} width={390}>
        <div className={`${t.font.display} text-[19px] leading-[26px] tracking-[0.04em]`} style={{ color: t.onDark }}>
          {d.lead}
        </div>
        <div className="mt-[6px] text-[13.5px] leading-[20px]">{d.sub}</div>
        <div className="mt-[41px] flex flex-col gap-[42px]">
          {d.paragraphs.map((p) => (
            <Lines key={p[0]} lines={p} className="text-[14px] leading-[24px] tracking-[-0.005em]" />
          ))}
        </div>
      </Placed>
      <ImagePlaceholder className="absolute inset-x-0 bottom-0" style={{ top: 553 }} tone="#c9ccd1" label="cello photo" />
    </Panel>
  )
}
