import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { MessageSquare, Brain, Lightbulb, Sparkles, User } from 'lucide-react'
import { theme } from './theme'
import { cover, need, system, solution, feedback, stp } from './data'
import { Bar, NamePill, Panel, SectionHead, Tag, Title } from './components'

const F = 'font-pretendard'

function Cover() {
  return (
    <Slide background={theme.dark} className={F}>
      <Abs x={63} y={62} className="flex items-center gap-2 text-[24px] font-bold text-white"><Sparkles size={22} color={theme.purple} />aness</Abs>
      <Abs x={63} y={125} className="text-[39px] font-bold leading-[56px] text-white">{cover.title.map((l) => <div key={l}>{l}</div>)}</Abs>
      <Abs x={63} y={504} w={110} h={49} className="flex items-center justify-center rounded-md text-[15px] font-semibold text-white" style={{ background: theme.purple }}>{cover.cta}</Abs>
      <Abs x={63} y={600} w={170} h={1} className="bg-white/15" />
      <Abs x={63} y={615} className="text-[15px] leading-[22px] text-white/60">{cover.note.map((l) => <div key={l}>{l}</div>)}</Abs>
      {cover.pills.map(([n, x, y]) => <NamePill key={n} name={n} x={x} y={y} />)}
    </Slide>
  )
}

function Need() {
  const icons = [Brain, Lightbulb]
  return (
    <Slide background={theme.dark} className={F}>
      <Tag dark>{need.label}</Tag>
      <Title y={110} size={27} color="#fff">{need.title.map((l) => <div key={l} className="leading-[44px]">{l}</div>)}</Title>
      {need.cards.map((c, i) => {
        const I = icons[i]
        return (
          <Abs key={c.h} x={c.x} y={250} w={511} h={390} className="overflow-hidden rounded-3xl" style={{ background: theme.card }}>
            <div className="flex h-[75px] items-center justify-center bg-black/20 text-[17px] font-semibold" style={{ color: theme.purple }}>{c.h}</div>
            <div className="mx-auto mt-[48px] flex size-[91px] items-center justify-center rounded-full text-white" style={{ background: theme.purple }}><I size={40} /></div>
            <div className="mt-[34px] text-center text-[19px] leading-[31px] text-white/40">
              {c.lines.map((l, j) => <div key={l} className={c.bold.includes(j) ? 'font-bold text-white' : ''}>{l}</div>)}
            </div>
          </Abs>
        )
      })}
    </Slide>
  )
}

function System() {
  return (
    <Slide className={F}>
      <Tag>{system.label}</Tag>
      <Title y={110} size={28}>{system.title}</Title>
      <Abs x={0} y={162} w={1280} className="text-center text-[14px] text-[#333]">{system.sub}</Abs>
      <Abs x={0} y={229} w={1280} h={360} style={{ background: theme.panel }} />
      {system.pills.map(([n, x, y]) => <NamePill key={n} name={n} x={x} y={y} w={130} h={54} shadow={false} />)}
      <ImagePlaceholder className="absolute rounded-md" style={{ left: 451, top: 282, width: 381, height: 256 }} />
      <Abs x={880} y={365} w={160} className="text-center text-[15px] font-semibold leading-[28px]">{system.flow.map((l) => <div key={l}>{l}</div>)}</Abs>
      <Abs x={1105} y={340} w={122} h={122} className="flex flex-col items-center justify-center gap-1 rounded-full bg-white text-[13px] text-[#666] shadow-[0_4px_18px_rgba(0,0,0,0.12)]"><User size={30} />USER</Abs>
      <Abs x={0} y={620} w={1280} className="text-center text-[14px] leading-[28px] text-[#222]">{system.note.map((l) => <div key={l}>{l}</div>)}</Abs>
    </Slide>
  )
}

function Solution() {
  const s = solution
  return (
    <Slide className={F}>
      <SectionHead a={s.label} b={s.sub} />
      <Title y={142} size={22}>{s.title}</Title>
      <ImagePlaceholder className="absolute" style={{ left: 0, top: 226, width: 512, height: 365 }} />
      <ImagePlaceholder className="absolute rounded-3xl" style={{ left: 450, top: 276, width: 180, height: 376 }} />
      <Abs x={84} y={618} className="text-[15px] text-[#999]">{s.caption}</Abs>
      <Abs x={707} y={225} w={519} h={195} className="rounded-xl border border-[#ddd] bg-white p-4 text-[14px] leading-[24px]">
        <div className="text-[15px] font-bold">● {s.problem.h}</div>
        <div className="mt-2 text-[#555]">{s.problem.b.map((b) => <div key={b}>· {b}</div>)}</div>
      </Abs>
      <Abs x={707} y={428} w={519} className="text-center text-[22px]">↓</Abs>
      <Abs x={707} y={462} w={519} h={190} className="overflow-hidden rounded-xl border border-[#c9b3ff] bg-white text-[14px] leading-[24px]">
        <div className="flex h-[56px] items-center px-4 text-[15px] font-bold text-white" style={{ background: theme.purple }}>● {s.fix.h}</div>
        <div className="p-4 pt-3 text-[#333]">{s.fix.b.map((b) => <div key={b}>· {b}</div>)}</div>
      </Abs>
    </Slide>
  )
}

function Feedback() {
  const f = feedback
  return (
    <Slide className={F}>
      <SectionHead a={solution.label} b={solution.sub} />
      <Title y={142} size={24}>{f.title}</Title>
      <Panel x={51} y={226} w={397} h={210}>
        <div className="absolute left-5 top-4 text-[14px] font-bold">{f.freq.q}</div>
        <ImagePlaceholder className="absolute rounded-full" style={{ left: 213, top: 27, width: 157, height: 157 }} />
        {f.freq.legend.map((l, i) => <div key={l} className="absolute left-5 text-[13px]" style={{ top: 112 + i * 26 }}>● {l}</div>)}
      </Panel>
      <Panel x={467} y={226} w={397} h={210}>
        <div className="absolute left-5 top-4 text-[14px] font-bold">{f.purpose.q}</div>
        {f.purpose.bars.map(([l, v], i) => <Bar key={l} label={l} v={v} x={20} y={68 + i * 47} w={355} />)}
      </Panel>
      <Panel x={51} y={456} w={397} h={212}>
        <div className="absolute left-5 top-4 text-[14px] font-bold">{f.pay.q}</div>
        {f.pay.rows.map((r, i) => (
          <div key={i} className="absolute flex w-full text-[14px]" style={{ top: 62 + i * 50 }}>
            <span className="ml-5 w-[100px] text-[#888]">{r[0]}</span><span className="w-[95px] text-[#999]">{r[1]}</span>
            <span className="w-[100px] text-[#555]">{r[2]}</span><span className="font-bold" style={{ color: theme.purple }}>{r[3]}</span>
          </div>
        ))}
      </Panel>
      <Panel x={467} y={456} w={397} h={212}>
        <div className="absolute left-5 top-4 text-[14px] font-bold">{f.pain.q}</div>
        {f.pain.bars.map(([l, v], i) => <Bar key={l} label={l} v={v} x={20} y={68 + i * 47} w={355} />)}
      </Panel>
      <Abs x={922} y={226} w={307} h={442} className="rounded-3xl" style={{ background: theme.dark }}>
        <div className="mt-[44px] flex justify-center" style={{ color: theme.purple }}><MessageSquare size={22} fill={theme.purple} /></div>
        <div className="mt-2 text-center text-[17px] font-bold text-white">{f.side.h}</div>
        {f.side.items.map((t, i) => (
          <div key={t} className="mx-[24px] mt-[14px] flex h-[78px] items-center justify-center rounded-lg px-4 text-center text-[15px] leading-[19px] text-white" style={{ background: i === 0 ? theme.purple : theme.card, marginTop: i === 0 ? 40 : 14 }}>{t}</div>
        ))}
      </Abs>
    </Slide>
  )
}

function Stp() {
  return (
    <Slide background={theme.dark} className={F}>
      <SectionHead a={stp.label} b={stp.sub} dark />
      <Title y={142} size={24} color="#fff">{stp.title}</Title>
      <Abs x={0} y={437} w={1280} h={1} className="bg-white/20" />
      {stp.cols.map((c) => (
        <div key={c.l}>
          <Abs x={c.x} y={230} w={339} className="text-center text-[15px]" style={{ color: theme.purple }}>{c.en}</Abs>
          <Abs x={c.x} y={262} w={339} h={175} className="flex flex-col items-center justify-center rounded-t-full text-white" style={{ background: 'linear-gradient(#8b4dff,#7a56f5)' }}>
            <div className="mt-6 text-[48px] font-semibold leading-none">{c.l}</div><div className="mt-2 text-[16px] font-semibold">{c.k}</div>
          </Abs>
          <Abs x={c.x - 16} y={466} w={380} className="text-[19px] font-bold leading-[30px] text-white">{c.h.map((l) => <div key={l}>{l}</div>)}</Abs>
          <Abs x={c.x - 16} y={540} w={380} className="text-[14px] leading-[21px] text-white/50">{c.p.map((l, i) => <div key={i} className="min-h-[21px]">{l}</div>)}</Abs>
        </div>
      ))}
    </Slide>
  )
}

const deck: DeckDefinition = { id: '28', title: '아네스 ANESS', slides: [Cover, Need, System, Solution, Feedback, Stp] }
export default deck
