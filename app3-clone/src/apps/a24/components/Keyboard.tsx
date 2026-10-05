import { ArrowBigUp, Delete, CornerDownLeft, Globe, Mic, Smile } from 'lucide-react'
import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export type KeyIcon = 'shift' | 'shiftOn' | 'delete' | 'return' | 'emoji'

export interface KeySpec {
  label?: string
  icon?: KeyIcon
  /** Key width in px. */
  w: number
  /** Gap before this key (defaults to the row gap). */
  gap?: number
  /** Smaller font for function labels like "123". */
  small?: boolean
}

export interface KeyRow {
  left: number
  keys: KeySpec[]
}

export interface KeyboardLayout {
  rows: KeyRow[]
  rowTop: number[]
  keyHeight: number
  gap: number
  /** Icons in the bottom accessory bar. */
  bottomLeft: 'globe' | 'emoji'
}

const ICONS: Record<KeyIcon, ReactNode> = {
  shift: <ArrowBigUp size={24} strokeWidth={1.6} />,
  shiftOn: <ArrowBigUp size={24} strokeWidth={1.6} fill="#000" />,
  delete: <Delete size={22} strokeWidth={1.6} />,
  return: <CornerDownLeft size={22} strokeWidth={1.6} />,
  emoji: <Smile size={22} strokeWidth={1.6} />,
}

export interface KeyboardProps {
  layout: KeyboardLayout
  background?: string
  className?: string
}

/** iOS (26) software keyboard rendered from row data; positioned by its parent (height to screen bottom). */
export function Keyboard({ layout, background = '#e4e4e7', className }: KeyboardProps) {
  const BottomLeft = layout.bottomLeft === 'globe' ? Globe : Smile
  return (
    <div className={cn('absolute inset-x-0 bottom-0 rounded-t-[26px] font-inter text-black', className)} style={{ background }}>
      {layout.rows.map((row, ri) => {
        let x = row.left
        return row.keys.map((k, ki) => {
          if (ki > 0) x += k.gap ?? layout.gap
          const left = x
          x += k.w
          return (
            <div
              key={`${ri}-${ki}`}
              className="absolute flex items-center justify-center rounded-[8px] bg-white"
              style={{ left, top: layout.rowTop[ri], width: k.w, height: layout.keyHeight, boxShadow: '0 1px 0 rgba(0,0,0,.08)' }}
            >
              {k.icon ? ICONS[k.icon] : <span className={k.small ? 'text-[16px]' : 'text-[21.5px] font-light leading-none'}>{k.label}</span>}
            </div>
          )
        })
      })}
      <BottomLeft className="absolute left-[29px] bottom-[24px]" size={26} strokeWidth={1.5} />
      <Mic className="absolute right-[32px] bottom-[23px]" size={26} strokeWidth={1.5} />
    </div>
  )
}
