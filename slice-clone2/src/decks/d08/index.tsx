import type { DeckDefinition } from '../../ui'
import { Abs } from '../../ui'
import { Quote } from 'lucide-react'
import { Box, Lines } from '../../ui'
import { Bubble, Card, Character, GridSlide, PageCard, Placeholder, Ring, Star, Title } from './components'
import { closing, contents, cover, keywords, photos, quote, steps, table, twoRow } from './data'
import { t } from './theme'

function Cover() {
  return (
    <GridSlide>
      <Card x={67} y={67} w={1146} h={586} />
      <Placeholder x={1065} y={32} w={42} h={110} r="0 0 21px 21px" label="paperclip" />
      <Abs x={96} y={288} h={146} className="whitespace-nowrap" style={{ writingMode: 'vertical-rl', fontSize: 14, color: '#aaa', letterSpacing: '0.02em' }}>{cover.sideL}</Abs>
      <Abs x={1170} y={288} h={148} className="whitespace-nowrap" style={{ writingMode: 'sideways-lr', fontSize: 14, color: '#aaa', letterSpacing: '0.02em' }}>{cover.sideR}</Abs>
      <Lines x={644} cy={212} align="center" size={112} className="font-pen" color={t.script} lines={[cover.script]} />
      <Title text={cover.title} cy={356} size={165} />
      <Character cx={634} cy={685} r={198} />
      <Bubble cx={790} cy={492} />
      <Star cx={373} cy={533} size={66} fill="#fdd" />
      <Star cx={957} cy={588} size={66} fill={t.mint} />
      <Ring cx={316} cy={570} />
    </GridSlide>
  )
}

function Contents() {
  return (
    <PageCard page={contents.page}>
      <Title text={contents.title} cy={186} size={104} />
      {contents.items.map((lines, i) => {
        const x = i % 2 ? 646 : 107, y = 273 + Math.floor(i / 2) * 121
        return (
          <div key={i}>
            <Box x={x} y={y} w={525} h={100} bg={t.paper} style={{ border: `2px solid ${t.navy}` }} />
            <Box x={x} y={y} w={68} h={100} bg={t.pink} style={{ border: `2px solid ${t.navy}` }} />
            <Lines x={x + 34} cy={y + 52} align="center" w={68} size={56} className="font-black" color="#fff" lines={[String(i + 1)]} style={{ WebkitTextStroke: `1px ${t.navy}` }} />
            <Lines x={x + 296} cy={y + 51 - (lines.length - 1) * 16} lh={32} align="center" w={440} size={26.5} className="font-medium" color={t.text} lines={lines} />
          </div>
        )
      })}
      <Character cx={52} cy={680} r={155} />
      <Character cx={1231} cy={719} r={170} />
    </PageCard>
  )
}

function QuotePage() {
  const [l1, l2] = quote.title
  return (
    <PageCard page={quote.page}>
      <Title cy={210} size={124} text={<><span style={{ color: t.pink }}>{l1[0]}</span>{l1[1]}</>} />
      <Title cy={340} size={124} text={l2[0]} />
      <Box x={67} y={456} w={1146} h={190} bg={t.paper} style={{ border: `2px solid ${t.navy}` }} />
      <Box x={100} y={444} w={90} h={24} bg="#fff" />
      <Box x={1090} y={444} w={90} h={24} bg="#fff" />
      <Abs x={106} y={418}><Quote size={72} fill={t.navy} color={t.navy} style={{ transform: 'scaleX(-1)' }} /></Abs>
      <Abs x={1104} y={418}><Quote size={72} fill={t.navy} color={t.navy} /></Abs>
      <Lines x={640} cy={526} lh={44} align="center" size={25.5} color="#555" lines={[<>{quote.body.plain}<span className="font-medium" style={{ color: t.text }}>{quote.body.strong}</span></>, <span className="font-medium" style={{ color: t.text }}>{quote.body.tail}</span>]} />
    </PageCard>
  )
}

function Keywords() {
  return (
    <PageCard page={keywords.page}>
      <Title text={keywords.title} cy={186} size={103} />
      {keywords.items.map((k, i) => {
        const x = 107 + i * 269, cx = x + 127
        return (
          <div key={k.name}>
            <Box x={x} y={276} w={254} h={344} bg={t.paper} style={{ border: `2px solid ${t.navy}` }} />
            <Box x={x} y={276} w={254} h={40} bg={t.pink} style={{ border: `2px solid ${t.navy}` }} />
            <Placeholder x={x + 13} y={254} w={44} h={54} r="22px" label="push pin" />
            <Lines x={cx} cy={381} align="center" w={254} size={47} className={t.display} color={t.navy} lines={[k.name]} />
            <Box x={x + 29} y={438} w={196} h={0} style={{ borderTop: `2px dotted ${t.navy}` }} />
            <Lines x={cx} cy={492} lh={34.5} align="center" w={254} size={25} color={t.text} lines={k.desc} />
          </div>
        )
      })}
    </PageCard>
  )
}

function TwoRow() {
  return (
    <PageCard page={twoRow.page} clip={false}>
      <Lines x={267} cy={262} lh={117.5} align="center" w={400} size={100} className={t.display} color={t.navy} lines={[twoRow.title[0], twoRow.title[1], <span style={{ color: t.pink }}>{twoRow.title[2]}</span>]} />
      {twoRow.blocks.map((b, i) => {
        const y = 138 + i * 260
        return (
          <div key={i}>
            <Box x={500} y={y} w={708} h={247} bg={t.paper} style={{ border: `2px solid ${t.navy}` }} />
            <Box x={500} y={y} w={15} h={247} bg={t.pink} style={{ border: `2px solid ${t.navy}` }} />
            <Lines x={573} cy={y + 57} size={34} className={t.display} color={t.navy} lines={[b.head]} />
            <Lines x={573} cy={y + 99} lh={32} size={21} color={t.text} lines={b.body} />
          </div>
        )
      })}
      <Abs x={1011} y={163}><Abs x={0} y={0}><Star cx={28} cy={28} size={56} fill="#fff" /></Abs></Abs>
      <Ring cx={1078} cy={138} />
      <Character cx={1188} cy={284} r={114} />
      <Character cx={1188} cy={469} r={114} />
      <Character cx={1188} cy={659} r={114} />
    </PageCard>
  )
}

function Photos() {
  const tints = [t.mint, '#fcc6d8', '#fffacd']
  return (
    <PageCard page={photos.page}>
      <Title text={photos.title} cy={181} size={90} />
      {photos.items.map((p, i) => {
        const x = 108 + i * 359, cx = x + 172
        return (
          <div key={i}>
            <Box x={x} y={263} w={345} h={356} bg={t.paper} style={{ border: `2px solid ${t.navy}` }} />
            <Box x={x} y={263} w={345} h={37} bg={t.pink} style={{ border: `2px solid ${t.navy}` }} />
            <Lines x={cx} cy={281} align="center" w={345} size={22} className="font-extrabold" color="#fff" lines={[p.head]} />
            <Placeholder x={x + 2} y={300} w={341} h={199} label={`photo (${tints[i]})`} />
            <Box x={x} y={499} w={345} h={2} bg={t.navy} />
            <Lines x={cx} cy={531} lh={28} align="center" w={345} size={20} color={t.text} lines={p.desc} />
          </div>
        )
      })}
    </PageCard>
  )
}

function Steps() {
  return (
    <PageCard page={steps.page}>
      <Title text={steps.title} cy={182} size={89} />
      {steps.items.map((s, i) => {
        const x = 107 + i * 269, cx = x + 127
        return (
          <div key={s.head}>
            <Box x={x} y={263} w={254} h={357} bg={t.paper} style={{ border: `2px solid ${t.navy}` }} />
            <Box x={x} y={263} w={254} h={16} bg={t.pink} style={{ border: `2px solid ${t.navy}` }} />
            <Abs x={cx - 99} y={299} w={199} h={122} className="rounded-[50%]" style={{ background: i % 2 ? t.mint : t.lemon, border: `2px solid ${t.navy}` }} />
            <Placeholder x={cx - 32} y={318} w={64} h={84} r="12px" label="hand counting icon" />
            <Box x={x + 29} y={442} w={196} h={0} style={{ borderTop: `2px dotted ${t.navy}` }} />
            <Lines x={cx} cy={483} align="center" w={254} size={31} className={t.display} color={t.navy} lines={[s.head]} />
            <Lines x={cx} cy={523} lh={27.5} align="center" w={254} size={19} color={t.text} lines={s.desc} />
          </div>
        )
      })}
    </PageCard>
  )
}

function Table() {
  const x0 = 175, cw = 227.25, rows = [363, 447, 533, 618]
  return (
    <PageCard page={table.page}>
      <Title text={table.title} cy={196} size={92} />
      <Lines x={640} cy={275} align="center" size={23} color={t.text} lines={[table.sub]} />
      <Box x={x0} y={321} w={cw * 4} h={297} bg={t.paper} style={{ border: `2px solid ${t.navy}` }} />
      <Box x={x0} y={321} w={cw * 4} h={42} bg={t.pink} style={{ border: `2px solid ${t.navy}`, borderBottom: 0 }} />
      {rows.slice(0, -1).map((y) => <Box key={y} x={x0} y={y} w={cw * 4} h={2} bg={t.navy} />)}
      {[1, 2, 3].map((i) => <Box key={i} x={x0 + i * cw} y={363} w={2} h={255} bg={t.navy} />)}
      {table.cols.map((c, i) => <Lines key={c} x={x0 + cw * (i + 0.5)} cy={342} align="center" w={cw} size={15} className="font-montserrat" color="#fff" lines={[c]} />)}
      {table.rows.map((r, ri) => r.map((cell, i) => cell && <Lines key={`${ri}-${i}`} x={x0 + cw * (i + 0.5)} cy={(rows[ri] + rows[ri + 1]) / 2} align="center" w={cw} size={20} color={t.text} lines={[cell]} />))}
      <Star cx={103} cy={208} size={70} fill={t.mint} />
      <Ring cx={150} cy={249} />
      <Star cx={1153} cy={616} size={66} fill="#fdd" />
      <Character cx={1240} cy={463} r={112} />
      <Character cx={45} cy={680} r={115} />
    </PageCard>
  )
}

function Closing() {
  return (
    <PageCard page={closing.page} clip={false}>
      <Placeholder x={0} y={135} w={125} h={47} r="0 24px 24px 0" label="paperclip" />
      <Lines x={640} cy={214} align="center" size={35} color={t.navy} lines={[closing.kicker]} />
      <Lines x={640} cy={318} align="center" size={156} className="font-pretendard font-extrabold tracking-[-0.045em]" color={t.navy} lines={[closing.title]} />
      <Character cx={337} cy={668} r={163} />
      <Character cx={650} cy={668} r={163} />
      <Character cx={950} cy={668} r={163} />
      <Bubble cx={729} cy={475} />
    </PageCard>
  )
}

const deck: DeckDefinition = { id: '08', title: '흰색과 파랑의 아기자기한 개인 프레젠테이션 게시글', slides: [Cover, Contents, QuotePage, Keywords, TwoRow, Photos, Steps, Table, Closing] }
export default deck
