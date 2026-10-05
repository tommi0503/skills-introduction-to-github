import type { StatCardData } from '../data'
import { cardShadow, theme } from '../theme'
import { MiniBars } from './MiniBars'

const tones = {
  green: { bar: `linear-gradient(180deg, #6ade97, ${theme.green})`, badge: theme.greenSoft, text: '#3d9b5e' },
  purple: { bar: `linear-gradient(180deg, #b39af3, ${theme.purple})`, badge: theme.purpleSoft, text: theme.purpleText },
}

export function StatCard({ data }: { data: StatCardData }) {
  const tone = tones[data.tone]
  return (
    <div className="h-[160px] w-[174px] shrink-0 rounded-[22px] px-[17px] pt-[15px]" style={{ background: theme.card, boxShadow: cardShadow }}>
      <p className="text-[14px] tracking-[-0.4px]" style={{ color: '#3a3a3a' }}>
        {data.title}
      </p>
      <div className="mt-[11px] flex items-center gap-[9px]">
        <span className="text-[31px] leading-[34px] font-light tracking-[-1px]" style={{ color: theme.ink }}>
          {data.value}
        </span>
        <span className="rounded-full px-[8px] py-[5px] text-[11px] tracking-[-0.2px]" style={{ background: tone.badge, color: tone.text }}>
          {data.delta}
        </span>
      </div>
      <div className="mt-[10px]">
        <MiniBars barWidth={19} gap={3.5} heights={data.bars} highlight={data.highlight} color={tone.bar} base={theme.bar} />
      </div>
    </div>
  )
}
