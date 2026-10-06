import type { ReactNode } from 'react'
import { Abs, ImagePlaceholder, Slide } from '../../ui'
import { Box, Lines } from '../../ui'
import { answerLabel } from './data'
import { t } from './theme'

const NOTCHES = [[180, 76], [364, 88], [596, 92], [825, 87], [1023, 76]] as const

/** Hand-drawn notebook page: thick outline with binder notches along the top. */
export function NoteSlide({ children }: { children: ReactNode }) {
  return (
    <Slide background={t.outside} className={t.light} style={{ color: t.ink, ['--ly' as string]: '0.05em' }}>
      <Box x={40} y={20} w={1204} h={740} bg={t.page} className="rounded-md" style={{ border: `${t.border}px solid ${t.ink}` }} />
      {NOTCHES.map(([x, w]) => (
        <Box key={x} x={x} y={-6} w={w} h={88} bg={t.outside} style={{ border: `${t.border}px solid ${t.ink}`, borderTop: 0, borderRadius: '0 0 36px 36px' }} />
      ))}
      {children}
    </Slide>
  )
}

export const Art = ({ x, y, w, h, r = '16px', label = 'hand-drawn illustration', tone }: { x: number; y: number; w: number; h: number; r?: string; label?: string; tone?: string }) => (
  <Abs x={x} y={y} w={w} h={h}><ImagePlaceholder label={label} tone={tone} className="h-full w-full" style={{ borderRadius: r }} /></Abs>
)

/** Rounded beige pill with centred text. */
export function Pill({ x, y, w, h, children, size, className = t.bold }: { x: number; y: number; w: number; h: number; children: ReactNode; size: number; className?: string }) {
  return (
    <>
      <Box x={x} y={y} w={w} h={h} bg={t.beige} className="rounded-full" />
      <Lines x={x + w / 2} cy={y + h / 2} align="center" w={w} size={size} className={className} color={t.ink} lines={[children]} />
    </>
  )
}

/** Outlined speech bubble with a small tail at bottom-left. */
export function Bubble({ x, y, w, h, text, size, tailX }: { x: number; y: number; w: number; h: number; text: string; size: number; tailX: number }) {
  return (
    <>
      <Abs x={tailX - 2} y={y + h - 4} w={0} h={0} style={{ borderTop: `22px solid ${t.ink}`, borderLeft: '6px solid transparent', borderRight: '10px solid transparent' }} />
      <Box x={x} y={y} w={w} h={h} bg={t.page} className="rounded-[26px]" style={{ border: `${t.border}px solid ${t.ink}`, boxShadow: `4px 4px 0 ${t.ink}` }} />
      <Lines x={x + w / 2} cy={y + h / 2} align="center" w={w} size={size} className={t.bold} color={t.ink} lines={[text]} />
    </>
  )
}

/** Question bar + quiz-type bubble + reading bear (shared by all quiz slides). */
export function QuizFrame({ q, tag, bubbleX = 879, bubbleW = 305, bubbleY = 337, children }: { q: string; tag: string; bubbleX?: number; bubbleW?: number; bubbleY?: number; children?: ReactNode }) {
  return (
    <NoteSlide>
      <Pill x={120} y={161} w={1037} h={87} size={44}>{q}</Pill>
      <Bubble x={bubbleX} y={bubbleY} w={bubbleW} h={89} text={tag} size={34} tailX={bubbleX + 52} />
      <Art x={955} y={bubbleY + 133} w={185} h={174} label="reading bear doodle" />
      {children}
    </NoteSlide>
  )
}

/** "정답: ___" answer line with sparkle doodles. */
export function Answer({ text, x = 346 }: { text: string; x?: number }) {
  return (
    <>
      <Art x={296} y={349} w={74} h={74} r="50%" label="sparkle doodle" tone="#eeeae6" />
      <Art x={753} y={581} w={45} h={40} r="50%" label="sparkle doodle" />
      <Lines x={163} cy={483} size={44} color={t.ink} lines={[answerLabel]} />
      <Lines x={x} cy={482} size={96} className={t.bold} color={t.ink} lines={[text]} />
      <Box x={157} y={556} w={713} h={2} bg="#444" />
    </>
  )
}
