import type { ReactNode } from 'react'
import { KeyValueList } from '../../../ui'

export interface LabeledRow {
  label: string
  value: ReactNode
}

export interface LabeledRowsProps {
  rows: LabeledRow[]
  labelWidth: number
  className?: string
  rowClassName?: string
  labelClassName?: string
  valueClassName?: string
  /** Spread the label's letters across the label width (e.g. "주 차"). */
  renderLabel?: (row: LabeledRow) => ReactNode
}

/** Thin adapter over KeyValueList for `{label, value}` data. */
export function LabeledRows({ rows, renderLabel, ...rest }: LabeledRowsProps) {
  return (
    <KeyValueList
      items={rows.map((r) => ({ key: r.label, label: r.label, value: r.value }))}
      renderLabel={renderLabel ? (item) => renderLabel({ label: item.key, value: item.value }) : undefined}
      {...rest}
    />
  )
}
