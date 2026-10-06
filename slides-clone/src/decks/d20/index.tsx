import { Abs, Slide, type DeckDefinition } from '../../ui'
import { Results } from '../d21'
import { Team } from '../d22'
import { action as A, changes as C, hero as H, pressure as P } from './data'
import { Heading, Photo, VeroHeader, VeroLogo, vero } from './parts'

const Hero = () => (
  <Slide background="#101012" className="font-manrope">
    <Photo x={0} y={0} w={1280} h={720} className="!bg-[#1c1c20]" />
    <VeroLogo x={575} y={226} size={30} />
    <Heading x={0} y={290} w={1280} size={66} lh={72} className="text-center">
      <div>{H.lines[0]}</div><div className="italic">{H.lines[1]}</div>
    </Heading>
    <Abs x={380} y={465} w={520} className="text-center text-[19px] leading-[25px] text-white/80">{H.sub}</Abs>
  </Slide>
)

const Pressure = () => (
  <Slide background="#1b1b1b" className="font-manrope">
    <Photo x={0} y={0} w={1280} h={433} />
    <Heading x={48} y={462} size={67} lh={70}>
      <div>{P.lines[0]}</div><div className="pl-[300px] italic">{P.lines[1]}</div><div className="pl-[440px]">{P.lines[2]}</div>
    </Heading>
    <Abs x={48} y={625} className="text-[18px] leading-[26px] text-white/80">{P.sub.map((s) => <div key={s}>{s}</div>)}</Abs>
  </Slide>
)

const Changes = () => (
  <Slide background="#1b1b1b" className="font-manrope">
    <VeroHeader section={C.section} page="Page 01" />
    <Heading x={51} y={135} size={57} lh={68}>{C.title.map((t) => <div key={t}>{t}</div>)}</Heading>
    <Abs x={51} y={438} w={260} className="text-[17px] leading-[24px] text-white/90">{C.sub}</Abs>
    <Abs x={51} y={555} w={290} className="text-[10px] leading-[13px] text-white/35">{C.note}</Abs>
    {C.bars.map((b, i) => {
      const x = 526 + i * 183
      return (
        <div key={b.v}>
          <Abs x={x} y={138} w={164} h={536} style={{ background: '#2a2a2a' }} />
          {b.image
            ? <Photo x={x} y={674 - b.h} w={164} h={b.h} className="!bg-[#6f8fc4]" />
            : <Abs x={x} y={674 - b.h} w={164} h={b.h} style={{ background: vero.blue }} />}
          <Abs x={x + 14} y={674 - b.h + 14} className="text-[36px] font-medium leading-none text-white">{b.v}</Abs>
          <Abs x={x + 14} y={674 - b.h + 62} w={120} className="text-[10px] leading-[12px] text-white/70">{b.l}</Abs>
        </div>
      )
    })}
  </Slide>
)

const Action = () => (
  <Slide background="#1b1b1b" className="font-manrope">
    <Photo x={539} y={0} w={741} h={720} />
    <VeroHeader section={A.section} />
    <Heading x={48} y={135} w={560} size={57} lh={68}>{A.title.map((t) => <div key={t}>{t}</div>)}</Heading>
    {A.pills.map((p) => (
      <Abs key={p.t} x={p.x} y={p.y} w={p.w} h={36} className="flex items-center justify-center rounded-full border border-white/20 bg-[#2b2b2b] text-[12px] font-medium text-white">{p.t}</Abs>
    ))}
    <Abs x={48} y={620} className="text-[17px] leading-[27px] text-white">{A.contact.map((c) => <div key={c}>{c}</div>)}</Abs>
  </Slide>
)

const deck: DeckDefinition = { id: '20', title: 'Vero Deck', slides: [Hero, Pressure, Changes, Action, Team, Results] }
export default deck
