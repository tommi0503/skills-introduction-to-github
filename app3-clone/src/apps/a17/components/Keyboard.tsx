import { ArrowBigUp, CornerDownLeft, Delete, Mic, Smile } from 'lucide-react'
import type { ReactNode } from 'react'
import { cn } from '../../../ui'

export interface KeyboardProps {
  suggestions: string[]
  rows: string[]
  background?: string
  className?: string
}

function Key({ children, className }: { children?: ReactNode; className?: string }) {
  return (
    <div
      className={cn('flex h-[42px] items-center justify-center rounded-[6px] bg-white text-[21px] text-black', className)}
      style={{ boxShadow: '0 1px 0 rgba(0,0,0,0.25)' }}
    >
      {children}
    </div>
  )
}

/** iOS light QWERTY keyboard with a suggestion strip. */
export function Keyboard({ suggestions, rows, background = '#e4e5e7', className }: KeyboardProps) {
  const [r1, r2, r3] = rows
  return (
    <div className={cn('absolute inset-x-0 bottom-0 rounded-t-[22px]', className)} style={{ background, height: 330 }}>
      <div className="flex h-[48px] items-center pt-[2px] text-[16px] text-[#333]">
        {suggestions.map((s, i) => (
          <div key={s} className={cn('flex flex-1 items-center justify-center', i > 0 && 'border-l border-[#c8c8cc]')}>
            {s}
          </div>
        ))}
      </div>
      <div className="flex flex-col gap-[11px] px-[3px] pt-[5px]">
        <div className="flex gap-[6px] px-[2px]">
          {r1.split('').map((k) => (
            <Key key={k} className="flex-1">{k}</Key>
          ))}
        </div>
        <div className="flex gap-[6px] px-[21px]">
          {r2.split('').map((k) => (
            <Key key={k} className="flex-1">{k}</Key>
          ))}
        </div>
        <div className="flex gap-[6px] px-[2px]">
          <Key className="mr-[8px] w-[44px]">
            <ArrowBigUp size={22} fill="currentColor" strokeWidth={1.5} />
          </Key>
          {r3.split('').map((k) => (
            <Key key={k} className="flex-1">{k}</Key>
          ))}
          <Key className="ml-[8px] w-[44px]">
            <Delete size={22} strokeWidth={1.6} />
          </Key>
        </div>
        <div className="flex gap-[6px] px-[2px]">
          <Key className="w-[90px] text-[15px]">123</Key>
          <Key className="flex-1" />
          <Key className="w-[92px]">
            <CornerDownLeft size={20} strokeWidth={1.6} />
          </Key>
        </div>
      </div>
      <div className="absolute inset-x-0 bottom-[22px] flex items-center justify-between px-[25px] text-[#4a4a4a]">
        <Smile size={30} strokeWidth={1.5} />
        <Mic size={27} strokeWidth={1.6} />
      </div>
    </div>
  )
}
