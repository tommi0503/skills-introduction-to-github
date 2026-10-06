import { Abs } from '../../ui'
import { theme } from './theme'
import type { Perk } from './data'

export const PerkCard = ({ p }: { p: Perk }) => {
  const I = p.icon
  return (
    <Abs x={p.x} y={p.y} w={300} h={93} className="rounded-xl bg-white font-inter shadow-[0_6px_24px_rgba(60,90,160,0.12)]">
      <div className="absolute flex items-center justify-center rounded-md" style={{ left: 20, top: 16, width: 22, height: 22, background: p.color + '55', color: p.color }}><I size={14} /></div>
      <div className="absolute text-[14px] text-gray-500" style={{ left: 52, top: 18 }}>{p.label}</div>
      <div className="absolute text-[20px] font-medium" style={{ left: 20, top: 52 }}>{p.text}</div>
    </Abs>
  )
}
export const Bullet = ({ y, b, last }: { y: number; b: { bold: string; text: string }; last: boolean }) => (
  <>
    <Abs x={44} y={y + 5} w={9} h={9} className="rounded-full" style={{ background: theme.blue }} />
    {!last && <Abs x={48} y={y + 22} w={1.5} h={36} style={{ background: theme.blue }} />}
    <Abs x={78} y={y - 8} w={385} className="font-inter text-[16px] leading-[26px]" style={{ color: theme.muted }}><b className="font-semibold">{b.bold}</b>{b.text}</Abs>
  </>
)
