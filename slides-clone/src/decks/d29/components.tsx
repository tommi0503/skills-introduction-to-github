import type { ReactNode } from 'react'
import { Abs, ImagePlaceholder } from '../../ui'
import { theme } from './theme'

export function Brand({ small }: { small?: boolean }) {
  return <div className="flex items-center gap-1.5 font-bold" style={{ color: theme.coral, fontSize: small ? 14 : 16 }}><ImagePlaceholder className="size-[16px] rounded-full" tone={theme.logoTone} />약손명가 <span className="font-normal text-[#444]">헬스케어</span></div>
}
export const Header = ({ left = '회사소개', page }: { left?: string; page?: string }) => (
  <>
    <Abs x={49} y={46} className="text-[14px] font-bold">{left}</Abs>
    <Abs x={1098} y={46}><Brand small /></Abs>
    {page && <Abs x={1180} y={686} className="text-[12px] text-[#aaa]">{page}</Abs>}
  </>
)
export const Title = ({ x = 84, y = 138, center, children }: { x?: number; y?: number; center?: boolean; children: ReactNode }) => (
  <Abs x={center ? 0 : x} y={y} w={center ? 1280 : undefined} className={`text-[34px] font-bold ${center ? 'text-center' : ''}`}>{children}</Abs>
)
export const Desc = ({ x = 84, y, lines, center }: { x?: number; y: number; lines: string[]; center?: boolean }) => (
  <Abs x={center ? 0 : x} y={y} w={center ? 1280 : undefined} className={`text-[17px] leading-[29px] text-[#444] ${center ? 'text-center' : ''}`}>{lines.map((l) => <div key={l}>{l}</div>)}</Abs>
)
export const Circle = ({ x, y, r, className = '', style, children }: { x: number; y: number; r: number; className?: string; style?: React.CSSProperties; children?: ReactNode }) => (
  <Abs x={x - r} y={y - r} w={2 * r} h={2 * r} className={`flex flex-col items-center justify-center rounded-full text-center ${className}`} style={style}>{children}</Abs>
)
export const Lines = ({ lines, className }: { lines: string[]; className?: string }) => <div className={className}>{lines.map((l) => <div key={l}>{l}</div>)}</div>
