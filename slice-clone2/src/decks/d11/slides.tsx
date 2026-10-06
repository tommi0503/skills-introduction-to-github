import { Database, CloudDownload, FileCheck, Settings, Globe, LockKeyholeOpen, Lightbulb, Send, FileCog, MousePointerClick, Blend, Presentation, FolderDown, Handshake } from 'lucide-react'
import { Abs, cn } from '../../ui'
import { ChapterRule, Disc, Folder, FolderCard, Heading, Lines, Photo, SerifPill, T } from './components'
import { contents, cover, fourKeys, longText, process, summary, thanks, threeKeys, twoImages } from './data'
import { t } from './theme'

/** Per-deck tuning knobs so sibling decks (d15) can reuse these layouts. */
export interface V {
  /** title font size */ ts?: number
  /** centre the kicker + title over the sheet */ center?: boolean
  /** shift heading block vertically */ dy?: number
  /** shift body block vertically */ by?: number
  /** generic x shift / size tweaks */ dx?: number
  bs?: number
  /** keyword-strip shift (LongText) */ ky?: number
  /** secondary text size */ bs2?: number
}
const H = (v: V, kicker: string, title: string, y: number, x = 101) =>
  v.center ? <Heading kicker={kicker} title={title} y={y + (v.dy ?? 0)} x={49} w={1127} align="center" size={v.ts} /> : <Heading kicker={kicker} title={title} y={y + (v.dy ?? 0)} x={x} size={v.ts} />

export const ch = (n: number) => `Chapter ${String(n).padStart(2, '0')}`

export function Cover({ data = cover, v = {} }: { data?: typeof cover; v?: V }) {
  return (
    <Folder cover>
      <Abs x={107} y={116 + (v.dy ?? 0)} className={cn(t.serif, 'whitespace-nowrap font-semibold')} style={{ fontSize: v.ts ?? 134, lineHeight: '109px', color: t.ink, letterSpacing: '-0.005em' }}>{data.title[0]}<br />{data.title[1]}</Abs>
      <Abs x={100} y={359} w={946} h={2} style={{ background: '#c0b8b0' }} />
      <T x={120} y={381} size={29} style={{ color: '#585048' }}>{data.sub}</T>
      {data.contacts.map(([k, v], i) => (
        <T key={k} x={i % 2 ? 857 : 665} y={i < 2 ? 610 : 640} size={16} style={{ color: '#686058', letterSpacing: '0.02em' }}><b className="font-semibold">{k}</b> {v}</T>
      ))}
    </Folder>
  )
}

export function Contents({ data = contents, v = {} }: { data?: typeof contents; v?: V }) {
  return (
    <Folder>
      <Abs x={49} y={300} w={560} h={398} style={{ background: '#f3f1ec', clipPath: 'polygon(0 0, 100% 100%, 0 100%)' }} />
      <ChapterRule label="Chapter 00" />
      <T x={139} y={186} size={75.5} className={cn(t.serif, 'font-semibold')} style={{ color: t.ink }}>{data.title}</T>
      <Abs x={608} y={165} w={1} h={467} style={{ background: t.rule }} />
      <Lines x={620} y={196} w={502} size={16} lh={27} align="right" lines={data.intro} style={{ color: t.body }} />
      {data.items.map((it, i) => {
        const y = 306 + i * 58.8
        return (
          <div key={it}>
            <SerifPill x={673 + (v.dx ?? 0)} y={y} w={113} h={33} radius={0} text={ch(i + 1)} />
            <Abs x={800 + (v.dx ?? 0)} y={y + 16} w={112} h={1} style={{ background: t.rule }} />
            <T x={822} y={y + 7} w={300} size={19.5} align="right" style={{ color: t.ink }}>{it}</T>
          </div>
        )
      })}
    </Folder>
  )
}

const ltIcons = [Globe, LockKeyholeOpen]
export function LongText({ chapter = ch(1), data = longText, v = {} }: { chapter?: string; data?: typeof longText; v?: V }) {
  return (
    <Folder chapter={chapter}>
      {H(v, data.kicker, data.title, 188)}
      <Lines x={100} y={290 + (v.by ?? 0)} w={v.dx ?? 521} size={v.bs ?? 16} lh={25.5} lines={data.body} justify style={{ color: t.body }} />
      <FolderCard x={101} y={474 + (v.by ?? 0)} w={523} h={174 - (v.by ?? 0)} tabW={115} tabH={10} />
      <Abs x={362} y={497 + (v.ky ?? 0)} w={1} h={131} style={{ background: '#d0ccc6' }} />
      {data.keys.map((k, i) => {
        const cx = [233, 489][i], Icon = ltIcons[i]
        return (
          <div key={k.k}>
            <T x={cx - 80} y={501 + (v.ky ?? 0)} w={160} size={13.5} align="center" className={t.serif} style={{ color: t.ink }}>{k.k}</T>
            <Abs x={cx - 21} y={538 + (v.ky ?? 0)}><Icon size={42} strokeWidth={1} color={t.ink} /></Abs>
            <T x={cx - 120} y={606 + (v.ky ?? 0)} w={240} size={15.5} align="center" style={{ color: t.ink }}>{k.text}</T>
          </div>
        )
      })}
      <Photo x={652} y={144 + (v.dy ?? 0) / 2} w={487} h={504 - (v.dy ?? 0) / 2} />
    </Folder>
  )
}

export function TwoImages({ chapter = ch(2), v = {} }: { chapter?: string; v?: V }) {
  return (
    <Folder chapter={chapter}>
      {H(v, twoImages.kicker, twoImages.title, 157)}
      {twoImages.cards.map((c, i) => {
        const x = [100, 627][i], w = [477, 488][i]
        return (
          <div key={c.k}>
            <FolderCard x={x} y={252} w={w} h={399} tab="right" tabW={167} tabH={16} bg={i ? t.cardGrey : t.cardWarm} />
            <Photo x={x + 9} y={268} w={w - 26} h={246} />
            <Abs x={x + w + 1} y={300} className={t.serif} style={{ writingMode: 'vertical-rl', fontSize: 13.5, color: t.ink }}>{c.k}</Abs>
            <T x={x + 9} y={540} w={w - 26} size={19} align="center" className="font-semibold">{c.head}</T>
            <Lines x={x + 9} y={580} w={w - 26} size={15.5} lh={25} align="center" lines={c.body} style={{ color: t.body }} />
          </div>
        )
      })}
    </Folder>
  )
}

const fkIcons = [Lightbulb, Send, FileCog, MousePointerClick]
const fkBg = [t.stone, t.cream, t.blush, '#ebebe9']
export function FourKeys({ chapter = ch(3), v = {} }: { chapter?: string; v?: V }) {
  return (
    <Folder chapter={chapter}>
      {H(v, fourKeys.kicker, fourKeys.title, 157)}
      <Abs x={444} y={283} w={343} h={343} className="overflow-hidden rounded-full"><Photo x={0} y={0} w={343} h={343} /></Abs>
      {fourKeys.items.map((it, i) => {
        const right = i % 2 === 1, cx = right ? 767 : 459, cy = i < 2 ? 361 : 546, ty = i < 2 ? 309 : 501
        const Icon = fkIcons[i]
        return (
          <div key={it.k}>
            <Disc cx={cx} cy={cy} r={78} bg={fkBg[i]}>
              <span className={cn(t.serif, 'leading-none')} style={{ fontSize: 13.5, color: t.ink }}>{it.k}</span>
              <Icon size={42} strokeWidth={1} color={t.ink} className="mt-[14px]" />
            </Disc>
            <T x={right ? 860 : 67} y={ty} w={right ? undefined : 300} size={19.5} align={right ? 'left' : 'right'} className="font-semibold">{it.head}</T>
            <Lines x={right ? 860 : 67} y={ty + 40} w={right ? undefined : 300} size={16} lh={27} align={right ? 'left' : 'right'} lines={it.body} style={{ color: t.body }} />
          </div>
        )
      })}
    </Folder>
  )
}

const tkIcons = [Database, CloudDownload, Settings]
const tkBg = [t.cardWarm, '#f4f0ec', t.cardGrey]
export function ThreeKeys({ chapter = ch(4), v = {} }: { chapter?: string; v?: V }) {
  return (
    <Folder chapter={chapter}>
      {H(v, threeKeys.kicker, threeKeys.title, 157)}
      {threeKeys.items.map((it, i) => {
        const x = 98 + i * 349
        const Icon = tkIcons[i]
        return (
          <div key={it.k}>
            <FolderCard x={x} y={290} w={329} h={358} tabW={136} tabH={17} bg={tkBg[i]} />
            <T x={x + 34} y={293} size={13.5} className={t.serif} style={{ color: t.ink }}>{it.k}</T>
            <Abs x={x + 142} y={372}><Icon size={46} strokeWidth={1} color={t.ink} /></Abs>
            <T x={x} y={464} w={329} size={19} align="center" className="font-semibold">{it.head}</T>
            <Abs x={x + 18} y={510} w={293} h={1} style={{ background: '#d0ccc6' }} />
            <Lines x={x} y={533} w={329} size={15.5} lh={25.5} align="center" lines={it.body} style={{ color: t.body }} />
          </div>
        )
      })}
    </Folder>
  )
}

const prIcons = [FileCheck, Blend, Presentation, FolderDown, Handshake]
const prBg = [t.stone, t.cream, t.blush, '#ebebe9', '#ebebe9']
export function Process({ chapter = ch(5), v = {} }: { chapter?: string; v?: V }) {
  return (
    <Folder chapter={chapter}>
      <Abs x={49} y={125} w={1127} h={254} style={{ background: t.band }} />
      <Photo x={87} y={139} w={520} h={220} />
      {H(v, process.kicker, process.title, 212, 646)}
      <Lines x={646} y={292} size={16} lh={26.5} lines={process.body} style={{ color: t.body }} />
      <Abs x={186} y={508} w={850} h={1} style={{ background: '#d8d4ce' }} />
      {process.steps.map((s, i) => {
        const cx = 186 + i * 212.5, big = i === 4, Icon = prIcons[i]
        return (
          <div key={s.step}>
            <T x={cx - 50} y={437} w={100} size={13.5} align="center" className={t.serif} style={{ color: t.ink }}>{s.step}</T>
            <Disc cx={cx} cy={big ? 492 : 508} r={big ? 78 : 43} bg={prBg[i]}><Icon size={big ? 44 : 34} strokeWidth={1} color={t.ink} className={big ? 'mt-[10px]' : ''} /></Disc>
            <T x={cx - 100} y={586} w={200} size={17.5} align="center" className="font-semibold">{s.head}</T>
            <T x={cx - 100} y={619 + (v.by ?? 0)} w={200} size={v.bs ?? 15.5} align="center" style={{ color: t.body }}>{s.sub}</T>
          </div>
        )
      })}
    </Folder>
  )
}

export function Summary({ chapter = ch(6), v = {} }: { chapter?: string; v?: V }) {
  return (
    <Folder chapter={chapter}>
      {H(v, summary.kicker, summary.title, 188)}
      {summary.rows.map((r, i) => {
        const cy = 371 + i * 63.2
        return (
          <div key={r.k}>
            <SerifPill x={101} y={cy - 16} w={112} text={r.k} />
            <T x={230} y={cy - 9} size={v.bs ?? 17} className="font-medium" style={{ color: '#504c48' }}>{r.text}</T>
            <Abs x={101} y={cy + 24} w={599} h={1} style={{ background: t.rule }} />
          </div>
        )
      })}
      <Photo x={725} y={165} w={412} h={486} />
    </Folder>
  )
}

export function Thanks({ data = thanks, v = {} }: { data?: typeof thanks; v?: V }) {
  return (
    <Folder cover>
      <T x={116} y={108} size={v.bs ?? 32.8} style={{ color: '#585048' }}>{data.sub}</T>
      <T x={117} y={156 + (v.dy ?? 0)} size={v.ts ?? 136} className={cn(t.serif, 'font-semibold')} style={{ color: t.ink, fontVariantLigatures: 'none' }}>{data.title}</T>
      <Lines x={116} y={306} size={v.bs2 ?? 21.2} lh={36} lines={data.body} style={{ color: '#686058' }} />
      <T x={116} y={555} size={20} className={cn(t.serif, 'font-semibold')} style={{ color: t.ink }}>{data.contact}</T>
      <Abs x={117} y={589} w={950} h={1} style={{ background: '#b8b0a8' }} />
      {data.cols.map(([k, v], i) => {
        const x0 = [117, 440, 766][i], x1 = [414, 731, 1062][i]
        return (
          <div key={k}>
            {i > 0 && <Abs x={x0 - 11} y={589} w={1} h={52} style={{ background: '#c8c0b8' }} />}
            <T x={x0} y={599} size={13} className={t.serif} style={{ color: t.ink }}>{k}</T>
            <T x={x1 - 300} y={628} w={300} size={21} align="right" className={cn(t.serif, "font-medium")} style={{ color: t.ink }}>{v}</T>
          </div>
        )
      })}
    </Folder>
  )
}
