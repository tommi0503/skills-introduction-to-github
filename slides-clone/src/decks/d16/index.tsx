import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { brand, feedback as F, roadmap as R } from './data'

const Feedback = () => (
  <Slide background="#1a1a1f" className="font-manrope">
    <ImagePlaceholder className="absolute inset-0" tone="#23232b" label="gradient background" />
    <Abs x={94} y={72} className="text-[14px] text-white/60">{F.section}</Abs>
    <Abs x={0} y={72} w={1204} className="text-right text-[14px] text-white/60">{brand}</Abs>
    <Abs x={94} y={240} w={800} className="text-[33px] leading-[39px] text-white">
      {F.quote.map((q) => <p key={q} className="mb-[12px]">{q}</p>)}
    </Abs>
    <ImagePlaceholder className="absolute rounded-full" tone="#3a3a44" style={{ left: 92, top: 568, width: 56, height: 56 }} />
    <Abs x={168} y={576} className="text-[16px] text-white">{F.author.name}</Abs>
    <Abs x={168} y={602} className="text-[12px] text-[#3fd9a8]">{F.author.role}</Abs>
    <Abs x={1240} y={672} className="text-[10px] text-white/40">9</Abs>
  </Slide>
)

const Roadmap = () => (
  <Slide className="font-manrope text-[#111]">
    <Abs x={94} y={76} className="text-[11px] text-[#aaa]">{R.section}</Abs>
    <Abs x={94} y={120} w={700} className="text-[44px] leading-[47px] tracking-[-0.01em]">{R.title}</Abs>
    {R.columns.map((c, i) => (
      <Abs key={c.no} x={94 + i * 352} y={366} w={260}>
        <div className="text-[11px] text-[#2cc7a8]">{c.no}</div>
        <div className="mt-[12px] text-[17px]">{c.name}</div>
        <ul className="mt-[40px] flex flex-col gap-[14px] text-[12px] leading-[17px] text-[#777]">
          {c.items.map((t) => <li key={t} className="relative pl-[16px]"><span className="absolute left-[2px] top-[6px] h-[3px] w-[3px] rounded-full bg-[#777]" />{t}</li>)}
        </ul>
      </Abs>
    ))}
    <Abs x={1220} y={684} className="text-[10px] text-[#bbb]">10</Abs>
  </Slide>
)

const deck: DeckDefinition = { id: '16', title: 'CLOUDS projects', slides: [Feedback, Roadmap] }
export default deck
