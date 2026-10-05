import type { ReactNode } from 'react'
import { cn } from '../../../ui'

/** Pill-shaped tag; all visuals injected. */
export function Chip({ children, className }: { children: ReactNode; className?: string }) {
  return <span className={cn('inline-flex shrink-0 items-center justify-center rounded-full', className)}>{children}</span>
}

export interface ChipRowsProps {
  rows: string[][]
  chipClassName: string
  selected?: string
  selectedClassName?: string
  rowClassName?: string
  className?: string
}

/** Rows of chips laid out exactly as the reference wraps them. */
export function ChipRows({ rows, chipClassName, selected, selectedClassName, rowClassName, className }: ChipRowsProps) {
  return (
    <div className={className}>
      {rows.map((row) => (
        <div key={row.join()} className={cn('flex', rowClassName)}>
          {row.map((label) => (
            <Chip key={label} className={cn(chipClassName, label === selected && selectedClassName)}>
              {label}
            </Chip>
          ))}
        </div>
      ))}
    </div>
  )
}
