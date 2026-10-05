import { ImagePlaceholder } from '../../../ui'
import { Box } from '../components/Box'
import { SectionTitle } from '../components/SectionTitle'
import { thinkSection as s, type ToolCard } from '../data'
import { theme } from '../theme'

const CARD = { top: 2020, w: 400, h: 450, xs: [85, 515, 945], captionTop: 2500 }

function ColorChip() {
  return (
    <div
      className="absolute left-[97px] top-[195px] flex h-[60px] items-center rounded-[14px] pl-[10px] pr-[12px] text-white"
      style={{ background: theme.color.chip }}
    >
      <span className="h-[38px] w-[38px] rounded-full" style={{ background: theme.color.chipDot }} />
      <span className="ml-[8px] text-[33px] leading-[35px]">{s.colorChip}</span>
    </div>
  )
}

function AiDialog() {
  return (
    <div className="absolute left-[20px] top-[155px] h-[140px] w-[361px] rounded-[16px] bg-white px-[20px] pt-[16px] text-center">
      <p className="text-[14px] font-medium leading-[20px]" style={{ color: theme.color.ink, letterSpacing: '-0.28px' }}>
        {s.ai.title}
      </p>
      <p className="mt-[2px] text-[14px] leading-[20px]" style={{ color: theme.color.hint, letterSpacing: '-0.28px' }}>
        {s.ai.body}
      </p>
      <div className="mt-[18px] flex h-[50px] items-center rounded-full border border-[#ececec] px-[1px]">
        {s.ai.options.map((o, i) => (
          <span
            key={o}
            className="flex h-[40px] w-[106px] items-center justify-center rounded-full text-[14px] font-medium"
            style={i === 0 ? { background: theme.color.ink, color: '#fff' } : { color: theme.color.ink }}
          >
            {o}
          </span>
        ))}
      </div>
    </div>
  )
}

function Card({ card, x }: { card: ToolCard; x: number }) {
  const bg = card.kind === 'color' ? theme.color.redCard : card.kind === 'similar' ? theme.color.tanCard : undefined
  return (
    <div
      className="absolute overflow-hidden"
      style={{ left: x, top: CARD.top, width: CARD.w, height: CARD.h, borderRadius: theme.cardRadius, background: bg }}
    >
      {card.images.map((r, i) => (
        <Box key={i} rect={r}>
          <ImagePlaceholder className="h-full w-full" />
        </Box>
      ))}
      {card.kind === 'color' && <ColorChip />}
      {card.kind === 'ai' && <AiDialog />}
    </div>
  )
}

/** "Search the way you think." — three feature cards with captions. */
export function Think() {
  return (
    <>
      <div className="absolute left-0 top-[1888px] flex justify-center" style={{ width: theme.contentWidth }}>
        <SectionTitle text={s.title} lineHeight={72.6} />
      </div>
      {s.cards.map((c, i) => (
        <div key={c.caption}>
          <Card card={c} x={CARD.xs[i]} />
          <p
            className="absolute text-center text-[24px] leading-[19.2px]"
            style={{ left: CARD.xs[i], top: CARD.captionTop, width: CARD.w, letterSpacing: '-0.96px', color: theme.color.ink }}
          >
            {c.caption}
          </p>
        </div>
      ))}
    </>
  )
}
