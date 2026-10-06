import type { ReactNode } from 'react'
import { Abs } from '../../ui'
import { theme } from './theme'

export const Tag = ({ children, dark }: { children: ReactNode; dark?: boolean }) => (
  <Abs x={0} y={48} w={1280} className="text-center text-[15px] font-semibold" style={{ color: theme.purple, opacity: dark ? 1 : 1 }}>{children}</Abs>
)
export const SectionHead = ({ a, b, dark }: { a: string; b: string; dark?: boolean }) => (
  <>
    <Abs x={47} y={50} className="text-[14px] font-semibold" style={{ color: theme.purple }}>{a}</Abs>
    <Abs x={47} y={82} className="text-[15px] font-bold" style={{ color: dark ? '#fff' : theme.ink }}>{b}</Abs>
  </>
)
export const Title = ({ y = 145, size = 24, children, color = theme.ink }: { y?: number; size?: number; children: ReactNode; color?: string }) => (
  <Abs x={0} y={y} w={1280} className="text-center font-bold" style={{ fontSize: size, color }}>{children}</Abs>
)
export function NamePill({ name, x, y, w = 156, h = 66, shadow = true }: { name: string; x: number; y: number; w?: number; h?: number; shadow?: boolean }) {
  return (
    <Abs x={x} y={y} w={w} h={h} className="flex items-center justify-center rounded-full bg-white text-[17px] font-bold text-[#222]" style={{ boxShadow: shadow ? '0 6px 24px rgba(139,77,255,0.35)' : '0 2px 10px rgba(0,0,0,0.12)' }}>{name}</Abs>
  )
}
export function Bar({ label, v, x, y, w, max = 50 }: { label: string; v: number; x: number; y: number; w: number; max?: number }) {
  return (
    <Abs x={x} y={y} w={w}>
      <div className="flex justify-between text-[13px] text-[#333]"><span>{label}</span><span className="font-semibold" style={{ color: theme.purple }}>{v}%</span></div>
      <div className="mt-[6px] h-[5px] rounded-full bg-[#e3e3e8]"><div className="h-full rounded-full" style={{ width: `${(v / max) * 100}%`, background: theme.purple }} /></div>
    </Abs>
  )
}
export const Panel = ({ x, y, w, h, children }: { x: number; y: number; w: number; h: number; children?: ReactNode }) => (
  <Abs x={x} y={y} w={w} h={h} className="rounded-2xl" style={{ background: theme.panel }}>{children}</Abs>
)
