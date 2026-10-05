import { ImagePlaceholder, Panel, Pill, Placed } from '../../../ui'
import { programPanel as d, thumbs } from '../data'
import { theme } from '../theme'
import { OutlineBadge } from '../components/OutlineBadge'
import { Lines } from '../components/Lines'
import { Stamp } from '../components/Stamp'
import { InfoSection } from '../components/InfoSection'

const THUMB = 103

/** Panel 4 — welcome booth, thumbnails, keyword chips, schedule & contact. */
export function ProgramPanel() {
  return (
    <Panel background={theme.white}>
      <Placed x={47} y={72}>
        <OutlineBadge label={d.badge} className="border-[1.5px] border-[#2a2a2a] bg-white px-[15px]" />
      </Placed>
      <Placed x={47} y={116}>
        <Lines lines={d.intro} className="text-[21px] font-medium leading-[34px] tracking-[-0.03em] text-[#1e1e1e]" />
      </Placed>
      <Placed x={68} y={220} width={346} className="grid grid-cols-3 gap-x-[19px] gap-y-[26px]">
        {thumbs.map((t, i) =>
          t === 'photo' ? (
            <ImagePlaceholder key={i} label="market photo" className="rounded-full" style={{ width: THUMB, height: THUMB }} />
          ) : (
            <Stamp key={i} lines={d.stamp} size={THUMB} color={theme.sky} />
          ),
        )}
      </Placed>
      <Placed x={47} y={497} className="flex flex-col gap-[14px]">
        {d.chips.map((row) => (
          <div key={row[0]} className="flex gap-[9px]">
            {row.map((c) => (
              <Pill key={c} className="h-[40px] bg-[#a9c8e8] px-[19px] text-[20.5px] font-medium tracking-[-0.04em] text-[#1e1e1e]">
                <span>{c}</span>
              </Pill>
            ))}
          </div>
        ))}
      </Placed>
      <Placed x={47} y={642} className="flex flex-col gap-[34px]">
        {d.sections.map((s) => (
          <InfoSection key={s.title} {...s} highlightColor={theme.blueText} />
        ))}
      </Placed>
      <Placed x={62} y={914} className="flex items-center text-[16.5px] text-[#1e1e1e]">
        <span>{d.contacts[0]}</span>
        <span className="mx-[14px] h-[18px] w-px bg-[#cfcfcf]" />
        <span>{d.contacts[1]}</span>
      </Placed>
    </Panel>
  )
}
