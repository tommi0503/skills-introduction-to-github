import type { ReactNode } from 'react'
import { Abs, ImagePlaceholder } from '../../ui'
import { theme } from './theme'

export function Head({ part, title, sub }: { part: string; title: string; sub: string }) {
  return (
    <>
      <Abs x={50} y={42} className="text-[14px] font-semibold">{part}</Abs>
      <Abs x={50} y={70} className="text-[34px] font-bold leading-none">{title}</Abs>
      <Abs x={281} y={78} className="text-[17px]">{sub}</Abs>
      <Abs x={281} y={108} w={949} h={2} className="bg-[#333]" />
      <ImagePlaceholder className="absolute rounded-full" style={{ left: 50, top: 600 + (part === 'PART 2.' ? 31 : 0) - 0, width: 52, height: 52 }} />
    </>
  )
}
export const Pill = ({ children, black, className = '' }: { children: ReactNode; black?: boolean; className?: string }) => (
  <div className={`inline-flex items-center justify-center rounded-full px-5 py-[6px] text-[17px] font-bold ${black ? 'bg-black text-white' : 'border border-[#ccc] bg-white'} ${className}`} style={{ color: black ? '#fff' : theme.ink }}>{children}</div>
)
export const Box = ({ x, y, w, h, className = '', style, children }: { x: number; y: number; w: number; h: number; className?: string; style?: React.CSSProperties; children?: ReactNode }) => (
  <Abs x={x} y={y} w={w} h={h} className={`border border-black text-center ${className}`} style={style}>{children}</Abs>
)
export const Lines = ({ lines, className }: { lines: string[]; className?: string }) => <div className={className}>{lines.map((l, i) => <div key={i}>{l}</div>)}</div>
