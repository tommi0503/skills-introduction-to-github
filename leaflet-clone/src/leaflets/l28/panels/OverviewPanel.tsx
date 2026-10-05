import { Panel, Placed } from '../../../ui'
import { LeafHeading } from '../../shared-2829/components/LeafHeading'
import { TaggedRow } from '../../shared-2829/components/TaggedRow'
import { autumn, fonts } from '../../shared-2829/theme'
import { BoothMap } from '../components/BoothMap'
import { boothMap, colors, overview } from '../data'

/** Panel 1 — festival introduction, key facts and booth layout. */
export function OverviewPanel() {
  return (
    <Panel>
      <Placed x={133} y={55}>
        <p className={`m-0 text-[24px] leading-none tracking-[-0.5px] ${fonts.heading}`} style={{ color: autumn.oliveText }}>
          {overview.kicker}
        </p>
      </Placed>
      <Placed x={78} y={100}>
        <LeafHeading title={overview.title} />
      </Placed>
      <Placed x={88} y={158} width={345}>
        <div className="text-[13px] font-medium leading-[23.3px] tracking-[-0.3px]" style={{ color: autumn.body }}>
          {overview.paragraph.map((l, i) => (
            <p key={i} className="m-0 whitespace-nowrap">
              {l}
            </p>
          ))}
        </div>
      </Placed>
      <Placed x={80} y={298} width={360} className="flex flex-col gap-[22px]">
        {overview.rows.map((r) => (
          <TaggedRow
            key={r.tag}
            tag={r.tag}
            lines={r.lines}
            color={colors.pill}
            className="min-h-[38px] items-center gap-[23px]"
            textClassName="text-[15px] font-medium leading-[23px] tracking-[-0.3px]"
            style={{ color: autumn.rowText }}
          />
        ))}
      </Placed>
      <Placed x={70} y={593}>
        <LeafHeading title={boothMap.title} />
      </Placed>
      <Placed x={70} y={658}>
        <BoothMap />
      </Placed>
    </Panel>
  )
}
