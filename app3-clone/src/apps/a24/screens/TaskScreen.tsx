import { CalendarDays, ChevronRight, GraduationCap, MoreHorizontal, X } from 'lucide-react'
import { ActivityMarks } from '../components/ActivityMarks'
import { CircleButton } from '../components/CircleButton'
import { MonthGrid, steps } from '../components/MonthGrid'
import { Shell } from '../components/Shell'
import { taskScreen as d } from '../data'
import { theme } from '../theme'

const COLS = steps(36, 50.2, 7)

export function TaskScreen() {
  return (
    <Shell background="#c9c9cc">
      <div className="absolute inset-x-0 top-[58px] h-[170px] rounded-t-[30px]" style={{ background: theme.rose }}>
        <CircleButton x={37} y={38} size={44} background="#e2b5b2">
          <X size={22} strokeWidth={1.8} />
        </CircleButton>
        <div className="absolute left-[30px] top-[74px] flex size-[76px] items-center justify-center rounded-full border-[2px] border-[#ece6e5] bg-[#ddd7d6]">
          <GraduationCap size={34} color={theme.roseText} fill={theme.roseText} strokeWidth={1.2} />
        </div>
        <span className="absolute left-[122px] top-[78px] text-[10px] text-[#c8a29e]">{d.time}</span>
        <span className="absolute left-[122px] top-[98px] text-[18.5px] font-bold text-[#f3e7e5]">{d.title}</span>
        <span className="absolute left-[122px] top-[126px] h-px w-[206px] bg-[#c99d99]" />
        <span className="absolute left-[347px] top-[102px] size-[21px] rounded-full border-[1.6px] border-[#f2e8e6]" />
      </div>

      <div className="absolute left-[16px] right-[17px] top-[252px] flex h-[50px] items-center rounded-full bg-[#d7d7d9] pl-[24px] pr-[14px]">
        <CalendarDays size={20} strokeWidth={1.4} color={theme.roseText} />
        <span className="ml-[15px] flex-1 text-[14.5px] text-[#1c1c1c]">{d.date}</span>
        <span className="text-[14px] text-[#8a8a8a]">{d.relative}</span>
        <ChevronRight size={15} color="#9a9a9a" className="ml-[4px]" />
      </div>
      <span className="absolute left-[32px] top-[338px] text-[15px] font-semibold text-[#1c1c1c]">{d.section}</span>
      <span className="absolute left-[332px] top-[338px] flex size-[22px] items-center justify-center rounded-full bg-[#aaaaad]">
        <MoreHorizontal size={14} />
      </span>

      <div className="absolute bottom-[8px] left-[8px] right-[8px] top-[354px] rounded-[26px] rounded-b-[38px] bg-white" style={{ boxShadow: '0 -4px 20px rgba(0,0,0,.08)' }}>
        <div className="absolute inset-x-0 top-0 z-10 h-[88px] rounded-t-[26px] bg-white">
        <div className="absolute left-[20px] top-[20px] flex items-center text-[19px] font-bold">
          {d.month}
          <span className="ml-[6px]" style={{ color: theme.roseText }}>{d.year}</span>
          <ChevronRight size={18} strokeWidth={2.4} color={theme.roseText} className="ml-[6px]" />
        </div>
        <div className="absolute left-[184px] top-[14px] flex h-[36px] w-[68px] items-center justify-center rounded-full bg-white text-[13px] font-medium" style={{ boxShadow: '0 2px 10px rgba(0,0,0,.08)' }}>
          {d.today}
        </div>
        <CircleButton x={285} y={32} size={40} className="shadow-[0_2px_10px_rgba(0,0,0,.08)]">
          <MoreHorizontal size={20} strokeWidth={2.4} />
        </CircleButton>
        <CircleButton x={337} y={32} size={40} className="shadow-[0_2px_10px_rgba(0,0,0,.08)]">
          <X size={20} strokeWidth={1.8} />
        </CircleButton>
        {d.weekdays.map((w, i) => (
          <span key={w} className="absolute -translate-x-1/2 text-[9.5px] text-[#999]" style={{ left: COLS[i], top: 69 }}>
            {w}
          </span>
        ))}
        </div>
        <MonthGrid
          cells={d.cells}
          colX={COLS}
          rowY={steps(96, 61, 6)}
          renderCell={(c) =>
            c.day === 0 ? null : (
              <div className="flex flex-col items-center gap-[6px]">
                <span
                  className="flex size-[30px] items-center justify-center rounded-full text-[15px] font-semibold"
                  style={{ background: c.selected ? '#000' : undefined, color: c.selected ? '#fff' : c.tone === 'rose' ? theme.roseText : '#111' }}
                >
                  {c.day}
                </span>
                <ActivityMarks count={c.marks ?? 0} />
              </div>
            )
          }
        />
      </div>
    </Shell>
  )
}
