import { Abs } from '../../ui'
import { Txt } from './components'
import { t } from './theme'

/** Line/area chart with gridlines, y ticks and year labels. `x,y` = plot top-left. */
export function AreaChart({ x, y, w, h, max, step, values, years }: { x: number; y: number; w: number; h: number; max: number; step: number; values: number[]; years: string[] }) {
  const pad = 22
  const px = (i: number) => pad + (i * (w - pad * 2)) / (values.length - 1)
  const py = (v: number) => h - (v / max) * h
  const pts = values.map((v, i) => `${px(i)},${py(v)}`).join(' ')
  const ticks = Array.from({ length: max / step + 1 }, (_, i) => i * step)
  return (
    <>
      <Abs x={x} y={y}>
        <svg width={w} height={h + 2} className="overflow-visible">
          {ticks.map((v) => <line key={v} x1={0} x2={w} y1={py(v)} y2={py(v)} stroke="#d9d9d9" strokeWidth={1} />)}
          <line x1={0} x2={0} y1={0} y2={h} stroke="#d9d9d9" />
          <polygon points={`${px(0)},${h} ${pts} ${px(values.length - 1)},${h}`} fill="#d5e3d1" />
          <polyline points={pts} fill="none" stroke={t.green} strokeWidth={2} />
          {values.map((v, i) => <circle key={i} cx={px(i)} cy={py(v)} r={3.5} fill={t.green} />)}
        </svg>
      </Abs>
      {ticks.map((v) => <Txt key={v} x={x - 8} cy={y + py(v)} size={16} align="right" w={60} style={{ color: '#666' }}>{v}</Txt>)}
      {years.map((yr, i) => <Txt key={yr} x={x + px(i)} cy={y + h + 16} size={16} align="center" w={60} style={{ color: '#666' }}>{yr}</Txt>)}
    </>
  )
}

/** Donut with the green share drawn clockwise from 12 o'clock. */
export function Donut({ cx, cy, r, ring, value, bg = t.bg }: { cx: number; cy: number; r: number; ring: number; value: number; bg?: string }) {
  return (
    <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: `conic-gradient(${t.green} 0 ${value}%, #c8c8c8 0)` }}>
      <div className="absolute rounded-full" style={{ inset: ring, background: bg }} />
    </Abs>
  )
}
