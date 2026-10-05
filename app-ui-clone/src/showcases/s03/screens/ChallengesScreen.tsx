import { ChipGroup } from '../../../ui'
import { ChallengeTile } from '../components/ChallengeTile'
import { GradientCard } from '../components/GradientCard'
import { Mascot } from '../components/Mascot'
import { TagPill } from '../components/TagPill'
import { challenges, challengesPage, filters, mascots } from '../data'
import { gradients } from '../theme'

/** Challenge browser: filters, featured challenge and a 2×2 catalogue. */
export function ChallengesScreen() {
  const f = challengesPage.featured
  return (
    <div className="relative h-full w-full">
      <div className="absolute left-[22.5px] top-[60.5px]">
        <div className="text-[26px] leading-[32px] font-semibold tracking-[-0.5px]">{challengesPage.title}</div>
        <div className="mt-[6px] text-[12.5px] leading-[16px] font-medium text-[#9c9ca1]">{challengesPage.subtitle}</div>
      </div>

      <ChipGroup
        items={filters}
        activeKey="all"
        gap={9}
        className="absolute left-[18.5px] top-[135px]"
        chipClassName="h-[41px] min-w-[55px] rounded-full px-[17px] text-[12px] font-semibold"
        activeClassName="bg-[#18171c] text-white"
        inactiveClassName="bg-[#f4f4f4] text-[#4a4a50]"
      />

      <GradientCard gradient={gradients.deepWork} className="absolute left-[18.5px] top-[196.5px] h-[126px] w-[337.5px]">
        <div className="absolute left-[20.5px] top-[24.5px]">
          <TagPill width={92.5}>{f.tag}</TagPill>
        </div>
        <div className="absolute left-[20.5px] top-[55px]">
          <div className="text-[20px] leading-[24px] font-semibold tracking-[-0.4px]">{f.title}</div>
          <div className="mt-[6px] text-[11px] font-medium text-[#55555b]">{f.meta}</div>
        </div>
        <Mascot spec={mascots.bear} style={{ position: 'absolute', left: 257.5, top: 52.5 }} />
      </GradientCard>

      <div className="absolute left-[22.5px] top-[347px] text-[13.5px] leading-[18px] font-semibold">{challengesPage.listTitle}</div>

      <div className="absolute left-[18.5px] top-[377.5px] grid w-[337.5px] grid-cols-2 gap-x-[14.5px] gap-y-[15px]">
        {challenges.map((c) => (
          <ChallengeTile key={c.id} challenge={c} />
        ))}
      </div>
    </div>
  )
}
