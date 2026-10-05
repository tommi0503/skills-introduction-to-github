import { ArrowUp, CalendarDays, ChevronLeft, ChevronRight, Files, Plus } from 'lucide-react'
import { ImagePlaceholder, cn } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { Keyboard } from '../components/Keyboard'
import { MonthGrid, steps } from '../components/MonthGrid'
import { Shell } from '../components/Shell'
import { keyboards, linkScreen as d } from '../data'
import { theme } from '../theme'

const COLS = steps(32, 49, 7)

export function LinkScreen() {
  return (
    <Shell background="linear-gradient(180deg,#fbf8ec 0%,#f7f5ee 60%,#eeeeee 100%)">
      <div className="absolute left-[13px] top-[58px] flex h-[60px] w-[131px] items-center rounded-full bg-[#fdfcf7] pl-[6px]" style={{ boxShadow: '0 6px 16px rgba(0,0,0,.06)' }}>
        <ImagePlaceholder label="Sam avatar" className="size-[48px] rounded-full" />
        <span className="ml-[11px] text-[17px] font-bold">{d.name}</span>
      </div>
      <CircleButton x={352} y={89} size={48} background="#fdfcf7" className="shadow-[0_6px_16px_rgba(0,0,0,.06)]">
        <Plus size={20} strokeWidth={2} />
      </CircleButton>

      <div className="absolute left-[15px] right-[17px] top-[134px] h-[340px] rounded-[16px] bg-white">
        <div className="absolute left-[15px] top-[22px] text-[18px] font-extrabold tracking-[-0.3px]">
          {d.month} <span className="text-[#d0d0d0]">{d.year}</span>
        </div>
        <CalendarDays className="absolute left-[267px] top-[23px]" size={20} strokeWidth={1.6} />
        <ChevronLeft className="absolute left-[302px] top-[23px]" size={20} strokeWidth={1.8} />
        <ChevronRight className="absolute left-[334px] top-[23px]" size={20} strokeWidth={1.8} />
        {d.weekdays.map((w, i) => (
          <span
            key={w}
            className="absolute -translate-x-1/2 text-[9.5px]"
            style={{ left: COLS[i], top: 64, color: i >= d.weekendFrom ? '#d9534f' : '#888' }}
          >
            {w}
          </span>
        ))}
        <MonthGrid
          cells={d.cells}
          colX={COLS}
          rowY={steps(107, 39.8, 6)}
          renderCell={(c) =>
            c.thumb ? (
              <ImagePlaceholder label="event photo" className="size-[32px] rounded-[6px]" />
            ) : (
              <span
                className={cn('flex h-[32px] w-[30px] items-center justify-center rounded-[6px] text-[14px] font-semibold', c.selected && 'text-white')}
                style={{ background: c.selected ? theme.purple : undefined, color: c.selected ? undefined : c.muted ? '#bdbdbd' : '#1a1a1a' }}
              >
                {c.day}
              </span>
            )
          }
        />
      </div>

      <div
        className="absolute left-[16px] right-[18px] top-[478px] z-10 flex h-[54px] items-center rounded-full bg-[#fbfbfb] pl-[22px] pr-[11px]"
        style={{ boxShadow: '0 4px 14px rgba(0,0,0,.08)' }}
      >
        <Files size={18} strokeWidth={1.7} />
        <span className="ml-[11px] h-[20px] w-[2px] bg-[#3b82f6]" />
        <span className="ml-[1px] flex-1 text-[14.5px] text-[#9a9a9a]">{d.placeholder}</span>
        <span className="flex size-[32px] items-center justify-center rounded-full bg-[#8a8a8a]">
          <ArrowUp size={17} color="#fff" strokeWidth={2.2} />
        </span>
      </div>
      <Keyboard layout={keyboards.upper} className="top-[542px]" />
    </Shell>
  )
}
