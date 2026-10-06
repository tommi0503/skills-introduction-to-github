import type { CSSProperties, ReactNode } from 'react'
import { Slide } from '../../ui'
import { theme } from './theme'

export const Frame = ({ bg = '#fff', children }: { bg?: string; children: ReactNode }) => (
  <Slide background={bg}>
    <div className="relative origin-top-left" style={{ width: 1280 / theme.k, height: 720 / theme.k, transform: `scale(${theme.k})` }}>{children}</div>
  </Slide>
)
export const T = ({ x, y, w, h, className = '', style, children }: { x: number; y: number; w?: number; h?: number; className?: string; style?: CSSProperties; children?: ReactNode }) => (
  <div className={`absolute font-inter ${className}`} style={{ left: x, top: y, width: w, height: h, ...style }}>{children}</div>
)
export const Pill = ({ x, y, children, solid }: { x: number; y: number; children: ReactNode; solid?: boolean }) => (
  <T x={x} y={y} className="whitespace-nowrap rounded-[2px] px-[3px] py-[1px] text-[4.2px] font-medium" style={solid ? { background: '#fff', color: theme.orange } : { background: 'rgba(255,255,255,0.22)', color: '#fff' }}>{children}</T>
)
export const InfoCard = ({ x, title, rows }: { x: number; title: string; rows: string[][] }) => (
  <T x={x} y={112} w={79} h={70} className="rounded-[3px] bg-white p-[5px] shadow-[0_1px_6px_rgba(0,0,0,0.12)]">
    <div className="text-[4.5px] font-bold" style={{ color: theme.orange }}>{title}</div>
    {rows.map(([a, b]) => <div key={a} className="mt-[3px] border-t border-gray-100 pt-[2px]"><div className="text-[4.2px] font-semibold">{a}</div><div className="text-[3.4px] leading-[4px] text-gray-500">{b}</div></div>)}
  </T>
)
