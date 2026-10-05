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
    <div className="h-[162px] w-[182px] shrink-0 rounded-[22px] px-[19px] pt-[18px]" style={{ background: theme.card, boxShadow: cardShadow }}>
      <p className="text-[13px] tracking-[-0.2px]" style={{ color: '#555' }}>
        {data.title}
      </p>
      <div className="mt-[14px] flex items-center gap-[11px]">
        <span className="text-[31px] leading-[34px] font-light tracking-[-1px]" style={{ color: theme.ink }}>
          {data.value}
        </span>
        <span className="rounded-full px-[7px] py-[3px] text-[10px] tracking-[-0.2px]" style={{ background: tone.badge, color: tone.text }}>
          {data.delta}
        </span>
      </div>
      <div className="mt-[13px]">
        <MiniBars heights={data.bars} highlight={data.highlight} color={tone.bar} base={theme.bar} />
      </div>
    </div>
  )
}
