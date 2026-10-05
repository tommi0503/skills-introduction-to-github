import { ArrowRight, Circle } from 'lucide-react'
import { CircleButton } from '../components/CircleButton'
import { GradientCard } from '../components/GradientCard'
import { Mascot } from '../components/Mascot'
import { PrimaryButton } from '../components/PrimaryButton'
import { SectionHeader } from '../components/SectionHeader'
import { SoftCard } from '../components/SoftCard'
import { TagPill } from '../components/TagPill'
import { TaskRow } from '../components/TaskRow'
import { WeekTracker } from '../components/WeekTracker'
import { mascots, morning, tasks, thisWeek } from '../data'
import { gradients } from '../theme'

/** Daily home: greeting, week tracker, active challenge and today's checklist. */
export function MorningScreen() {
  const c = morning.challenge
  return (
    <div className="relative h-full w-full">
      <div className="absolute left-[22.5px] top-[57px]">
        <div className="text-[12px] leading-[16px] font-medium text-[#8f8f94]">{morning.date}</div>
        <div className="mt-[3.5px] text-[24px] leading-[30px] font-semibold tracking-[-0.4px]">{morning.greeting}</div>
      </div>
      <div className="absolute left-[308px] top-[57px]">
        <CircleButton icon={Circle} size={44} iconSize={11} />
      </div>

      <div className="absolute left-[20px] top-[125px] w-[336px]">
        <WeekTracker title={morning.weekTitle} count={morning.weekCount} days={thisWeek} height={110} headerTop={14} labelsTop={43.5} />
      </div>

      <GradientCard gradient={gradients.mindful} className="absolute left-[20px] top-[251px] h-[184px] w-[336px]">
        <div className="absolute left-[20px] top-[21.5px]">
          <TagPill width={107.5}>{c.tag}</TagPill>
        </div>
        <div className="absolute left-[20px] top-[58.5px]">
          <div className="text-[22px] leading-[26px] font-semibold tracking-[-0.4px]">{c.title}</div>
          <div className="mt-[7.5px] text-[11.5px] font-medium text-[#55555b]">{c.meta}</div>
        </div>
        <Mascot spec={{ ...mascots.flower, w: 69, h: 58.5 }} style={{ position: 'absolute', left: 243.5, top: 58 }} />
        <div className="absolute left-[20px] right-[22px] top-[133px]">
          <SectionHeader title={c.progressLabel} titleClassName="text-[11.5px] font-medium text-[#55555b]" />
          <span className="absolute right-0 top-0 text-[11.5px] font-medium text-[#55555b]">{Math.round(c.progress * 100)}%</span>
          <div className="mt-[8px] h-[6px] rounded-full bg-white/80">
            <div className="h-full rounded-full bg-[#18171c]" style={{ width: `${c.progress * 100}%` }} />
          </div>
        </div>
      </GradientCard>

      <SectionHeader
        title={morning.todayTitle}
        aside={morning.todayCount}
        className="absolute left-[22.5px] right-[24px] top-[454px]"
        titleClassName="text-[14px]"
      />
      <SoftCard className="absolute left-[20px] top-[482.5px] w-[336px]">
        {tasks.map((t, i) => (
          <TaskRow key={t.id} task={t} divider={i < tasks.length - 1} />
        ))}
      </SoftCard>

      <div className="absolute inset-x-[20px] top-[725px]">
        <PrimaryButton label={morning.cta} icon={ArrowRight} />
      </div>
    </div>
  )
}
