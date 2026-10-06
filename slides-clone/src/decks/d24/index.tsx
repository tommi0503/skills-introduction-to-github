import { Abs, Slide, type DeckDefinition } from '../../ui'
import { theme } from './theme'
import { heading, questions, footer } from './data'
import { QuestionCard, NoticeBar } from './components'

function Questions() {
  return (
    <Slide background={theme.page} className="font-pretendard">
      <Abs x={61} y={48} w={1158} h={624} className="rounded-xl bg-white shadow-[0_6px_24px_rgba(0,0,0,0.08)]" />
      <Abs x={61} y={48} w={1158} h={52} className="rounded-t-xl" style={{ background: theme.blue }} />
      {[102, 640, 1176].map((x) => <Abs key={x} x={x - 5} y={70} w={10} h={10} className="rounded-full bg-white/70" />)}
      <Abs x={0} y={125} w={1280} className="flex items-center justify-center gap-4 text-[50px] font-extrabold" style={{ color: theme.ink }}>
        <span className="flex size-[44px] items-center justify-center rounded-full bg-white text-[20px] font-bold" style={{ border: `2px solid ${theme.blue}`, color: theme.blueText }}>{heading.num}</span>
        <span>{heading.plain} <span style={{ color: theme.blueText }}>{heading.accent}</span></span>
      </Abs>
      <Abs x={1010} y={128} w={13} h={13} className="rounded-full" style={{ background: theme.blue }} />
      {questions.map((q) => <QuestionCard key={q.q} {...q} />)}
      <NoticeBar text={footer} />
    </Slide>
  )
}

const deck: DeckDefinition = { id: '24', title: '상담교사의 고민과 질문들', slides: [Questions] }
export default deck
