import { ArrowUp, Camera, ChevronLeft, ChevronRight, Mic, Scan } from 'lucide-react'
import { MonthGrid, steps } from '../components/MonthGrid'
import { Shell } from '../components/Shell'
import { trackScreen as d } from '../data'
import { theme } from '../theme'

const COLS = steps(27, 55.2, 7)

export function TrackScreen() {
  return (
    <Shell background={theme.scrim} className="font-figtree">
      <div className="absolute inset-x-0 top-0 h-[447px] rounded-b-[16px]" style={{ background: theme.cream }}>
        <ChevronLeft className="absolute left-[20px] top-[66px]" size={16} strokeWidth={1.6} color="#555" />
        <span className="absolute inset-x-0 top-[66px] text-center text-[12.5px] font-bold tracking-[2.6px] text-[#222]">{d.month}</span>
        <ChevronRight className="absolute right-[20px] top-[66px]" size={16} strokeWidth={1.6} color="#555" />
        {d.weekdays.map((w, i) => (
          <span key={i} className="absolute -translate-x-1/2 text-[10.5px] font-medium text-[#444]" style={{ left: COLS[i], top: 108 }}>
            {w}
          </span>
        ))}
        <MonthGrid
          cells={d.cells}
          colX={COLS}
          rowY={steps(154, 55.6, 5)}
          renderCell={(c) => (
            <div className="relative flex size-[29px] items-center justify-center rounded-full" style={c.ring ? { border: `1px solid ${theme.ringGreen}` } : undefined}>
              <span className="text-[15px]" style={{ color: c.muted ? theme.muted : c.tone === 'blue' ? theme.blue : '#1e1e1e' }}>
                {c.day}
              </span>
              {c.dot && <span className="absolute top-[34px] size-[4px] rounded-full" style={{ background: theme.dotRed }} />}
            </div>
          )}
        />
      </div>

      <span className="absolute left-[16px] top-[611px] text-[12.5px] font-medium text-[#222]">{d.suggestionsTitle}</span>
      <div className="absolute left-[17px] top-[634px] flex gap-[10px]">
        {d.suggestions.map((s, i) => (
          <div
            key={s}
            className="flex h-[60px] shrink-0 items-center justify-center rounded-[12px] px-[14px] text-center text-[12.5px] leading-[18px] text-[#222]"
            style={{ background: theme.scrimCard, width: i === 0 ? 228 : 109 }}
          >
            {s}
          </div>
        ))}
      </div>
      <div className="absolute left-[17px] right-[17px] top-[705px] h-[100px] rounded-[14px]" style={{ background: theme.scrimCard }}>
        <span className="absolute left-[21px] top-[18px] text-[15px] text-[#555]">{d.placeholder}</span>
        <span className="absolute left-[18px] top-[56px] flex size-[27px] items-center justify-center text-[#333]">
          <Scan className="absolute inset-0" size={27} strokeWidth={1.4} />
          <Camera size={14} strokeWidth={1.8} />
        </span>
        <Mic className="absolute right-[56px] top-[56px]" size={24} strokeWidth={1.5} color="#222" />
        <span className="absolute right-[15px] top-[53px] flex size-[31px] items-center justify-center rounded-full bg-[#a9a6a2]">
          <ArrowUp size={16} color="#d8d6d3" />
        </span>
      </div>
    </Shell>
  )
}
