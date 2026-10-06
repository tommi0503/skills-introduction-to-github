import type { ReactNode } from 'react'
import { Abs } from '../../ui'
import { Check, ArrowRight, Hexagon } from 'lucide-react'
import { theme } from './theme'

export function Brand({ size = 15 }: { size?: number }) {
  return <div className="flex items-center gap-1.5 font-semibold" style={{ color: theme.blue, fontSize: size }}><Hexagon size={size} fill={theme.blue} />AIR KLASS <span className="text-[10px] font-normal text-[#444]">business</span></div>
}
export const Footer = () => <Abs x={51} y={666}><Brand /></Abs>
export const Label = ({ children, color = theme.ink }: { children: ReactNode; color?: string }) => <Abs x={51} y={50} className="text-[15px] font-bold" style={{ color }}>{children}</Abs>

export function Menu({ items, active, y = 125 }: { items: string[]; active: number; y?: number }) {
  return (
    <Abs x={84} y={y} className="text-[21px] leading-[41px]">
      {items.map((m, i) => <div key={m} className="font-bold" style={{ color: i === active ? theme.blueText : theme.pale }}>{m}</div>)}
    </Abs>
  )
}
export function Lines({ lines, className }: { lines: string[]; className?: string }) {
  return <div className={className}>{lines.map((l) => <div key={l}>{l}</div>)}</div>
}
export function Circle({ x, y, r, lines }: { x: number; y: number; r: number; lines: string[] }) {
  return (
    <Abs x={x - r} y={y - r} w={r * 2} h={r * 2} className="flex flex-col items-center justify-center rounded-full bg-[#eaf1fd] shadow-[inset_0_0_0_1px_#d3e2f8]">
      <Check size={16} color={theme.blue} /><Lines lines={lines} className="mt-1 text-center text-[13px] leading-[18px]" />
    </Abs>
  )
}
export function ArrowDot({ x, y, white }: { x: number; y: number; white?: boolean }) {
  return <Abs x={x - 14} y={y - 14} w={28} h={28} className="flex items-center justify-center rounded-full" style={{ background: white ? '#fff' : theme.blue, color: white ? theme.ink : '#fff' }}><ArrowRight size={16} /></Abs>
}
