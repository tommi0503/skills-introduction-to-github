import { Abs } from '../../ui'
import { theme } from './theme'

export const TopBar = ({ title, left, right }: { title: string; left?: string; right?: string }) => (
  <>
    <Abs x={0} y={45} w={1280} className="text-center text-[27px] font-semibold">{title}</Abs>
    {left && <Abs x={50} y={50} className="text-[16px]" style={{ color: theme.pale }}>{left}</Abs>}
    {right && <Abs x={1000} y={50} w={230} className="text-right text-[16px]" style={{ color: theme.pale }}>{right}</Abs>}
  </>
)
export const Lines = ({ lines, className }: { lines: string[]; className?: string }) => <div className={className}>{lines.map((l) => <div key={l}>{l}</div>)}</div>
export const YellowDot = ({ x, y, d = 40 }: { x: number; y: number; d?: number }) => (
  <Abs x={x - d / 2} y={y - d / 2} w={d} h={d} className="rounded-full" style={{ background: theme.yellow }} />
)
