import { DataTable, type DataColumn } from '../../../ui'
import type { FareRow } from '../cruise/content'

export interface FareTableProps {
  rows: readonly FareRow[]
  columns: { type: string; adult: string; youth: string; child: string }
  /** Column widths in px / CSS, in order type, adult, youth, child. */
  widths?: Array<number | string>
  /** Joins multi-line type labels with a space instead of breaking. */
  inlineType?: boolean
  className?: string
  headClassName?: string
  headCellClassName?: string
  rowClassName?: string
  cellClassName?: string
  typeCellClassName?: string
  valueCellClassName?: string
}

/** 크루즈 운항 요금 table; all visual styling injected by the leaflet. */
export function FareTable({
  rows,
  columns,
  widths = [],
  inlineType,
  typeCellClassName,
  valueCellClassName,
  ...style
}: FareTableProps) {
  const valueKeys = ['adult', 'youth', 'child'] as const
  const cols: DataColumn<FareRow>[] = [
    {
      key: 'type',
      header: columns.type,
      width: widths[0],
      cellClassName: typeCellClassName,
      render: (r) => (inlineType ? r.type.join(' ') : r.type.map((t) => <div key={t}>{t}</div>)),
    },
    ...valueKeys.map((k, i) => ({
      key: k,
      header: columns[k],
      width: widths[i + 1],
      cellClassName: valueCellClassName,
      render: (r: FareRow) => r[k],
    })),
  ]
  return <DataTable columns={cols} rows={rows as FareRow[]} {...style} />
}
