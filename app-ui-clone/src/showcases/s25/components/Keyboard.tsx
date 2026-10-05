import type { CSSProperties, ReactNode } from 'react'
import { cn } from '../../../ui'
import type { KeySpec } from '../data'

export interface KeyboardProps {
  rows: KeySpec[][]
  /** Letter key width (pt). */
  keyWidth?: number
  keyHeight?: number
  /** Horizontal gap between keys (pt). */
  gap?: number
  /** Vertical gap between rows (pt). */
  rowGap?: number
  /** Left inset (pt). Letter-only rows are centred; rows with sized keys start at the inset. */
  inset?: number
  background?: string
  className?: string
  style?: CSSProperties
  /** Slot under the key rows (emoji / mic bar). */
  footer?: ReactNode
}

/** iOS-style software keyboard rendered from row data. */
export function Keyboard({
  rows,
  keyWidth = 31.5,
  keyHeight = 42,
  gap = 7.2,
  rowGap = 11.4,
  inset = 7.3,
  background = '#e0e1e3',
  className,
  style,
  footer,
}: KeyboardProps) {
  return (
    <div className={cn('rounded-t-[16px]', className)} style={{ background, paddingTop: 25, ...style }}>
      <div className="flex flex-col" style={{ gap: rowGap }}>
        {rows.map((row, r) => {
          const sized = row.some((k) => k.width)
          return (
            <div
              key={r}
              className={cn('flex', sized ? 'justify-start' : 'justify-center')}
              style={{ gap, paddingLeft: inset, paddingRight: inset }}
            >
              {row.map((k, i) => (
                <Key key={i} spec={k} width={k.width ?? keyWidth} height={keyHeight} />
              ))}
            </div>
          )
        })}
      </div>
      {footer}
    </div>
  )
}

function Key({ spec, width, height }: { spec: KeySpec; width: number; height: number }) {
  const Icon = spec.icon
  const isWord = (spec.label?.length ?? 0) > 1
  return (
    <div
      className="flex shrink-0 items-center justify-center rounded-[7px] bg-white text-black"
      style={{
        width,
        height,
        marginLeft: spec.offset,
        boxShadow: '0 1px 0 rgba(0,0,0,0.28)',
        fontSize: isWord ? 16 : 22,
        lineHeight: 1,
        paddingBottom: isWord ? 0 : 2,
      }}
    >
      {Icon ? <Icon size={22} strokeWidth={1.6} /> : spec.label}
    </div>
  )
}
