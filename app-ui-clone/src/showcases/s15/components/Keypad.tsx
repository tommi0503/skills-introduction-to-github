import type { KeypadKey } from '../data'
import { theme } from '../theme'

/** 4-column numeric keypad; keys carry their own grid placement and tone. */
export function Keypad({ keys }: { keys: KeypadKey[] }) {
  return (
    <div className="grid grid-cols-4 gap-x-[5.4px] gap-y-[5.4px]" style={{ gridAutoRows: 83.2 }}>
      {keys.map((k) => {
        const Icon = k.icon
        const dark = k.tone === 'primary'
        return (
          <span
            key={k.key}
            className="flex items-center justify-center rounded-full text-[31px]"
            style={{
              gridColumn: k.col,
              gridRow: `${k.row} / span ${k.rowSpan ?? 1}`,
              background: theme.keyTones[k.tone],
              color: dark ? '#fff' : theme.ink,
            }}
          >
            {Icon ? <Icon size={dark ? 20 : 28} strokeWidth={dark ? 2.4 : 1.9} /> : k.label}
          </span>
        )
      })}
    </div>
  )
}
