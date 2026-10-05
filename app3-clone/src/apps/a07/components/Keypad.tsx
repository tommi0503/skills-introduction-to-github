import { Delete } from 'lucide-react'
import { cn } from '../../../ui'
import type { KeyDef } from '../data'

export interface KeypadProps {
  keys: KeyDef[]
  columns?: number
  keyHeight?: number
  gap?: number
  keyColor?: string
  textColor?: string
  className?: string
}

/** Reusable iOS-style numeric keypad (digits + letters, bare decimal/delete keys). */
export function Keypad({
  keys,
  columns = 3,
  keyHeight = 46,
  gap = 7,
  keyColor = '#6b6b6d',
  textColor = '#fff',
  className,
}: KeypadProps) {
  return (
    <div className={cn('grid', className)} style={{ gridTemplateColumns: `repeat(${columns}, 1fr)`, gap, color: textColor }}>
      {keys.map((k) => (
        <div
          key={k.key}
          className="flex flex-col items-center justify-center rounded-[5px]"
          style={{ height: keyHeight, background: k.bare ? 'transparent' : keyColor }}
        >
          {k.kind === 'delete' ? (
            <Delete size={22} strokeWidth={1.6} />
          ) : (
            <>
              <span className={cn('leading-[24px]', k.kind === 'decimal' ? 'text-[18px]' : 'text-[24px]')}>{k.digit}</span>
              {k.letters && <span className="text-[8.5px] leading-[11px] font-semibold tracking-[2.2px]">{k.letters}</span>}
            </>
          )}
        </div>
      ))}
    </div>
  )
}
