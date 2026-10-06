import { ArrowRight, BarChart3, Brain, FileText, Layers, Search, Settings, Sparkles } from 'lucide-react'
import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { brand, built, hero, ideas, impact, layers, prompt, quote, signals, stat } from './data'
import { Crystal, Glow, Logo, Mono } from './parts'

const Hero = () => (
  <Slide background={brand.ink} className="font-manrope text-white">
    <Glow x={-40} y={400} w={500} h={200} c="#10122a" />
    <Crystal x={810} y={0} w={440} h={440} />
    <Logo x={25} y={30} size={22} />
    <Abs x={65} y={170} className="text-[63px] font-medium leading-[76px] tracking-[-0.02em] whitespace-nowrap">
      <div>{hero.lines[0]}</div><div className="pl-[240px]">{hero.lines[1]}</div><div>{hero.lines[2]}</div>
    </Abs>
    <Mono x={60} y={585} w={330} className="text-[10px] text-white/60">{hero.mono}</Mono>
    <ArrowRight size={16} className="absolute text-white/50" style={{ left: 790, top: 588 }} />
    <Abs x={823} y={588} className="text-[13px] leading-[17px]">{hero.tag.map((t) => <div key={t}>{t}</div>)}</Abs>
  </Slide>
)

const Quote = () => (
  <Slide className="font-montalt">
    <Glow x={-60} y={150} w={260} h={280} c="#ece9f8" />
    <Logo x={640} y={185} size={36} color="#050507" />
    <Abs x={640} y={265} w={620} className="text-[40px] font-medium leading-[44px] tracking-[-0.01em] text-[#9a9a9f]">
      {quote.lead}<span className="text-[#050507]">{quote.strong}</span>{quote.rest}
    </Abs>
    <ImagePlaceholder className="absolute" tone="#2a2a30" style={{ left: 22, top: 510, width: 108, height: 108 }} />
    <Abs x={150} y={560} className="text-[11px] font-semibold">{quote.author.name}</Abs>
    <Mono x={150} y={585} className="text-[10px] leading-[12px] text-[#666]">{quote.author.role.map((r) => <div key={r}>{r}</div>)}</Mono>
  </Slide>
)

const Ideas = () => (
  <Slide background={brand.ink} className="font-manrope text-white">
    <Glow x={-80} y={-60} w={420} h={180} c="#1a1440" />
    <Crystal x={790} y={0} w={490} h={530} />
    <Logo x={52} y={100} size={30} />
    <Abs x={55} y={330} className="text-[82px] font-medium leading-[70px] tracking-[-0.02em]">
      <div>{ideas.lines[0]}</div><div className="text-[#9a9a9f]">{ideas.lines[1]}</div>
      <div><span className="text-[#9a9a9f]">to </span>Completion</div>
    </Abs>
    <Mono x={78} y={615} className="text-[11px] text-white/70">{ideas.mono.map((m) => <div key={m}>{m}</div>)}</Mono>
    <Mono x={1000} y={640} className="text-white/70">{ideas.url}</Mono>
  </Slide>
)

const Stat = () => (
  <Slide background={brand.ink} className="font-manrope text-white">
    <Logo x={25} y={26} size={20} />
    <Abs x={30} y={100} className="text-[200px] font-medium leading-[240px] tracking-[-0.05em]">
      {stat.value[0]}<span className="bg-clip-text text-transparent" style={{ backgroundImage: 'linear-gradient(90deg,#c9b8ff,#7646ff)' }}>{stat.value[1]}</span>
    </Abs>
    <Abs x={320} y={316} className="text-[11px] text-white/50">{stat.caption}</Abs>
    <Abs x={702} y={385} className="text-[14px]">{stat.head}</Abs>
    <Abs x={702} y={440} w={540} className="text-[30px] leading-[37px] tracking-[-0.01em]">{stat.body}</Abs>
  </Slide>
)

const nodes: [number, number, boolean, typeof Layers][] = [
  [160, 200, false, Layers], [320, 200, true, Search], [480, 200, false, Brain],
  [160, 360, true, FileText], [480, 360, true, Settings],
  [160, 520, false, Sparkles], [320, 520, true, BarChart3], [480, 520, false, Layers],
]
const Impact = () => (
  <Slide background="#f3f3f4" className="font-manrope">
    <Logo x={22} y={28} size={16} color="#050507" />
    <Abs x={635} y={0} w={645} h={720} style={{ background: brand.purple }} />
    {nodes.map(([x, y, dark, Icon]) => (
      <Abs key={`${x}${y}`} x={x - 37} y={y - 37} w={75} h={75} className="flex items-center justify-center rounded-md shadow-sm" style={{ background: dark ? brand.purple : '#fff' }}>
        <Icon size={26} color={dark ? '#fff' : '#555'} />
      </Abs>
    ))}
    <Abs x={298} y={307} w={110} h={110} className="flex items-center justify-center rounded-md" style={{ background: brand.purple }}>
      <ImagePlaceholder className="h-[40px] w-[70px] rounded-sm" tone="#b9a4ff" />
    </Abs>
    <Mono x={22} y={640} w={400} className="text-[9px] text-[#555]">{impact.caption}</Mono>
    <Abs x={677} y={104} className="text-[28px] font-semibold leading-[40px] tracking-[-0.01em] text-white">
      <div>{impact.title[0]}</div><div className="font-medium text-white/60">{impact.title[1]}</div>
    </Abs>
    {impact.steps.map((s, i) => (
      <Abs key={s.v} x={635 + i * 205} y={[322, 420, 478][i]} w={205} h={720 - [322, 420, 478][i]} className="bg-white">
        <div className="absolute left-[32px] top-[26px] text-[44px] font-medium leading-[56px] tracking-[-0.03em]">{s.v}</div>
        <div className="absolute left-[32px] top-[92px] w-[130px] font-plexmono text-[8px] leading-[10px] text-[#777]">{s.l}</div>
      </Abs>
    ))}
  </Slide>
)

const Built = () => (
  <Slide background={brand.purple} className="font-manrope text-white">
    <Logo x={27} y={36} size={46} />
    <ArrowRight size={30} className="absolute" style={{ left: 30, top: 358 }} />
    <Abs x={100} y={352} w={800} className="text-[33px] font-medium leading-[43px] tracking-[-0.01em]">
      <span className="font-semibold">{built.strong}</span><span className="text-white/55">{built.rest}</span>
    </Abs>
  </Slide>
)

const Prompt = () => (
  <Slide background={brand.ink} className="font-manrope">
    <Abs x={0} y={0} w={540} h={720} style={{ background: brand.purple }} />
    <Abs x={540} y={0} w={380} h={720} className="bg-[#f3f3f4]" />
    <Logo x={30} y={355} size={26} />
    <Abs x={30} y={430} w={440} className="text-[34px] font-medium leading-[43px] text-white">
      {prompt.title[0]}{prompt.title[1]}<span className="text-white/60">{prompt.title[2]}</span>
    </Abs>
    <Abs x={583} y={437} w={175} h={32} className="flex items-center bg-[#7646ff] px-3 font-plexmono text-[11px] text-white">{prompt.tag}</Abs>
    <Mono x={583} y={480} w={300} className="text-[9px] text-[#777]">{prompt.monoLeft}</Mono>
    <Abs x={955} y={80} w={180} h={30} className="flex items-center bg-white px-3 font-plexmono text-[11px] text-black">{brand.name}</Abs>
    <Mono x={955} y={140} w={300} className="text-[10px] text-white/80">{prompt.monoRight}</Mono>
    <Crystal x={920} y={400} w={360} h={320} />
  </Slide>
)

const Layers_ = () => (
  <Slide background="#f1f1f2" className="font-manrope">
    <Logo x={5} y={28} size={14} color="#050507" />
    <Abs x={-25} y={420} className="text-[34px] font-medium leading-[43px]">
      <div className="text-[#9a9a9f]">{layers.title[0]}</div><div className="text-[#9a9a9f]">{layers.title[1]}</div>
      <div>{layers.title[2]}</div><div className="font-semibold">{layers.title[3]}</div>
    </Abs>
    {layers.cards.map((c, i) => (
      <Abs key={c.tag} x={437 + i * 418} y={127} w={400} h={525} className="overflow-hidden">
        <ImagePlaceholder className="absolute inset-0" tone="#1d1b2e" />
        <div className="absolute bottom-0 left-0 right-0 h-[320px] bg-white/10 p-6 backdrop-blur-[2px]">
          <div className="font-plexmono text-[9px] text-white/70">{c.tag}</div>
          <div className="mt-24 text-[24px] font-medium leading-[32px] text-white">{c.text}</div>
        </div>
      </Abs>
    ))}
  </Slide>
)

const Signals = () => (
  <Slide background={brand.ink} className="font-manrope text-white">
    <Logo x={5} y={28} size={14} />
    <Abs x={-60} y={110} className="text-[30px] leading-[43px] tracking-[-0.01em]">
      <div>{signals.title[0]}</div><div className="text-white/70">{signals.title[1]}</div>
    </Abs>
    {signals.boxes.map((b, i) => (
      <Abs key={b.v} x={575 + i * 290} y={175} w={290} h={212} className={i ? 'bg-[#6c6c70]' : 'border border-white/30'}>
        <div className="absolute left-5 top-14 text-[38px] font-medium">{b.v}</div>
        <Mono x={20} y={125} w={220} className="text-[9px] text-white/70">{b.t}</Mono>
      </Abs>
    ))}
    <Abs x={580} y={392} w={285} h={220} style={{ background: brand.purple }}>
      <div className="absolute left-5 top-5 text-[34px] font-medium">{signals.year}</div>
    </Abs>
  </Slide>
)

const deck: DeckDefinition = { id: '17', title: 'Elabor.rate', slides: [Prompt, Hero, Quote, Signals, Ideas, Stat, Layers_, Impact, Built] }
export default deck
