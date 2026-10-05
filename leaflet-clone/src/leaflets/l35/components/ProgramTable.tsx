import { DataTable, type DataColumn } from '../../../ui'
import { larana } from '../../shared-3435/theme'
import type { ProgramRow } from '../data'

export interface ProgramTableProps {
  headers: { program: string; target: string; main: string }
  rows: ProgramRow[]
  className?: string
}

/** Blue-headed 3-column checkup table; the last column may carry a smaller sub line. */
export function ProgramTable({ headers, rows, className }: ProgramTableProps) {
  const columns: DataColumn<ProgramRow>[] = [
    { key: 'program', header: headers.program, width: 132, render: (r) => <span className="font-bold">{r.program}</span> },
    { key: 'target', header: headers.target, width: 115, render: (r) => r.target },
    {
      key: 'main',
      header: headers.main,
      render: (r) => (
        <span className="flex flex-col items-center">
          <span className={r.sub ? 'font-bold' : 'whitespace-pre-line'}>{r.main}</span>
          {r.sub && <span className="text-[12.5px] leading-[20px]" style={{ color: larana.inkSoft }}>{r.sub}</span>}
        </span>
      ),
    },
  ]
  return (
    <div className={className} style={{ background: '#f5f6f9' }}>
      <DataTable
        columns={columns}
        rows={rows}
        className="text-[14.5px] leading-[22px]"
        headClassName="text-white"
        headCellClassName="h-[48px] p-0 text-[15px] font-bold bg-[#4a7de8]"
        rowClassName="border-t border-[#e2e5ec] first:border-t-0"
        cellClassName="h-[66.5px] p-0"
      />
    </div>
  )
}
