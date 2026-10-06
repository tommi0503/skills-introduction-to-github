import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { Box, Lines } from '../../ui'
import { BlobSlide, Dots, Header, ICONS, Photo, SideIntro, Small } from './components'
import { cover, fourIcons, fourPhotos, index, keywords, longText, section, sixList, twoPhotos } from './data'
import { t } from './theme'

function Cover() {
  return (
    <BlobSlide panel={cover.panel} deco={cover.deco}>
      <Lines x={653} cy={234} align="center" size={111} className="font-poppins font-bold tracking-[-0.03em]" color={t.lavender} lines={[cover.title[0]]} />
      <Lines x={653} cy={354} align="center" size={111} className="font-poppins font-bold tracking-[-0.03em]" color="#555" lines={[cover.title[1]]} />
      <Dots x={187} y={474} w={901} color="#bbb" />
      <Lines x={669} cy={533} align="center" size={37} color={t.text} lines={[cover.sub]} />
      {[418, 919].map((x) => <Lines key={x} x={x} cy={535} align="center" w={30} size={22} color={t.lavender} lines={['✦']} />)}
    </BlobSlide>
  )
}

function Index() {
  return (
    <BlobSlide panel={index.panel} deco={index.deco}>
      <Lines x={640} cy={184} align="center" size={87} className={t.head} color={t.ink} lines={[index.title]} />
      <Dots x={187} y={248} w={901} />
      {index.items.map((it, i) => {
        const col = Math.floor(i / 3), row = i % 3
        const cx = col ? 698 : 301, y = 337 + row * 109
        return (
          <div key={it.n}>
            <Abs x={cx - 27} y={y - 27} w={54} h={54} className="rounded-full" style={{ background: t.ink }} />
            <Lines x={cx} cy={y} align="center" w={54} size={15} className="font-poppins font-bold" color="#fff" lines={[it.n]} />
            <Lines x={cx + 47} cy={y - 16} size={24} className={t.head} color={t.ink} lines={[it.title]} />
            <Small x={cx + 47} cy={y + 19} align="left" size={14.5} lines={[it.sub]} />
          </div>
        )
      })}
    </BlobSlide>
  )
}

function Keywords() {
  return (
    <BlobSlide panel={keywords.panel} deco={keywords.deco}>
      <Header badge={keywords.badge} title={keywords.title} />
      {keywords.items.map((k) => {
        const Icon = ICONS[k.icon as keyof typeof ICONS]
        const [x, y, w, h] = k.blob
        return (
          <div key={k.cx}>
            <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label="organic icon blob" className="h-full w-full" style={{ borderRadius: '48% 52% 45% 55% / 55% 50% 50% 45%' }} /></Abs>
            <Abs x={x + w / 2 - 36} y={y + h / 2 - 36}><Icon size={72} strokeWidth={1.2} color="#666" /></Abs>
            <Lines x={k.cx} cy={495} align="center" w={300} size={26} className="font-medium" color={t.ink} lines={[k.name]} />
            <Small x={k.cx} cy={535} lh={24.5} size={15} w={300} lines={k.desc} />
          </div>
        )
      })}
    </BlobSlide>
  )
}

function TwoPhotos() {
  return (
    <BlobSlide panel={twoPhotos.panel} deco={twoPhotos.deco}>
      <Header badge={twoPhotos.badge} title={twoPhotos.title} rule={[252, 1142]} />
      {twoPhotos.items.map((p) => (
        <div key={p.x}>
          <Photo x={p.x} y={227} w={462} h={259} />
          <Box x={p.x} y={495} w={462} h={118} bg={t.card} />
          <Box x={p.x + 95} y={455} w={272} h={42} bg="#fff" className="rounded-t-2xl" />
          <Lines x={p.x + 231} cy={481} align="center" w={272} size={21} className={t.head} color={t.ink} lines={[p.tab]} />
          <Small x={p.x + 231} cy={526} lh={23.5} size={13.5} w={462} lines={p.caption} />
        </div>
      ))}
    </BlobSlide>
  )
}

function FourIcons() {
  return (
    <BlobSlide panel={fourIcons.panel} deco={fourIcons.deco}>
      <Header badge={fourIcons.badge} title={fourIcons.title} x={420} />
      {fourIcons.items.map((it, i) => {
        const x = i % 2 ? 644 : 141, y = i < 2 ? 236 : 434
        const Icon = ICONS[it.icon]
        return (
          <div key={i}>
            <Box x={x} y={y} w={495} h={189} bg={t.card} className="rounded-lg" />
            <Abs x={x + 48} y={y + 40} w={108} h={108} className="rounded-full bg-white" />
            <Abs x={x + 80} y={y + 72}><Icon size={44} strokeWidth={1.3} color="#444" /></Abs>
            <Lines x={x + 185} cy={y + 54} size={22} className={t.head} color={t.ink} lines={[it.title]} />
            <Small x={x + 185} cy={y + 89} align="left" lh={24.5} size={14.5} lines={it.desc} />
          </div>
        )
      })}
    </BlobSlide>
  )
}

function Section() {
  return (
    <BlobSlide panel={section.panel} deco={section.deco}>
      {/* big numeral as SVG text: its box is the glyph run, so it doesn't swallow the title below */}
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        <text x={640} y={304} textAnchor="middle" fontSize={192} fontWeight={700} letterSpacing="-0.02em" fill={t.ink} className="font-montserrat">{section.n}</text>
      </svg>
      <Lines x={640} cy={369} align="center" size={37} className={t.head} color={t.ink} lines={[section.title]} />
      {section.points.map((p, i) => {
        const cy = [437, 496, 558][i]
        return (
          <div key={p.n}>
            <Abs x={468 - 16} y={cy - 16} w={32} h={32} className="rounded-full" style={{ background: t.ink }} />
            <Lines x={468} cy={cy} align="center" w={32} size={10.5} className="font-poppins font-bold" color="#fff" lines={[p.n]} />
            <Lines x={496} cy={cy} size={19.5} color={t.text} lines={[p.text]} />
            {i < 2 && <Dots x={453} y={cy + 26} w={374} />}
          </div>
        )
      })}
    </BlobSlide>
  )
}

function FourPhotos() {
  return (
    <BlobSlide panel={fourPhotos.panel} deco={fourPhotos.deco}>
      <Header badge={fourPhotos.badge} title={fourPhotos.title} rule={[131, 1023]} />
      {fourPhotos.items.map((it, i) => {
        const x = 166 + i * 240.1, cx = x + 113
        return (
          <div key={i}>
            <Photo x={x} y={230} w={226} h={242} r="113px 113px 0 0" />
            <Box x={x} y={472} w={226} h={156} bg={t.card} />
            <Lines x={cx} cy={509} align="center" w={226} size={20} className={t.head} color={t.ink} lines={[it.title]} />
            <Box x={x + 30} y={527} w={166} h={0} style={{ borderTop: '1px dashed #c9b9a8' }} />
            <Small x={cx} cy={549} size={13.5} w={226} lines={it.desc} />
          </div>
        )
      })}
    </BlobSlide>
  )
}

function LongText() {
  return (
    <BlobSlide panel={longText.panel} deco={longText.deco}>
      <SideIntro badge={longText.badge} title={longText.title} desc={longText.desc} />
      <Photo x={484} y={149} w={662} h={317} />
      <Abs x={462} y={521} w={90} h={48}><ImagePlaceholder label="mint cloud" className="h-full w-full rounded-full" /></Abs>
      <Lines x={503} cy={555} size={16.5} className="font-medium" color={t.ink} lines={[longText.keyword]} />
      <Small x={613} cy={509} align="left" lh={27} size={13.5} w={600} lines={longText.body} />
    </BlobSlide>
  )
}

function SixList() {
  return (
    <BlobSlide panel={sixList.panel} deco={sixList.deco}>
      <SideIntro badge={sixList.badge} title={sixList.title} desc={sixList.desc} />
      {sixList.items.map((it, i) => {
        const cy = 156 + i * 82.4
        return (
          <div key={it.n}>
            <Box x={473} y={cy - 33} w={676} h={66} bg={t.card} className="rounded-full" />
            <Abs x={506 - 33} y={cy - 33} w={66} h={66} className="rounded-full" style={{ background: t.rose }} />
            <Lines x={506} cy={cy} align="center" w={66} size={19} className="font-poppins font-semibold" color={t.ink} lines={[it.n]} />
            <Lines x={560} cy={cy} size={19.5} color={t.text} lines={[it.text]} />
          </div>
        )
      })}
    </BlobSlide>
  )
}

const deck: DeckDefinition = { id: '10', title: '회색의 아기자기한 비즈니스 기획서', slides: [Cover, Index, Keywords, TwoPhotos, FourIcons, Section, FourPhotos, LongText, SixList] }
export default deck
