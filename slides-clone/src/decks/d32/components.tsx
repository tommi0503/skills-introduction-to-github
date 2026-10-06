import type { ReactNode } from 'react'
import { Abs, ImagePlaceholder } from '../../ui'
import { Heart, Trees } from 'lucide-react'
import { theme } from './theme'

export const Logo = ({ y = 62, white }: { y?: number; white?: boolean }) => (
  <Abs x={1100} y={y} className="flex items-center gap-1 text-[20px] font-bold" style={{ color: white ? '#fff' : theme.green }}><Trees size={22} />초록우산</Abs>
)
export const Head = ({ crumb, title, white, dim }: { crumb: string; title: ReactNode; white?: boolean; dim?: boolean }) => (
  <>
    <Abs x={52} y={46} className="text-[14px] font-semibold" style={{ color: white ? '#fff' : theme.green }}>{crumb}</Abs>
    <Abs x={52} y={72} className="text-[29px] font-bold leading-[43px]" style={{ color: white ? '#fff' : dim ? '#555' : theme.ink }}>{title}</Abs>
    <Logo y={dim ? 62 : 56} white={white} />
  </>
)
export const Lines = ({ lines, className }: { lines: string[]; className?: string }) => <div className={className}>{lines.map((l) => <div key={l}>{l}</div>)}</div>
export const Panel = ({ x, w, children }: { x: number; w: number; children?: ReactNode }) => (
  <Abs x={x} y={154} w={w} h={513} className="rounded-[28px] shadow-[0_2px_16px_rgba(0,0,0,0.06)]" style={{ background: theme.panel }}>{children}</Abs>
)
export const PanelTitle = ({ lines }: { lines: string[] }) => <Lines lines={lines} className="pt-[34px] text-center text-[24px] font-medium leading-[37px] text-[#444]" />
export const Tag = ({ x, y, children, solid }: { x: number; y: number; children: ReactNode; solid?: boolean }) => (
  <Abs x={x} y={y} className="rounded-full px-3 py-[2px] text-[16px] font-semibold" style={{ background: solid ? theme.mid : '#fff', color: solid ? '#fff' : theme.green, border: `1px solid ${theme.mid}` }}>{children}</Abs>
)
export const BigHeart = ({ x, y, size, fill, children }: { x: number; y: number; size: number; fill: string; children: ReactNode }) => (
  <Abs x={x} y={y} w={size} h={size} className="flex items-center justify-center text-center text-white">
    <Heart className="absolute inset-0" size={size} fill={fill} stroke="none" />
    <div className="relative">{children}</div>
  </Abs>
)
export { ImagePlaceholder }
