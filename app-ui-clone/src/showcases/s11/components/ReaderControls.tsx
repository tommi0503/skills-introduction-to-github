import { Clock3, Sun, Type } from 'lucide-react'
import type { ReactNode } from 'react'
import { cn } from '../../../ui'

function RoundAction({ children }: { children: ReactNode }) {
  return <span className="ml-[4px] flex size-[42px] items-center justify-center rounded-full bg-black">{children}</span>
}

export interface ReaderControlsProps {
  time: string
  modes: string[]
  active: string
}

/** Bottom reader toolbar: timer pill, Read/Listen switch and two round actions. */
export function ReaderControls({ time, modes, active }: ReaderControlsProps) {
  return (
    <div className="flex items-center font-inter text-white">
      <div className="flex h-[43px] w-[93px] items-center justify-center gap-[10px] rounded-full bg-black">
        <Clock3 size={19} strokeWidth={1.8} />
        <span className="text-[13.5px] font-semibold">{time}</span>
      </div>
      <div className="ml-[15px] flex h-[43px] w-[139px] items-center rounded-full bg-black p-[4px]">
        {modes.map((m) => (
          <span
            key={m}
            className={cn(
              'flex h-full flex-1 items-center justify-center rounded-full text-[13.5px]',
              m === active ? 'bg-white font-semibold text-black' : 'text-[#bdbdbd]',
            )}
          >
            {m}
          </span>
        ))}
      </div>
      <RoundAction>
        <Sun size={21} strokeWidth={1.6} />
      </RoundAction>
      <RoundAction>
        {/* "Tt" text-size glyph composed from two lucide Type icons */}
        <span className="relative flex items-end">
          <Type size={19} strokeWidth={1.6} />
          <Type size={11} strokeWidth={2} className="-ml-[7px] mb-[1px]" />
        </span>
      </RoundAction>
    </div>
  )
}
