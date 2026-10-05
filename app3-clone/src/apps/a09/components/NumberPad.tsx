import type { ReactNode } from 'react'
import { Delete } from 'lucide-react'
import { padRows, type PadKey } from '../data'
import { theme } from '../theme'

function DigitKey({ k }: { k: PadKey }) {
  return (
    <div
      className="flex h-[47px] flex-col items-center justify-center rounded-[5px]"
      style={{ background: theme.key, boxShadow: `0 1px 0 ${theme.keyShadow}` }}
    >
      <span className="text-[25px] leading-[26px] text-black" style={{ marginTop: k.letters === undefined ? 0 : -2 }}>
        {k.digit}
      </span>
      {k.letters !== undefined && (
        <span className="h-[11px] text-[9.5px] leading-[11px] font-bold tracking-[2px] text-black">{k.letters}</span>
      )}
    </div>
  )
}

export interface NumberPadProps {
  /** Bar above the keys (accessory "Done" bar or the QuickType suggestion). */
  accessory: ReactNode
  top: number
}

/** iOS numeric keypad pinned to the bottom of the screen. */
export function NumberPad({ accessory, top }: NumberPadProps) {
  return (
    <div className="absolute inset-x-0 bottom-0" style={{ top, background: theme.keyboardBg }}>
      {accessory}
      <div className="grid grid-cols-3 gap-x-[6px] gap-y-[9px] px-[6px] pt-[6px]">
        {padRows.flat().map((k, i) =>
          k === null ? (
            <div key={i} />
          ) : k === 'delete' ? (
            <div key={i} className="flex h-[47px] items-center justify-center">
              <Delete size={26} strokeWidth={1.5} className="text-black" />
            </div>
          ) : (
            <DigitKey key={i} k={k} />
          ),
        )}
      </div>
    </div>
  )
}
