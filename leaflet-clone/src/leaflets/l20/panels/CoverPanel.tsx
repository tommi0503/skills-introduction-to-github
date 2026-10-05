import { Phone } from 'lucide-react'
import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { CardSheet } from '../../shared-2021/components/CardSheet'
import { CenteredRow } from '../../shared-2021/components/CenteredRow'
import { IconDisc } from '../../shared-2021/components/IconDisc'
import { DISPLAY } from '../../shared-2021/theme'
import { cn } from '../../../ui'
import { cards, coverPanel as c } from '../data'

const BUTTON_TOP = 586
const BUTTON_STEP = 82

export function CoverPanel() {
  return (
    <Panel>
      <CardSheet insets={cards[2]} />
      <CenteredRow top={78}>
        <span className="flex h-[46px] w-[182px] items-center justify-center rounded-full bg-[#d2e2f1] font-jua text-[25px] leading-none text-[#2f5378]">
          {c.kicker}
        </span>
      </CenteredRow>
      <CenteredRow top={142}>
        <span className={cn(DISPLAY, 'text-[64px] leading-none tracking-[-0.01em] text-[#3a6ea8]')}>{c.title}</span>
      </CenteredRow>
      <CenteredRow top={216}>
        <span className={cn(DISPLAY, 'text-[64px] leading-none tracking-[-0.01em] text-[#d0647a]')}>{c.subtitle}</span>
      </CenteredRow>
      <CenteredRow top={296}>
        <span className="text-[21px] font-bold tracking-[-0.03em] text-[#4a79a6]">{c.tagline}</span>
      </CenteredRow>
      <Placed x={80} y={360} width={320} height={226}>
        <ImagePlaceholder label="seniors with smartphones illustration" className="h-full w-full" />
      </Placed>
      {c.courses.map((course, i) => (
        <Placed
          key={course}
          x={86}
          y={BUTTON_TOP + i * BUTTON_STEP}
          width={308}
          height={64}
          className="flex items-center justify-center rounded-[12px] bg-[#d2e2f1] text-[27px] font-bold tracking-[-0.03em] text-[#3b5a7c]"
        >
          {course}
        </Placed>
      ))}
      <CenteredRow top={876} centerX={241}>
        <span className="text-[20px] font-medium tracking-[-0.03em] text-[#50545a]">
          <b className="mr-[10px] font-bold text-[#3f4348]">{c.inquiryLabel}</b>
          {c.inquiryPlace}
        </span>
      </CenteredRow>
      <CenteredRow top={912} centerX={242}>
        <span className="flex items-center gap-[8px] text-[22px] font-bold text-[#45484e]">
          <IconDisc icon={Phone} size={22} iconSize={12} filled />
          {c.inquiryPhone}
        </span>
      </CenteredRow>
    </Panel>
  )
}
