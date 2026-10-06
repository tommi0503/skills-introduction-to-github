import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { Check } from 'lucide-react'
import { theme as t } from './theme'
import { cover, features, footnote, users, marketing } from './data'
import { Lines, TopBar, YellowDot } from './components'

const F = 'font-pretendard'

function Cover() {
  return (
    <Slide className={F}>
      <Abs x={0} y={326} w={1280} h={394} style={{ background: t.yellow }} />
      <Abs x={-110} y={95} w={1500} h={300} className="rounded-[50%] bg-white" />
      <Abs x={0} y={80} w={1280} className="text-center text-[32px] font-light text-[#444]">{cover.sub}</Abs>
      <Abs x={0} y={118} w={1280} className="text-center text-[92px] font-bold leading-none">{cover.title}</Abs>
      <ImagePlaceholder className="absolute rounded-[30px]" style={{ left: 416, top: 237, width: 207, height: 356 }} />
      <ImagePlaceholder className="absolute rounded-[34px]" style={{ left: 574, top: 292, width: 256, height: 376 }} />
      <Abs x={1180} y={633} w={50} h={2} className="bg-[#333]" />
      <Abs x={1000} y={642} w={230} className="text-right text-[16px] leading-[26px] text-white/80"><Lines lines={cover.note} /></Abs>
    </Slide>
  )
}

function Features() {
  return (
    <Slide background={t.soft} className={F}>
      <Abs x={0} y={300} w={1280} h={420} className="bg-white" />
      <TopBar title="KB Pay" right="KB Pay 마케팅 지원 >" />
      {features.map((f) => (
        <div key={f.title}>
          <YellowDot x={f.x} y={159} />
          <Abs x={f.x - 150} y={187} w={300} className="text-center text-[23px] font-bold">{f.title}</Abs>
          <ImagePlaceholder className="absolute rounded-t-[36px]" style={{ left: f.phone.x, top: 244, width: f.phone.w, height: 262 }} />
          <Abs x={f.x - 190} y={548} w={380} className="text-center text-[19px] leading-[27px] text-[#555]"><Lines lines={f.lines} /></Abs>
        </div>
      ))}
      <Abs x={0} y={686} w={1280} className="text-center text-[14px]" style={{ color: t.pale }}>{footnote}</Abs>
    </Slide>
  )
}

function Users() {
  return (
    <Slide className={F}>
      <TopBar title="KB Pay" right="KB Pay 마케팅 지원 >" />
      <Abs x={136} y={313} className="text-[36px] leading-[73px]">
        <div className="font-normal">{users.lines[0]}</div>
        <div className="text-[42px] font-bold">{users.lines[1]}</div>
        <div className="text-[42px] font-bold" style={{ color: t.yellow }}>{users.brand}</div>
      </Abs>
      <Abs x={723} y={194} w={400} h={400} className="rounded-full" style={{ background: `conic-gradient(from 0deg, ${t.yellow} 0 125deg, #f1f1f1 125deg 360deg)` }} />
      <Abs x={738} y={209} w={370} h={370} className="rounded-full bg-white" />
      <Abs x={883} y={338} w={80} className="flex justify-center gap-1">
        {[t.yellow, '#e5e5e5', '#e5e5e5'].map((c, i) => <span key={i} className="size-[18px] rounded-full" style={{ background: c }} />)}
      </Abs>
      <Abs x={723} y={374} w={400} className="text-center text-[18px] text-[#666]">{users.label}</Abs>
      <Abs x={723} y={402} w={400} className="text-center text-[54px] font-bold">{users.value}</Abs>
    </Slide>
  )
}

function Marketing() {
  const m = marketing
  return (
    <Slide className={F}>
      <TopBar title={m.title} left="< KB Pay" right="KB Pay 로고 정보 제안 >" />
      <Check className="absolute" size={20} color={t.yellow} style={{ left: 630, top: 138 }} strokeWidth={3} />
      <Abs x={0} y={176} w={1280} className="text-center text-[35px] font-medium">{m.head}</Abs>
      <Abs x={540} y={241} w={200} h={200} className="rounded-full" style={{ background: t.yellow }} />
      <ImagePlaceholder className="absolute" style={{ left: 595, top: 262, width: 90, height: 80 }} />
      <Abs x={540} y={355} w={200} className="text-center text-[30px] font-bold text-white">{m.center}</Abs>
      <Abs x={639} y={433} w={2} h={38} className="bg-[#ddd]" />
      <Abs x={367} y={490} w={546} h={1} className="bg-[#ddd]" />
      {m.items.map((it) => (
        <div key={it.name}>
          <Abs x={it.x} y={512} w={259} h={119} className="rounded-2xl bg-white shadow-[0_2px_14px_rgba(0,0,0,0.12)]">
            <div className="mx-auto mt-[22px] w-[80px] rounded-full bg-black py-[3px] text-center text-[24px] font-bold text-white">{it.name}</div>
            <Lines lines={it.lines} className="mt-3 text-center text-[18px] leading-[27px] text-[#555]" />
          </Abs>
          <Abs x={it.x} y={640} w={259} className="text-center text-[14px]" style={{ color: t.pale }}>{it.cap}</Abs>
        </div>
      ))}
    </Slide>
  )
}

const deck: DeckDefinition = { id: '31', title: 'KB Pay', slides: [Cover, Features, Users, Marketing] }
export default deck
