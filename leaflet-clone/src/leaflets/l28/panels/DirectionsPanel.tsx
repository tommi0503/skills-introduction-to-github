import { Bus, TrainFront } from 'lucide-react'
import { Panel, Placed } from '../../../ui'
import { LeafHeading } from '../../shared-2829/components/LeafHeading'
import { TaggedRow } from '../../shared-2829/components/TaggedRow'
import { autumn, fonts } from '../../shared-2829/theme'
import { RoadMap } from '../components/RoadMap'
import { TransitLine } from '../components/TransitLine'
import { colors, directions } from '../data'

const transitIcons = { bus: Bus, subway: TrainFront }

/** Panel 2 — how to get there, shuttle/parking info and credits. */
export function DirectionsPanel() {
  return (
    <Panel>
      <Placed x={57} y={100}>
        <LeafHeading title={directions.title} />
      </Placed>
      <RoadMap />
      <Placed x={57} y={423}>
        <LeafHeading />
      </Placed>
      <Placed x={82} y={482} className="flex flex-col gap-[20px]" style={{ color: autumn.rowText }}>
        {directions.transit.map((t, i) => (
          <TransitLine key={i} icon={transitIcons[t.icon]} iconColor={autumn.teal} lines={t.lines} />
        ))}
      </Placed>
      <Placed x={84} y={602} className="flex flex-col gap-[19px]" style={{ color: autumn.rowText }}>
        {directions.rows.map((r) => (
          <TaggedRow
            key={r.tag}
            tag={r.tag}
            lines={r.lines}
            color={colors.tag}
            className="items-start gap-[23px]"
            textClassName="-mt-[2px] text-[14.5px] font-medium leading-[23.5px] tracking-[-0.3px] whitespace-nowrap"
          />
        ))}
      </Placed>
      <Placed x={62} y={852} className="flex flex-col gap-[10px]">
        {directions.credits.map((c) => (
          <div key={c.label} className="flex">
            <span className={`w-[103px] shrink-0 text-[18px] leading-[26px] ${fonts.heading}`} style={{ color: autumn.sponsorLabel }}>
              {c.label}
            </span>
            <div className="text-[14.5px] font-medium leading-[23px] tracking-[-0.3px]" style={{ color: autumn.sponsorText }}>
              {c.lines.map((l, i) => (
                <p key={i} className="m-0 whitespace-nowrap">
                  {l}
                </p>
              ))}
            </div>
          </div>
        ))}
      </Placed>
    </Panel>
  )
}
