import { ChevronLeft, Share } from 'lucide-react'
import { CircleButton } from '../components/CircleButton'
import { GradientCard } from '../components/GradientCard'
import { Mascot } from '../components/Mascot'
import { PrimaryButton } from '../components/PrimaryButton'
import { StatCard } from '../components/StatCard'
import { WeekTracker } from '../components/WeekTracker'
import { last7, mascots, progress, stats } from '../data'
import { gradients } from '../theme'

/** Mascot trio inside the streak card (card-relative positions). */
const trio = [
  { spec: mascots.cloud, x: 94, y: 43 },
  { spec: mascots.flower, x: 139, y: 24 },
  { spec: mascots.pebble, x: 211.5, y: 44 },
]

/** Streak overview: hero streak card, last-7-days tracker, stats and share CTA. */
export function ProgressScreen() {
  return (
    <div className="relative h-full w-full">
      <div className="absolute left-[19px] top-[57.5px]">
        <CircleButton icon={ChevronLeft} size={42} iconSize={16} />
      </div>
      <div className="absolute inset-x-0 top-[69px] text-center text-[14.5px] leading-[19px] font-semibold">{progress.title}</div>

      <GradientCard gradient={gradients.streak} className="absolute left-[20px] top-[116px] h-[240px] w-[336px]">
        {trio.map(({ spec, x, y }, i) => (
          <Mascot key={i} spec={spec} style={{ position: 'absolute', left: x, top: y }} />
        ))}
        <div className="absolute inset-x-0 top-[95.5px] text-center">
          <div className="text-[62px] leading-[62px] font-bold tracking-[-1px]">{progress.streak}</div>
          <div className="mt-[8px] text-[15px] leading-[18px] font-bold tracking-[-0.2px]">{progress.streakLabel}</div>
          <div className="mt-[8px] text-[11.5px] leading-[17px] font-medium text-[#55555b]">
            {progress.streakNote.map((l) => (
              <div key={l}>{l}</div>
            ))}
          </div>
        </div>
      </GradientCard>

      <div className="absolute left-[20px] top-[371px] w-[336px]">
        <WeekTracker title={progress.weekTitle} count={progress.weekCount} days={last7} height={108} headerTop={13.5} labelsTop={42.5} />
      </div>

      <div className="absolute left-[20px] top-[495px] grid w-[336px] grid-cols-2 gap-x-[15px] gap-y-[16.5px]">
        {stats.map((s) => (
          <StatCard key={s.label} stat={s} />
        ))}
      </div>

      <div className="absolute inset-x-[20px] top-[725px]">
        <PrimaryButton label={progress.cta} icon={Share} />
      </div>
    </div>
  )
}
