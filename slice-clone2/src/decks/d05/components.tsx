import type { ReactNode } from 'react'
import { BookMarked, BookOpen, Contact, FilePenLine, FileSearch, Inbox, Landmark, Laptop, Library, Music, TabletSmartphone } from 'lucide-react'
import { Abs, Slide } from '../../ui'
import { Box, Lines } from '../../ui'
import { frame } from './data'
import { t } from './theme'

export const ICONS = { landmark: Landmark, library: Library, bookmark: BookMarked, inbox: Inbox, search: FileSearch, edit: FilePenLine, tablet: TabletSmartphone, contact: Contact, music: Music, laptop: Laptop, book: BookOpen }
export type IconKey = keyof typeof ICONS

export function Icon({ k, cx, cy, size, color = t.icon, stroke = 1.4 }: { k: IconKey; cx: number; cy: number; size: number; color?: string; stroke?: number }) {
  const I = ICONS[k]
  return <Abs x={cx - size / 2} y={cy - size / 2}><I size={size} color={color} strokeWidth={stroke} /></Abs>
}

/** Binder folder: teal cover, side tab with vertical label, white page with grey header strip and page-stack edge. */
export function FolderSlide({ headerH = 105, page, children, overlay }: { headerH?: number; page?: string; children?: ReactNode; overlay?: ReactNode }) {
  return (
    <Slide background={t.bg} className={t.sans} style={{ color: t.ink, ['--ly' as string]: '0.07em' }}>
      <Box x={28} y={33} w={1195} h={667} bg={t.folder} className="rounded-tr-xl rounded-br-md" />
      <Box x={1205} y={470} w={46} h={230} bg={t.folder} className="rounded-tr-[22px] rounded-br-xl" />
      <Abs x={1222} y={520} w={28} h={150} className="flex items-center justify-center text-white" style={{ writingMode: 'vertical-rl', fontSize: 13.5, letterSpacing: '0.1em' }}>{frame.tab}</Abs>
      <Box x={40} y={42} w={1160} h={649} bg={t.edge} />
      <Box x={43} y={42} w={1155} h={649} bg="#fff" />
      {[1183, 1188, 1193].map((x) => <Box key={x} x={x} y={42} w={1.5} h={649} bg="#c8c8ca" />)}
      <Box x={45} y={42} w={1137} h={headerH} bg={t.head} />
      <Lines x={85} cy={73} size={12.5} className="font-bold tracking-[0.04em]" color={t.muted} lines={[frame.left]} />
      <Lines x={1139} cy={73} align="right" size={12.5} className="font-bold tracking-[0.04em]" color={t.muted} lines={[frame.right]} />
      {page !== undefined && (
        <>
          <Abs x={611 - 40} y={147 - 40} w={80} h={80} className="rounded-full bg-white" />
          <Box x={545} y={147} w={130} h={44} bg="#fff" />
          <Lines x={611} cy={133} align="center" w={60} size={17} color={t.muted} lines={[page]} />
        </>
      )}
      {overlay}
      {children}
    </Slide>
  )
}

export const Title = ({ text, cy, x = 640, size = 56, align = 'center' as const }: { text: string | readonly string[]; cy: number; x?: number; size?: number; align?: 'left' | 'center' }) => (
  <Lines x={x} cy={cy} lh={Math.round(size * 1.12)} align={align} size={size} className={t.display} color={t.deep} lines={typeof text === 'string' ? [text] : text} />
)

/** Small white circle with a grey letter. */
export const LetterDot = ({ cx, cy, letter, r = 18, bg = '#fff', color = t.muted }: { cx: number; cy: number; letter: string; r?: number; bg?: string; color?: string }) => (
  <>
    <Abs x={cx - r} y={cy - r} w={r * 2} h={r * 2} className="rounded-full" style={{ background: bg }} />
    <Lines x={cx} cy={cy} align="center" w={r * 2} size={15} className="font-medium" color={color} lines={[letter]} />
  </>
)
