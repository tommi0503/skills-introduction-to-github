import type { CSSProperties } from 'react'
import { DataTable, type DataColumn } from '../../../ui'
import { autumn } from '../../shared-2829/theme'
import { schedule, type ProgramRow } from '../data'

const columns: DataColumn<ProgramRow>[] = [
  { key: 'time', header: schedule.headers.time, width: '33.3%', render: (r) => r.time },
  { key: 'program', header: schedule.headers.program, width: '33.4%', render: (r) => r.program },
  { key: 'place', header: schedule.headers.place, width: '33.3%', render: (r) => r.place },
]

const vars = {
  '--line': autumn.tableLine,
  '--head': autumn.tableHead,
  '--headText': autumn.headingBrown,
  '--body': autumn.tableBody,
  color: autumn.tableText,
} as CSSProperties

/** Program timetable: beige header, light rows separated by beige rules. */
export function ScheduleTable({ width }: { width: number }) {
  return (
    <div style={{ ...vars, width }}>
      <DataTable
        columns={columns}
        rows={schedule.rows}
        className="table-fixed"
        headCellClassName="h-[60px] p-0 text-[12.5px] font-bold border-x-[2px] first:border-l-0 last:border-r-0 border-[var(--line)]"
        cellClassName="h-[59.7px] p-0 text-[16.5px] border-t-[3px] border-x-[2px] first:border-l-0 last:border-r-0 border-[var(--line)]"
        headClassName="bg-[var(--head)] text-[var(--headText)]"
        rowClassName="bg-[var(--body)]"
      />
    </div>
  )
}
