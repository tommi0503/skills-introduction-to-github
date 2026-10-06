import type { DeckDefinition } from '../../ui'
import { Abs, ImagePlaceholder } from '../../ui'
import { Box, Lines } from '../../ui'
import { FolderSlide, Icon, LetterDot, Title } from './components'
import { chapter, closing, compare, contents, cover, keywords, longText, process, twoImages } from './data'
import { t } from './theme'

const Photo = ({ x, y, w, h }: { x: number; y: number; w: number; h: number }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label="photo" className="h-full w-full" /></Abs>
)

function Cover() {
  return (
    <FolderSlide headerH={132}>
      <Abs x={611 - 52} y={114} w={104} h={104} className="rounded-full bg-white" />
      <Icon k="book" cx={611} cy={164} size={62} stroke={1.3} />
      <Lines x={613} cy={308} lh={130} align="center" size={100} className={t.display} color={t.teal} lines={[cover.title[0]]} />
      <Lines x={611} cy={438} align="center" size={100} className={t.display} color={t.deep} lines={[cover.title[1]]} />
      <Box x={296} y={539} w={633} h={63} className="rounded-[10px]" style={{ background: `linear-gradient(90deg, ${t.slate}, #7898aa)` }} />
      <Box x={308} y={548} w={164} h={43} bg="#fff" className="rounded-lg" />
      <Lines x={390} cy={571} align="center" w={164} size={19} className="font-bold" color="#2b4a6b" lines={[cover.keyword]} />
      <Lines x={508} cy={569} size={25} className="font-medium" color="#fff" lines={[cover.keywordText]} />
    </FolderSlide>
  )
}

function Contents() {
  return (
    <FolderSlide page={contents.page}>
      <Lines x={611} cy={256} align="center" size={64} className="font-montserrat font-extrabold tracking-[0.01em]" color={t.deep} lines={[contents.title]} />
      {contents.items.map((it, i) => {
        const x = 79 + i * 216, cx = x + 101
        return (
          <div key={i}>
            <Box x={x} y={353} w={202} h={40} bg={t.teal} />
            <Lines x={cx} cy={373} align="center" w={202} size={15} color="#fff" lines={[String(i + 1)]} />
            <Box x={x} y={393} w={202} h={247} bg={t.card} />
            <Lines x={cx} cy={446} lh={27} align="center" w={202} size={20} className="font-bold" color={t.ink} lines={it.label} />
            <Abs x={cx - 47} y={567 - 47} w={94} h={94} className="rounded-full bg-white" />
            <Icon k={it.icon} cx={cx} cy={567} size={46} />
          </div>
        )
      })}
    </FolderSlide>
  )
}

function Chapter() {
  return (
    <FolderSlide page={chapter.page} overlay={<Box x={36} y={88} w={570} h={603} bg={t.slate} style={{ clipPath: 'polygon(0 0, 92% 39.5%, 100% 44%, 100% 100%, 0 100%)', borderRadius: '0 0 12px 0' }} />}>
      <Box x={89} y={341} w={125} h={40} bg="#fff" className="rounded-lg" />
      <Lines x={151} cy={361} align="center" w={125} size={18} className="font-medium" color={t.slate} lines={[chapter.pill]} />
      <Lines x={86} cy={432} lh={73} size={64} className={t.display} color="#fff" lines={chapter.title} />
      <Photo x={648} y={173} w={500} h={240} />
      {chapter.rows.map((r, i) => {
        const y = 424 + i * 83.6
        return (
          <div key={r.letter}>
            <Box x={648} y={y} w={44} h={75} bg={t.teal} />
            <Lines x={670} cy={y + 37} align="center" w={44} size={14} className="font-bold" color="#fff" lines={[r.letter]} />
            <Box x={692} y={y} w={456} h={75} bg={t.card} />
            <Lines x={717} cy={y + 37} size={19} color={t.text} lines={[<><b className="text-[#222]">{r.lead}</b>{r.text}</>]} />
          </div>
        )
      })}
    </FolderSlide>
  )
}

function LongText() {
  return (
    <FolderSlide page={longText.page}>
      <Title text={longText.title} x={118} cy={225} align="left" size={52} />
      <Lines x={545} cy={206} lh={25.5} size={16} color={t.text} lines={longText.body} />
      {longText.circles.map((c, i) => {
        const cx = [361, 611, 863][i]
        const fg = c.filled ? '#fff' : t.ink
        return (
          <div key={c.letter}>
            <Abs x={cx - 139} y={517 - 139} w={278} h={278} className="rounded-full" style={{ background: c.filled ? t.teal : t.card }} />
            <LetterDot cx={cx} cy={423} letter={c.letter} />
            <Icon k={c.icon} cx={cx} cy={484} size={46} color={c.filled ? '#fff' : '#777'} />
            <Lines x={cx} cy={542} align="center" w={260} size={21} className="font-bold" color={fg} lines={[c.title]} />
            <Lines x={cx} cy={576} lh={23} align="center" w={260} size={16} color={c.filled ? '#fff' : t.text} lines={c.desc} />
          </div>
        )
      })}
    </FolderSlide>
  )
}

function TwoImages() {
  return (
    <FolderSlide page={twoImages.page}>
      <Title text={twoImages.title} cy={216} />
      <Box x={77} y={288} w={1070} h={25} bg={t.teal} />
      <Box x={77} y={313} w={1070} h={344} bg={t.card} />
      {twoImages.items.map((it, i) => {
        const dx = i * 523
        return (
          <div key={it.letter}>
            <Photo x={106 + dx} y={337} w={252} h={296} />
            <LetterDot cx={397 + dx} cy={358} letter={it.letter} />
            <Lines x={378 + dx} cy={424} lh={31} size={21} className="font-bold" color={t.ink} lines={it.title} />
            <Lines x={378 + dx} cy={529} lh={22.7} size={16} color={t.text} lines={it.body} />
          </div>
        )
      })}
    </FolderSlide>
  )
}

function Compare() {
  return (
    <FolderSlide page={compare.page}>
      <Title text={compare.title} cy={216} />
      {compare.rows.map((r, i) => {
        const y = 286 + i * 122.4
        return (
          <div key={i}>
            <Box x={98} y={y} w={158} h={110} bg={t.teal} className="rounded-md" />
            <Icon k={r.icon} cx={177} cy={y + 42} size={36} color="#fff" />
            <Lines x={177} cy={y + 85} align="center" w={158} size={17} className="font-medium" color="#fff" lines={[r.key]} />
            <Lines x={287} cy={y + 17} size={14} color="#aaa" lines={[compare.labels[0]]} />
            <Lines x={1102} cy={y + 17} align="right" size={14} color="#aaa" lines={[compare.labels[1]]} />
            <Box x={268} y={y + 34} w={428} h={76} bg={t.before} />
            <Box x={696} y={y + 34} w={430} h={76} bg={t.after} />
            <Lines x={289} cy={y + 71} size={19} className="font-bold" color={t.ink} lines={[r.before]} />
            <Lines x={1102} cy={y + 71} align="right" size={19} className="font-bold" color={t.ink} lines={[r.after]} />
          </div>
        )
      })}
    </FolderSlide>
  )
}

function Keywords() {
  return (
    <FolderSlide page={keywords.page}>
      <Title text={keywords.title} cy={217} />
      {keywords.items.map((it, i) => {
        const right = i % 2 === 1, y = i < 2 ? 285 : 477
        const x = right ? 617 : 95
        const tx = right ? 843 : 379
        const align = right ? 'right' : 'left'
        return (
          <div key={it.letter}>
            <Box x={x} y={y} w={512} h={180} bg={t.card} />
            <Box x={right ? x + 503 : x} y={y} w={9} h={180} bg="#c8c8ca" />
            <Photo x={right ? 864 : 114} y={y + 9} w={244} h={162} />
            <LetterDot cx={right ? 821 : 398} cy={y + 34} letter={it.letter} />
            <Lines x={tx} cy={y + 86} align={align} w={420} size={19} className="font-bold" color={t.ink} lines={[it.title]} />
            <Lines x={tx} cy={y + 128} lh={26} align={align} w={420} size={16} color={t.text} lines={it.bullets} />
          </div>
        )
      })}
    </FolderSlide>
  )
}

function Process() {
  return (
    <FolderSlide page={process.page}>
      <Title text={process.title} x={330} cy={252} size={52} />
      <Photo x={118} y={389} w={418} h={247} />
      <Box x={610} y={226} w={1.5} h={308} bg="#ccc" />
      {process.steps.map((s) => {
        const big = s.letter === 'D'
        return (
          <div key={s.letter}>
            {big ? (
              <>
                <Abs x={611 - 51} y={s.cy - 51} w={102} h={102} className="rounded-full" style={{ background: t.teal }} />
                <Lines x={611} cy={s.cy - 31} align="center" w={40} size={14} className="font-bold" color="#fff" lines={[s.letter]} />
                <Icon k="book" cx={611} cy={s.cy + 8} size={34} color="#fff" />
              </>
            ) : (
              <>
                <Abs x={611 - 22} y={s.cy - 22} w={44} h={44} className="rounded-full" style={{ background: '#a5a5a7' }} />
                <Lines x={611} cy={s.cy} align="center" w={40} size={13} className="font-bold" color="#fff" lines={[s.letter]} />
              </>
            )}
            <Lines x={681} cy={big ? s.cy - 37 : s.cy + 1} size={20} className="font-bold" color={big ? t.deep : t.ink} lines={[s.title]} />
            <Lines x={681} cy={big ? s.cy - 6 : s.cy + 32} lh={21.5} size={16} color={t.text} lines={s.desc} />
          </div>
        )
      })}
    </FolderSlide>
  )
}

function Closing() {
  return (
    <FolderSlide overlay={<><Box x={28} y={32} w={1003} h={668} bg={t.slate} className="rounded-r-2xl" /><Box x={28} y={32} w={27} h={668} bg={t.slateLight} /></>}>
      <Abs x={521 - 41} y={237 - 41} w={82} h={82} className="rounded-full bg-white" />
      <Icon k="book" cx={521} cy={237} size={46} color={t.slate} />
      <Lines x={521} cy={358} align="center" size={100} className={t.display} color="#fff" lines={[closing.title]} />
      <Lines x={521} cy={447} align="center" size={17} color="#fff" lines={[closing.sub]} />
      <Lines x={521} cy={535} align="center" size={20} className="font-bold" color="#fff" lines={[closing.org]} />
      <Lines x={521} cy={574} lh={25} align="center" size={16} color="#fff" lines={closing.contact} />
    </FolderSlide>
  )
}

const deck: DeckDefinition = { id: '05', title: '하늘색과 회색의 심플한 교육 소개서', slides: [Cover, Contents, Chapter, LongText, TwoImages, Compare, Keywords, Process, Closing] }
export default deck
