import { ChevronLeft, ChevronRight, Flame, Plus, Share } from 'lucide-react'
import { CircleButton } from '../components/CircleButton'
import { MonthGrid, steps } from '../components/MonthGrid'
import { Shell } from '../components/Shell'
import { meetingScreen as d } from '../data'
import { theme } from '../theme'

const COLS = steps(27, 55.7, 7)
const SHADOW = 'shadow-[0_8px_18px_rgba(90,90,160,.12)]'

export function MeetingScreen() {
  return (
    <Shell background="#fff">
      <CircleButton x={37} y={80} className={SHADOW}>
        <ChevronLeft size={20} strokeWidth={2} />
      </CircleButton>
      <span className="absolute inset-x-0 top-[70px] flex items-center justify-center gap-[6px] text-[14px] font-semibold">
        <Flame size={16} fill="#000" />
        {d.streak}
      </span>
      <CircleButton x={352} y={80} className={SHADOW}>
        <Share size={17} strokeWidth={1.8} />
      </CircleButton>
      <div className="absolute inset-x-0 top-[130px] flex items-center justify-center gap-[24px] text-[13.5px] text-[#8a8a8a]">
        <ChevronLeft size={15} strokeWidth={1.5} />
        {d.month}
        <ChevronRight size={15} strokeWidth={1.5} />
      </div>
      {d.weekdays.map((w, i) => (
        <span key={i} className="absolute -translate-x-1/2 text-[9.5px] font-medium text-[#9a9a9a]" style={{ left: COLS[i], top: 169 }}>
          {w}
        </span>
      ))}
      <MonthGrid
        cells={d.cells}
        colX={COLS}
        rowY={[212, 382]}
        renderCell={(c) => (c.day ? <span className="text-[9.5px] text-[#9a9a9a]">{c.day}</span> : null)}
      />
      {d.cells.slice(0, 7).map((c, i) =>
        c.day ? <Plus key={i} className="absolute -translate-x-1/2" style={{ left: COLS[i], top: 270 }} size={16} strokeWidth={1.2} color="#777" /> : null,
      )}

      <div className="absolute inset-x-0 bottom-0 top-[418px] rounded-t-[32px] text-white" style={{ background: theme.sheetDark }}>
        <span className="absolute left-1/2 top-[8px] h-[4px] w-[30px] -translate-x-1/2 rounded-full bg-[#8a8a8a]" />
        <span className="absolute left-[28px] top-[35px] text-[16px]">{d.sheetTitle}</span>
        {d.rows.map((r, i) => (
          <div key={r.label} className="absolute left-[28px] right-[28px] flex h-[32px] items-center justify-between" style={{ top: 83 + i * 48 }}>
            <span className="text-[13.5px] text-[#efefef]">{r.label}</span>
            {r.action ? (
              <span className="flex h-[32px] items-center gap-[6px] rounded-full bg-[#555] px-[14px] text-[12px]">
                <Plus size={13} strokeWidth={1.6} />
                {r.action}
              </span>
            ) : (
              <span className="text-[12px]" style={{ color: r.muted ? '#7a7a7a' : '#f2f2f2' }}>{r.value}</span>
            )}
          </div>
        ))}
        <span className="absolute left-[28px] top-[284px] text-[12px] text-[#777]">{d.notes}</span>
        <div className="absolute left-[20px] right-[20px] top-[342px] flex h-[55px] items-center justify-center rounded-full bg-white text-[14px] font-medium text-[#111]">
          {d.cta}
        </div>
      </div>
    </Shell>
  )
}
