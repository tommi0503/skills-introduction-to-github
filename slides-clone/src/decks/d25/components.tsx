import { Abs } from '../../ui'
import { BarChart3, Crosshair, Megaphone, Shapes } from 'lucide-react'
import { theme } from './theme'

export function Meta({ page, dark }: { page: string; dark?: boolean }) {
  return (
    <div className="absolute inset-x-0 top-[22px] font-dm text-[17px]" style={{ color: dark ? '#fff' : theme.ink }}>
      <span className="absolute left-[54px]">splashlink agecy</span>
      <span className="absolute" style={{ left: 632 }}>2024</span>
      <span className="absolute right-[64px]">{page}</span>
    </div>
  )
}

export function Logo() {
  return <div className="flex items-center gap-2 font-dm text-[30px] font-semibold text-white"><Shapes size={26} />splashlink</div>
}

export function IconDot({ kind, x, y }: { kind: 'chart' | 'target' | 'mega'; x: number; y: number }) {
  const I = kind === 'chart' ? BarChart3 : kind === 'target' ? Crosshair : Megaphone
  return <Abs x={x} y={y} w={40} h={40} className="flex items-center justify-center rounded-full text-white" style={{ background: theme.dark }}><I size={20} /></Abs>
}

export function StatCard({ title, desc, y }: { title: string; desc: string[]; y: number }) {
  return (
    <Abs x={713} y={y} w={502} h={170} style={{ background: `linear-gradient(90deg, ${theme.lime}, #fafbe8)` }}>
      <div className="absolute left-[37px] top-[30px] flex size-[44px] items-center justify-center rounded-md" style={{ background: theme.dark, color: theme.lime }}><Shapes size={24} /></div>
      <div className="absolute left-[113px] top-[30px] font-dm text-[28px]" style={{ color: theme.ink }}>{title}</div>
      <div className="absolute left-[113px] top-[78px] font-dm text-[22px] leading-[30px]" style={{ color: theme.ink }}>{desc.map((d) => <div key={d}>{d}</div>)}</div>
    </Abs>
  )
}
