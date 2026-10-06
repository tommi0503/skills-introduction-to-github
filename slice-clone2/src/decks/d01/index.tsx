import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder, cn } from '../../ui'
import { Bubble, Center, Croc, FrameSlide, Heading, Photo, Star } from './components'
import { charts, closing, cover, keywords, longText, photos, team, toc, topic } from './data'
import { t } from './theme'

function Cover() {
  return (
    <FrameSlide>
      <Center cy={248} size={118} className={t.head}>
        {cover.title}<span className={t.body} style={{ fontSize: 98 }}>{cover.titleTail}</span>
      </Center>
      <Center cy={390} size={44} className={t.body}>{cover.sub}</Center>
      <Croc x={36} y={322} w={310} h={328} />
      <Croc x={992} y={322} w={256} h={334} />
    </FrameSlide>
  )
}

function Toc() {
  return (
    <FrameSlide>
      <Heading text={toc.title} cy={128} size={62} />
      {toc.items.map((it, i) => (
        <Abs key={it.label} x={395} y={226 + i * 97} h={60} className="flex items-center gap-5 whitespace-nowrap leading-none">
          <span className={t.head} style={{ fontSize: 46 }}>{it.label}</span>
          <span className={t.body} style={{ fontSize: 38 }}>{it.text}</span>
        </Abs>
      ))}
      <Croc x={952} y={350} w={268} h={300} />
    </FrameSlide>
  )
}

function Team() {
  return (
    <FrameSlide>
      <Heading text={team.title} cy={114} size={58} />
      {team.members.map((m, i) => {
        const cx = 262 + i * 271
        return (
          <div key={i}>
            <Abs x={cx - 104} y={226} w={208} h={208} className="overflow-hidden rounded-full" style={{ border: `3px solid ${t.ink}` }}>
              <ImagePlaceholder label="member photo" className="h-full w-full" />
            </Abs>
            <Center cy={490} size={46} x={cx - 135} w={270} className={t.head}>{m.name}</Center>
            <Center cy={548} size={30} x={cx - 135} w={270} className={t.body}>{m.role}</Center>
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Topic() {
  return (
    <FrameSlide>
      <Heading text={topic.kicker} cy={140} size={60} />
      <Center cy={340} size={100} className={t.body}>{topic.title}</Center>
      <Center cy={452} size={40} className={t.body}>{topic.sub}</Center>
      <Star x={146} y={348} size={70} />
      <Star x={1015} y={232} size={44} />
      <Star x={1062} y={240} size={70} />
      <Croc x={972} y={366} w={268} h={318} />
    </FrameSlide>
  )
}

function Keywords() {
  return (
    <FrameSlide>
      <Heading text={keywords.title} cy={124} size={58} />
      {keywords.items.map((k, i) => {
        const cx = [262, 627, 1030][i]
        return (
          <div key={k.word}>
            <Croc x={cx - 68} y={214} w={136} h={96} />
            {i === keywords.circled && (
              <Abs x={cx - 155} y={302} w={310} h={124} className="rounded-[50%]" style={{ border: `4px solid ${t.red}` }} />
            )}
            <Center cy={364} size={84} x={cx - 180} w={360} className={t.head}>{k.word}</Center>
            {k.desc.map((d, j) => (
              <Center key={d} cy={462 + j * 58} size={34} x={cx - 180} w={360} className={t.body}>{d}</Center>
            ))}
          </div>
        )
      })}
    </FrameSlide>
  )
}

function Charts() {
  const { pie, bars } = charts
  return (
    <FrameSlide>
      <Heading text={charts.title} cy={118} size={60} />
      <Abs x={202} y={210} w={320} h={320} className="rounded-full" style={{ border: `4px solid ${t.ink}`, background: `conic-gradient(${t.teal} 0 ${pie.value}%, #fff 0)` }} />
      <Abs x={250} y={318} className={cn(t.head, 'leading-none')} style={{ fontSize: 50 }}>{pie.labels[0]}</Abs>
      <Abs x={360} y={402} className={cn(t.head, 'leading-none')} style={{ fontSize: 60 }}>{pie.labels[1]}</Abs>
      <Center cy={583} size={42} x={162} w={400} className={t.body}>{pie.caption}</Center>
      {bars.heights.map((h, i) => (
        <Abs key={i} x={752 + i * 84} y={514 - h} w={48} h={h} className="rounded-t-[24px]" style={{ border: `4px solid ${t.ink}`, borderBottom: 0 }} />
      ))}
      <Abs x={725} y={512} w={400} h={4} style={{ background: t.ink }} />
      <Abs x={856} y={270} w={92} h={50}><ImagePlaceholder label="curly arrow" className="h-full w-full" /></Abs>
      <Abs x={952} y={240} className={cn(t.body, 'leading-none')} style={{ fontSize: 54 }}>{bars.emphasis}</Abs>
      <Abs x={998} y={400} className={cn(t.body, 'leading-none')} style={{ fontSize: 32 }}>{bars.note}</Abs>
      <Center cy={583} size={42} x={710} w={400} className={t.body}>{bars.caption}</Center>
    </FrameSlide>
  )
}

function Photos() {
  return (
    <FrameSlide>
      <Heading text={photos.title} cy={124} size={60} />
      <Photo x={133} y={226} w={384} h={380} />
      <Photo x={602} y={283} w={566} h={326} />
      <Abs x={330} y={520} w={305} h={110} className={cn('flex flex-col items-center justify-center bg-white leading-tight', t.body)} style={{ border: `3px solid ${t.ink}` }}>
        <div style={{ fontSize: 36 }}>{photos.caption[0]}</div>
        <div style={{ fontSize: 22 }}>{photos.caption[1]}</div>
      </Abs>
      <Bubble x={888} y={188} w={316} h={152} lines={photos.bubble} />
    </FrameSlide>
  )
}

function LongText() {
  return (
    <FrameSlide>
      <Heading text={longText.title} cy={124} size={60} />
      <Photo x={126} y={203} w={309} h={413} />
      <Bubble x={88} y={170} w={262} h={120} lines={longText.bubble} style={{ fontSize: 26 }} />
      <Abs x={478} y={240} className={cn(t.head, 'whitespace-nowrap leading-none')} style={{ fontSize: 46 }}>{longText.heading}</Abs>
      <Abs x={478} y={318} w={690} className={t.body} style={{ fontSize: 33, lineHeight: '50px' }}>{longText.body}</Abs>
    </FrameSlide>
  )
}

function Closing() {
  return (
    <FrameSlide>
      <Croc x={87} y={180} w={428} h={510} />
      <Heading text={closing.kicker} cy={124} size={58} />
      {closing.lines.map((l, i) => (
        <Center key={l} cy={300 + i * 142} size={112} x={500} w={480} className={t.body}>{l}</Center>
      ))}
    </FrameSlide>
  )
}

const deck: DeckDefinition = { id: '01', title: '아고 프레젠테이션', slides: [Cover, Toc, Team, Topic, Keywords, Charts, Photos, LongText, Closing] }
export default deck
