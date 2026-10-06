import { Triangle } from 'lucide-react'
import type { ReactNode } from 'react'
import { Abs, Slide, type DeckDefinition } from '../../ui'
import { brand, kpi, progress } from './data'

const S = 3.122 // reference px -> slide px
const sx = (x: number) => (x - 171) * S

function Chrome({ page, children, bg = '#fff' }: { page: number; children: ReactNode; bg?: string }) {
  return (
    <Slide background={bg} className="font-dm">
      {children}
      <Abs x={59} y={662} className="text-[16px] font-medium" style={{ color: brand.blue }}>{brand.name}</Abs>
      <Abs x={0} y={662} w={1221} className="text-right text-[14px]" style={{ color: brand.blue }}>Page {page}</Abs>
    </Slide>
  )
}

const Title = ({ lines, y = 100 }: { lines: string[]; y?: number }) => (
  <Abs x={59} y={y} className="text-[58px] font-medium leading-[69px] tracking-[-0.02em]">
    <div className="text-[#111]">{lines[0]}</div>
    <div className="text-[#8a8a8a]">{lines[1]}</div>
  </Abs>
)

const Progress = () => (
  <Chrome page={1} bg="#f7f7f7">
    <Abs x={59} y={64} className="text-[14px] text-[#555]">{progress.section}</Abs>
    <Title lines={progress.title} y={108} />
    <Abs x={53} y={290} w={1170} h={343} className="rounded-[24px] bg-white">
      {Array.from({ length: 17 }).map((_, i) => <div key={i} className="absolute top-[20px] h-[290px] w-px bg-[#e6e6e6]" style={{ left: 40 + i * 70 }} />)}
    </Abs>
    {progress.tasks.map((t) => (
      <div key={t.label}>
        <Abs x={96} y={t.y - 16} w={144} h={32} className="flex items-center justify-center rounded-md text-[12px] font-medium"
          style={{ background: t.active ? '#e3ebff' : '#ececec', color: t.active ? brand.blue : '#222' }}>{t.label}</Abs>
        <Abs x={sx(t.start)} y={t.y - 16} w={sx(t.end) - sx(t.start)} h={32} className="rounded-full bg-[#ececec]" />
        <Abs x={sx(t.start)} y={t.y - 16} w={sx(t.done) - sx(t.start)} h={32} className="rounded-full" style={{ background: t.active ? brand.blue : '#bdbdbd' }} />
        <Abs x={sx(t.done) - 50} y={t.y - 8} w={40} h={16} className="flex items-center justify-center rounded-full bg-white text-[8px]">{t.pct}</Abs>
        <Abs x={sx(t.end) + 20} y={t.y - 12} w={300} className="text-[9px] leading-[11px] text-[#444]">{t.note}</Abs>
      </div>
    ))}
  </Chrome>
)

const Kpi = () => (
  <Chrome page={2}>
    <Abs x={0} y={0} w={787} h={318} className="bg-[#f5f5f5]" />
    <Abs x={787} y={0} w={493} h={625} className="rounded-br-[28px]" style={{ background: brand.blue }} />
    <Abs x={59} y={64} className="text-[14px] text-[#555]">{kpi.section}</Abs>
    <Title lines={kpi.title} y={102} />
    <Abs x={50} y={400} className="text-[180px] leading-[250px] tracking-[-0.03em] text-black">{kpi.hero.value}</Abs>
    <Triangle size={36} className="absolute fill-[#cfcfcf] text-[#cfcfcf]" style={{ left: 537, top: 420 }} />
    <Abs x={537} y={462} className="text-[22px] leading-[28px]" style={{ color: brand.blue }}>{kpi.hero.label.map((l) => <div key={l}>{l}</div>)}</Abs>
    {kpi.stats.map((s, i) => {
      const y = [78, 250, 420][i]
      return (
        <div key={s.value}>
          <Abs x={850} y={y} className="text-[72px] leading-[100px] text-white tracking-[-0.02em]">{s.value}</Abs>
          <Abs x={850} y={y + 100} w={300} className="text-[14px] leading-[18px] text-white/80">{s.label}</Abs>
          {i < 2 && <Abs x={850} y={y + 153} w={360} h={1} className="bg-white/40" />}
        </div>
      )
    })}
  </Chrome>
)

const deck: DeckDefinition = { id: '15', title: 'DigiCorp KPI', slides: [Progress, Kpi] }
export default deck
