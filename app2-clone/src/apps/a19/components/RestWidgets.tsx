import { ArrowLeft, ArrowRight, Moon, Sun } from 'lucide-react'
import { cn } from '../../../ui'
import { fi } from '../theme'

/** Text tabs with an underline below the active one. */
export function PeriodTabs({ items, active, gaps, className }: { items: string[]; active: string; gaps: number[]; className?: string }) {
  return (
    <div className={cn('flex border-b border-[#e3e3e3]', className)}>
      {items.map((t, i) => (
        <div key={t} className="relative pb-[12px] text-[15.5px]" style={{ color: t === active ? '#111' : '#888', marginRight: gaps[i] ?? 0 }}>
          {t}
          {t === active && <span className="absolute -bottom-[1px] left-[-1px] right-[-1px] h-[2px] bg-[#555]" />}
        </div>
      ))}
    </div>
  )
}

/** Rounded pill with previous/next arrows around a date. */
export function DateStepper({ label, className }: { label: string; className?: string }) {
  const arrow = 'flex h-[22px] w-[22px] items-center justify-center rounded-full bg-[#f1f1f1]'
  return (
    <div className={cn('flex h-[37px] items-center justify-between rounded-full border border-[#ececec] px-[6px]', className)}>
      <span className={arrow}><ArrowLeft size={13} strokeWidth={2.2} /></span>
      <span className="text-[13px] text-[#555]">{label}</span>
      <span className={arrow}><ArrowRight size={13} strokeWidth={2.2} /></span>
    </div>
  )
}

/** Labelled value with an optional left divider. */
export function Metric({
  label,
  value,
  color,
  align = 'left',
  divider,
  className,
  valueClassName,
}: {
  label: string
  value: string
  color: string
  align?: 'left' | 'center'
  divider?: boolean
  className?: string
  valueClassName?: string
}) {
  return (
    <div className={cn('flex flex-col', align === 'center' ? 'items-center' : 'items-start', divider && 'border-l border-[#e6e6e6]', className)}>
      <span className="text-[13px] text-[#777]">{label}</span>
      <span className={cn('font-medium', valueClassName)} style={{ color }}>{value}</span>
    </div>
  )
}

/** Day timeline: light track with dark sleep segments on a 0..1 axis. */
export function SleepTimeline({ segments, className }: { segments: { from: number; to: number }[]; className?: string }) {
  return (
    <div className={cn('overflow-hidden rounded-[20px]', className)} style={{ background: fi.timelineBg }}>
      {segments.map((s, i) => (
        <span
          key={i}
          className="absolute inset-y-0"
          style={{ left: `${s.from * 100}%`, width: `max(2px, ${(s.to - s.from) * 100}%)`, background: fi.blue }}
        />
      ))}
    </div>
  )
}

/** Night bar: moon + start, sun + end, with red interruption ticks. */
export function NightBar({ start, end, marks, className }: { start: string; end: string; marks: number[]; className?: string }) {
  return (
    <div className={cn('flex h-[28px] items-center justify-between rounded-full px-[10px] text-[13.5px] font-medium text-white', className)} style={{ background: fi.blue }}>
      {marks.map((m) => (
        <span key={m} className="absolute inset-y-0 w-[1.5px] bg-[#e06a6a]" style={{ left: m }} />
      ))}
      <span className="flex items-center gap-[6px]">
        <Moon size={14} fill="#fff" strokeWidth={0} />
        {start}
      </span>
      <span className="flex items-center gap-[5px]">
        {end}
        <Sun size={17} strokeWidth={2} fill="#fde47a" stroke="#fde47a" />
      </span>
    </div>
  )
}

export function Band({ className }: { className?: string }) {
  return <div className={cn('h-[9px] bg-[#f2f2f2]', className)} />
}

/** Axis labels centred on evenly spaced ticks; first/last hug the edges. */
export function TickAxis({ labels, className }: { labels: string[]; className?: string }) {
  const last = labels.length - 1
  return (
    <div className={cn('h-[14px]', className)}>
      {labels.map((l, i) => (
        <span
          key={i}
          className="absolute text-[11px] text-[#888]"
          style={{
            left: i === last ? undefined : `${(i / last) * 100}%`,
            right: i === last ? 0 : undefined,
            transform: i === 0 || i === last ? undefined : 'translateX(-50%)',
          }}
        >
          {l}
        </span>
      ))}
    </div>
  )
}
