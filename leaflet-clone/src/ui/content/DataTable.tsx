import type { ReactNode } from 'react'
import { cn } from '../core/cn'

export interface DataColumn<Row> {
  key: string
  header: ReactNode
  /** Width as CSS value (e.g. '30%', 80). */
  width?: string | number
  align?: 'left' | 'center' | 'right'
  render: (row: Row, rowIndex: number) => ReactNode
  cellClassName?: string
}

export interface DataTableProps<Row> {
  columns: DataColumn<Row>[]
  rows: Row[]
  className?: string
  headClassName?: string
  headCellClassName?: string
  rowClassName?: string | ((row: Row, index: number) => string)
  cellClassName?: string
  hideHeader?: boolean
}

/** Generic table: columns describe how to render each cell; all styling is injected. */
export function DataTable<Row>({
  columns,
  rows,
  className,
  headClassName,
  headCellClassName,
  rowClassName,
  cellClassName,
  hideHeader,
}: DataTableProps<Row>) {
  return (
    <table className={cn('w-full border-collapse', className)}>
      <colgroup>
        {columns.map((c) => (
          <col key={c.key} style={{ width: c.width }} />
        ))}
      </colgroup>
      {!hideHeader && (
        <thead className={headClassName}>
          <tr>
            {columns.map((c) => (
              <th key={c.key} className={cn('font-[inherit]', headCellClassName)} style={{ textAlign: c.align ?? 'center' }}>
                {c.header}
              </th>
            ))}
          </tr>
        </thead>
      )}
      <tbody>
        {rows.map((row, i) => (
          <tr key={i} className={typeof rowClassName === 'function' ? rowClassName(row, i) : rowClassName}>
            {columns.map((c) => (
              <td key={c.key} className={cn(cellClassName, c.cellClassName)} style={{ textAlign: c.align ?? 'center' }}>
                {c.render(row, i)}
              </td>
            ))}
          </tr>
        ))}
      </tbody>
    </table>
  )
}
