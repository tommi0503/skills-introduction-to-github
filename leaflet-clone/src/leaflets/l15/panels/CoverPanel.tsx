import { Panel, Placed } from '../../../ui'
import { Lines } from '../../shared-1516/components/Lines'
import { Ornament } from '../../shared-1516/components/Ornament'
import { concertTheme as t } from '../../shared-1516/theme'
import { cover as d } from '../data'

const ornament = { width: 246, flourishWidth: 118, flourishHeight: 16, lineColor: '#c9b29a' }

/** Front cover: edition, ornamented title, date/venue and credits. */
export function CoverPanel() {
  return (
    <Panel background={t.burgundy} className="text-center" style={{ color: t.onDark }}>
      <Placed x={0} y={36} width={480} className="text-[12px]" style={{ color: t.onDarkMuted }}>
        {d.edition}
      </Placed>
      <Placed x={125} y={237}>
        <Ornament {...ornament} />
      </Placed>
      <Placed x={0} y={275} width={480}>
        <Lines lines={d.titleLines} className={`${t.font.title} text-[66px] leading-[72px] text-[#e8dcc0]`} />
      </Placed>
      <Placed x={125} y={446}>
        <Ornament {...ornament} />
      </Placed>
      <Placed x={0} y={642} width={480} className="text-[20px] font-semibold leading-[28px]">
        {d.date}
      </Placed>
      <Placed x={0} y={689} width={480} className="text-[16px] leading-[22px]" style={{ color: t.onDarkMuted }}>
        {d.venue}
      </Placed>
      <Placed x={99} y={962} className="flex gap-[42px] text-[12.5px] leading-[18px]">
        {d.credits.map((c) => (
          <span key={c.label} style={{ color: t.onDarkMuted }}>
            <b className="mr-[7px] font-bold" style={{ color: t.onDark }}>
              {c.label}
            </b>
            {c.value}
          </span>
        ))}
      </Placed>
    </Panel>
  )
}
