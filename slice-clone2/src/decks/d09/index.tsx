import type { ComponentType } from 'react'
import type { DeckDefinition } from '../../ui'
import { Abs, Slide } from '../../ui'
import { Asterisk, X } from 'lucide-react'
import { Box, Lines } from '../../ui'
import { Answer, Art, Bubble, NoteSlide, Pill, QuizFrame } from './components'
import { countdown, cover, ending, prize, quizzes, ready, rules } from './data'
import { t } from './theme'

function Cover() {
  return (
    <NoteSlide>
      <Bubble x={520} y={198} w={256} h={87} text={cover.bubble} size={40} tailX={548} />
      <Lines x={381} cy={399} align="center" w={400} size={150} className={t.bold} color={t.ink} lines={[cover.title[0]]} />
      <Lines x={898} cy={399} align="center" w={400} size={150} className={t.bold} color={t.ink} lines={[cover.title[1]]} />
      <Art x={549} y={332} w={185} h={174} label="reading bear doodle" />
      <Art x={112} y={417} w={106} h={95} r="50%" label="sun doodle" />
      <Art x={829} y={152} w={98} h={144} label="music notes doodle" />
      <Art x={1066} y={381} w={92} h={38} label="swirl doodle" />
      <Box x={221} y={524} w={840} h={82} bg={t.beige} className="rounded-full" />
      <Lines x={250} cy={564} size={28} className={t.bold} color={t.ink} lines={[cover.memo]} />
      <Lines x={448} cy={564} size={32} color={t.ink} lines={[cover.memoText]} />
    </NoteSlide>
  )
}

function Rules() {
  return (
    <NoteSlide>
      <Pill x={131} y={166} w={1017} h={129} size={90}>{rules.title}</Pill>
      {[212, 1074].map((cx) => <Abs key={cx} x={cx - 34} y={195}><Asterisk size={68} strokeWidth={4} color={t.ink} /></Abs>)}
      {rules.rows.map(([n, text], i) => {
        const cy = 385 + i * 99.5
        return (
          <div key={n}>
            <Lines x={207} cy={cy} size={56} color={t.ink} lines={[n]} />
            <Lines x={693} cy={cy} align="center" w={700} size={46} color={t.ink} lines={[text]} />
            <Box x={190} y={cy + 47} w={898} h={2.5} bg="#333" />
          </div>
        )
      })}
      <Art x={1064} y={540} w={116} h={130} label="bunny doodle" />
    </NoteSlide>
  )
}

function Ready() {
  return (
    <NoteSlide>
      <Lines x={640} cy={288} align="center" size={37.5} color={t.grey} lines={[ready.kicker]} />
      <Lines x={640} cy={396} align="center" size={85} className={t.bold} color={t.ink} lines={[ready.title]} />
      <Box x={196} y={458} w={887} h={16} bg={t.ink} className="rounded-full" />
      <Art x={979} y={249} w={71} h={69} label="star doodle" />
    </NoteSlide>
  )
}

const Count = ({ i }: { i: number }) => {
  const c = countdown[i]
  return (
    <NoteSlide>
      <Art {...c.art} label="person illustration" />
      <Art x={683} y={163} w={456} h={459} r="50%" label="flower blob" tone="#f3efeb" />
      <Lines x={912} cy={383} align="center" w={300} size={300} className={t.bold} color={t.ink} lines={[c.n]} />
      <Abs x={1055} y={193} w={50} h={48} className="rounded-full" style={{ background: t.ink }} />
      <Abs x={701} y={403} w={56} h={50} className="rounded-full" style={{ background: '#999' }} />
      <Art x={1060} y={505} w={95} h={80} label="swirl doodle" />
    </NoteSlide>
  )
}
const counts = countdown.map((_, i) => () => <Count i={i} />) as ComponentType[]

function PhotoQuiz() {
  return (
    <QuizFrame q={quizzes.photo.q} tag={quizzes.photo.tag}>
      <Box x={174} y={299} w={640} h={340} style={{ border: `3px solid ${t.ink}` }}><Art x={0} y={0} w={634} h={334} r="0" label="photo" /></Box>
    </QuizFrame>
  )
}

const PhotoAnswer = () => <QuizFrame q={quizzes.photo.q} tag={quizzes.photo.tag}><Answer text={quizzes.photo.answer} /></QuizFrame>

function OX({ reveal = false }: { reveal?: boolean }) {
  const dim = reveal ? '#ddd' : t.ink
  return (
    <QuizFrame q={quizzes.ox.q} tag={quizzes.ox.tag} bubbleX={912} bubbleW={252}>
      <Box x={176} y={315} w={303} h={293} bg={t.page} style={{ border: `3px solid ${dim}` }} />
      <Abs x={327 - 71} y={462 - 71} w={142} h={142} className="rounded-full" style={{ border: `30px solid ${dim}` }} />
      <Box x={522} y={315} w={303} h={293} bg={t.page} style={{ border: `3px solid ${t.ink}` }} />
      <Abs x={514} y={352}><X size={220} strokeWidth={2.6} color={t.ink} /></Abs>
    </QuizFrame>
  )
}
const OXQuiz = () => <OX />
const OXAnswer = () => <OX reveal />

function WordQuiz() {
  const q = quizzes.word
  return (
    <QuizFrame q={q.q} tag={q.tag} bubbleX={912} bubbleW={252}>
      {q.hints.map(([k, v], i) => (
        <div key={k}>
          <Lines x={183} cy={402 + i * 112} size={46} color={t.ink} lines={[k]} />
          <Lines x={343} cy={402 + i * 112} size={46} color={t.ink} lines={[v]} />
          <Box x={154} y={452 + i * 115} w={731} h={2.5} bg="#333" />
        </div>
      ))}
    </QuizFrame>
  )
}
const WordAnswer = () => <QuizFrame q={quizzes.word.q} tag={quizzes.word.tag} bubbleX={912} bubbleW={252}><Answer text={quizzes.word.answer} x={435} /></QuizFrame>

function SoundQuiz() {
  const q = quizzes.sound
  return (
    <QuizFrame q={q.q} tag={q.tag} bubbleX={893} bubbleW={279}>
      <Box x={152} y={299} w={677} h={352} style={{ border: `3px solid ${t.ink}` }} />
      <Art x={361} y={343} w={250} h={268} r="125px 125px 30px 30px" label="person silhouette" tone={t.sand} />
      <Lines x={486} cy={470} align="center" w={200} size={250} className={t.bold} color={t.ink} lines={['?']} />
    </QuizFrame>
  )
}
const SoundAnswer = () => <QuizFrame q={quizzes.sound.q} tag={quizzes.sound.tag} bubbleX={893} bubbleW={279}><Answer text={quizzes.sound.answer} x={370} /></QuizFrame>

function Ending() {
  const lines = [[125, 352, 261, 537], [252, 470, 323, 586], [1148, 377, 1055, 494], [1053, 454, 952, 575]]
  return (
    <NoteSlide>
      <Pill x={400} y={200} w={479} h={91} size={35} className={t.light}>{ending.pill}</Pill>
      <Lines x={640} cy={375} lh={110} align="center" size={84} className={t.bold} color={t.ink} lines={ending.title} />
      <svg className="absolute left-0 top-0" width={1280} height={720}>
        {lines.map(([x1, y1, x2, y2], i) => <line key={i} x1={x1} y1={y1} x2={x2} y2={y2} stroke={t.ink} strokeWidth={5} strokeLinecap="round" />)}
      </svg>
      <Abs x={163} y={156}><Asterisk size={72} strokeWidth={4} color={t.ink} /></Abs>
      <Abs x={793} y={594} w={56} h={56} className="rounded-full" style={{ background: t.ink }} />
      <Art x={1018} y={302} w={78} h={78} r="50%" label="sparkle doodle" tone="#eeeae6" />
      <Art x={160} y={300} w={40} h={36} r="50%" label="sparkle doodle" tone={t.sand} />
      <Art x={168} y={567} w={40} h={40} r="50%" label="sparkle doodle" tone="#eeeae6" />
      <Art x={1027} y={570} w={46} h={44} r="50%" label="sparkle doodle" tone={t.sand} />
    </NoteSlide>
  )
}

function Prize() {
  return (
    <Slide background="#000" className={t.light} style={{ color: t.ink }}>
      <Box x={38} y={28} w={1214} h={672} bg={t.page} style={{ border: '5px solid #c8c8c8' }} />
      <Art x={130} y={210} w={435} h={395} label="celebrating person illustration" />
      <Art x={172} y={95} w={368} h={115} r="50% 50% 0 0" label="curved Congratulations lettering" />
      <Art x={580} y={90} w={600} h={550} r="50%" label="flower blob" tone="#f3efeb" />
      <Lines x={878} cy={290} align="center" size={26} color={t.ink} lines={[prize.kicker]} />
      <Lines x={878} cy={365} lh={68} align="center" size={52} className={t.bold} color={t.ink} lines={prize.title} />
    </Slide>
  )
}

const deck: DeckDefinition = {
  id: '09',
  title: '검정 아기자기한 퀴즈 게임 안내',
  slides: [Cover, Rules, Ready, ...counts, PhotoQuiz, PhotoAnswer, OXQuiz, OXAnswer, WordQuiz, WordAnswer, SoundQuiz, SoundAnswer, Ending, Prize],
}
export default deck
