import type { CSSProperties } from 'react'
import { DataTable, type DataColumn } from '../../../ui'
import { larana } from '../../shared-3435/theme'
import type { HoursRow } from '../data'

const columns: DataColumn<HoursRow>[] = [
  {
    key: 'day',
    header: '',
    width: 116,
    render: (r) => <span className="whitespace-pre font-bold">{r.day}</span>,
    cellClassName: 'bg-[var(--hours-tint)]',
  },
  { key: 'time', header: '', align: 'left', render: (r) => r.time, cellClassName: 'pl-[16px] border-l border-[var(--hours-line)]' },
]

export interface HoursTableProps {
  rows: HoursRow[]
  className?: string
}

/** Two-column opening-hours table: tinted label column, thin-ruled time column. */
export function HoursTable({ rows, className }: HoursTableProps) {
  const vars = { '--hours-tint': larana.cellTint, '--hours-line': larana.line, color: larana.ink } as CSSProperties
  return (
    <div className={className} style={{ ...vars, border: `1.5px solid ${larana.line}` }}>
      <DataTable
        columns={columns}
        rows={rows}
        hideHeader
        className="text-[17px]"
        cellClassName="h-[44px] p-0"
        rowClassName="border-b-[1.5px] border-[var(--hours-line)] last:border-b-0"
      />
    </div>
  )
}
