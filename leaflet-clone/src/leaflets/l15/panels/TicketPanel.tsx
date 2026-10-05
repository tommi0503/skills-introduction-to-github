import { DataTable, Panel, Pill, Placed } from '../../../ui'
import { EyebrowHeading } from '../../shared-1516/components/EyebrowHeading'
import { LabeledRows } from '../../shared-1516/components/LabeledRows'
import { concertTheme as t } from '../../shared-1516/theme'
import { VenueMap } from '../components/VenueMap'
import { ticket as d, type TicketRow } from '../data'

const columns = (['seat', 'price', 'note'] as const).map((key) => ({
  key,
  header: d.columns[key],
  width: '33.33%',
  render: (row: TicketRow) => row[key],
  cellClassName: key === 'seat' ? 'font-bold' : undefined,
}))

const subTitle = 'text-[20px] font-bold leading-none'

/** Middle outside panel: ticket prices, how to buy and directions. */
export function TicketPanel() {
  return (
    <Panel background={t.paper} style={{ color: t.body }}>
      <Placed x={41} y={55}>
        <EyebrowHeading eyebrow={d.eyebrow} title={d.title} eyebrowColor="#5a4a4a" titleColor={t.heading} />
      </Placed>

      <Placed x={34} y={144} width={412}>
        <DataTable
          columns={columns}
          rows={d.rows}
          headClassName="text-[16px]"
          headCellClassName="h-[43px] p-0 font-semibold text-[#f1e3e3]"
          rowClassName="h-[43px]"
          cellClassName="p-0 text-[16.5px] border-b-2 border-[#e6ddcc] text-[#4a4040]"
          className="[&_thead]:bg-[#673a4b]"
        />
      </Placed>
      <Placed x={70} y={331} className="text-[12.5px] text-[#555]">
        {d.footnote}
      </Placed>

      <Placed x={70} y={403} className={subTitle} style={{ color: t.heading }}>
        {d.purchaseTitle}
      </Placed>
      <Placed x={68} y={448} className="flex flex-col gap-[15.5px]">
        {d.purchase.map((p) => (
          <div key={p.label} className="flex items-center">
            <Pill className="h-[44px] w-[106px] bg-[#5a2427] text-[16px] font-medium text-[#f3e6e0]">
              <span>{p.label}</span>
            </Pill>
            <span className="ml-[20px] text-[15px] text-[#4a4040]">{p.value}</span>
          </div>
        ))}
      </Placed>

      <Placed x={71} y={661} className={subTitle} style={{ color: t.heading }}>
        {d.mapTitle}
      </Placed>
      <Placed x={56} y={702}>
        <VenueMap title={d.venueLabel} width={370} height={215} />
      </Placed>

      <Placed x={87} y={934} width={380}>
        <LabeledRows
          rows={d.access}
          labelWidth={54}
          className="gap-[9px]"
          rowClassName="leading-[20px]"
          labelClassName="text-[15px] font-bold text-[#3f3434]"
          valueClassName="text-[15px] text-[#4a4040]"
          renderLabel={(r) =>
            r.label.includes(' ') ? (
              <span className="flex w-[44px] justify-between">
                {r.label.split(' ').map((c) => (
                  <span key={c}>{c}</span>
                ))}
              </span>
            ) : (
              r.label
            )
          }
        />
      </Placed>
    </Panel>
  )
}
