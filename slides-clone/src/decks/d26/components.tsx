import { Abs, ImagePlaceholder } from '../../ui'
import { theme } from './theme'

export function SystemCard({ label, x }: { label: string; x: number }) {
  const i = label.lastIndexOf(' '); const a = label.slice(0, i), rest = [label.slice(i + 1)]
  return (
    <Abs x={x} y={322} w={190} h={398}>
      <div className="h-[114px] bg-white px-[20px] pt-[32px] text-[15px] font-semibold leading-[19px]">{a}<br />{rest.join(" ")}</div>
      <ImagePlaceholder className="h-[284px] w-full" />
    </Abs>
  )
}

/**
 * Horizontal bar with a right-aligned value. The label is drawn once over the whole row with
 * mix-blend "difference", so it stays legible (white on the bar, black on the track) even when the
 * value is wider than a short bar.
 */
export function BarRow({ value, w, y }: { value: string; w: number; y: number }) {
  return (
    <Abs x={33} y={y} w={821} h={70} className="isolate bg-white">
      <div className="absolute right-0 top-0 h-full bg-black" style={{ width: w }} />
      <div className="absolute inset-0 flex items-center justify-end pr-1 text-[60px] font-light leading-none text-white mix-blend-difference" style={{ letterSpacing: '-0.02em' }}>{value}</div>
    </Abs>
  )
}

export function Layer({ n, title, desc, y }: { n: string; title: string; desc: string[]; y: number }) {
  return (
    <Abs x={94} y={y} w={300} className="text-right">
      <div className="text-[11px]" style={{ color: theme.muted }}>{n}</div>
      <div className="mt-1 text-[18px] font-semibold">{title}</div>
      <div className="mt-3 text-[13px] leading-[18px]" style={{ color: theme.muted }}>{desc.map((d) => <div key={d}>{d}</div>)}</div>
    </Abs>
  )
}
