import { Divider, ImagePlaceholder, Panel, Placed } from '../../../ui'
import { RoundedBox } from '../../shared-1718/components/RoundedBox'
import { outsidePalette as c } from '../../shared-1718/theme'
import { timetable } from '../data'
import { TimetableItem } from '../components/TimetableItem'

/** Middle outer panel: outlined card with the programme timetable. */
export function TimetablePanel() {
  return (
    <Panel background={c.cream}>
      <RoundedBox x={54} y={74} width={375} height={842} radius={12} background={c.card} borderColor={c.cardBorder}>
        <p className="absolute left-0 right-0 m-0 text-center text-[21.5px] font-bold" style={{ top: 45, color: c.accent }}>
          {timetable.title}
        </p>
        <div className="absolute flex flex-col" style={{ left: 21, right: 21, top: 122 }}>
          {timetable.entries.map((entry, i) => (
            <div key={entry.title}>
              {i > 0 && <Divider color={c.rule} className="mb-[21px] mt-[18px]" />}
              <TimetableItem
                entry={entry}
                titleClassName="text-[17px] font-bold leading-[30px] mb-[5px]"
                lineClassName="text-[15px] leading-[22px]"
                titleColor={c.ink}
                lineColor={c.inkSoft}
              />
            </div>
          ))}
        </div>
      </RoundedBox>
      <ImagePlaceholder label="books icon" className="absolute" style={{ left: 330, top: 848, width: 82, height: 82 }} />
      <Placed x={0} y={946} width={480} className="text-center text-[14px]" style={{ color: c.inkMuted }}>
        {timetable.website}
      </Placed>
    </Panel>
  )
}
