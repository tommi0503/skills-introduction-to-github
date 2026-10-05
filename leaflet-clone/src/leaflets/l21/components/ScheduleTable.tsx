import { DataTable, type DataColumn } from '../../../ui'
import type { CourseRow, CourseSession } from '../data'

export interface ScheduleTableProps {
  title: string
  rows: CourseRow[]
}

function SessionCell({ s }: { s: CourseSession }) {
  return (
    <div className="flex flex-col items-center">
      <span className="text-[17.5px] font-medium leading-[20px] tracking-[-0.02em] text-[#4f5359]">{s.period}</span>
      <span className="mt-[2px] text-[10.5px] font-medium leading-[12px] tracking-[-0.04em] text-[#6b6f75]">{s.deadline}</span>
    </div>
  )
}

/** 강좌 × 회차 timetable with a pale-blue caption bar. */
export function ScheduleTable({ title, rows }: ScheduleTableProps) {
  const sessionCount = rows[0]?.sessions.length ?? 0
  const columns: DataColumn<CourseRow>[] = [
    {
      key: 'name',
      header: null,
      width: 115,
      render: (r) => <span className="text-[15.5px] font-medium tracking-[-0.03em] text-[#5a5e64]">{r.name}</span>,
    },
    ...Array.from({ length: sessionCount }, (_, i) => ({
      key: `s${i}`,
      header: null,
      render: (r: CourseRow) => <SessionCell s={r.sessions[i]} />,
      cellClassName: 'border-l-2 border-[#c3d4e7]',
    })),
  ]
  return (
    <div className="flex flex-col">
      <div className="flex h-[45px] items-center justify-center border-b-2 border-[#c3d4e7] bg-[#d5e3f1] text-[19px] font-bold tracking-[-0.03em] text-[#2f4f78]">
        {title}
      </div>
      <DataTable
        columns={columns}
        rows={rows}
        hideHeader
        className="table-fixed"
        rowClassName="h-[54px] border-b-2 border-[#c3d4e7]"
        cellClassName="p-0 align-middle"
      />
    </div>
  )
}
