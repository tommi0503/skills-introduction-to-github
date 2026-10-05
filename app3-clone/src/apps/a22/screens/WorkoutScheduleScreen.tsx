import { Bookmark, ChevronLeft, MoreHorizontal } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { DateCard } from '../components/DateCard'
import { PillButton } from '../components/PillButton'
import { Shell } from '../components/Shell'
import { WheelPicker } from '../components/WheelPicker'
import { workout } from '../data'
import { theme } from '../theme'

export function WorkoutScheduleScreen() {
  return (
    <Shell background="#fff" statusColor="#fff">
      <ImagePlaceholder label="Workout class photo" tone={theme.photo} className="absolute inset-x-0 top-0 h-[340px]" />
      <ChevronLeft className="absolute left-[22px] top-[67px]" size={24} strokeWidth={1.6} color="#cfcfcf" />
      <MoreHorizontal className="absolute left-[289px] top-[68px]" size={22} strokeWidth={2.4} color="#fff" />
      <Bookmark className="absolute left-[334px] top-[67px]" size={24} fill="#fff" color="#fff" />
      <h1 className="absolute left-[25px] top-[138px] text-[26px] font-medium leading-[32px] text-[#eeeeee]">
        {workout.title.map((l) => (
          <span key={l} className="block">{l}</span>
        ))}
      </h1>
      <p className="absolute left-[25px] top-[242px] text-[15px] text-[#9a9a9a]">{workout.coach}</p>

      <div className="absolute inset-x-0 bottom-0 top-[321px] rounded-t-[12px] bg-white">
        <h2 className="absolute left-[21px] top-[42px] text-[21.5px] font-medium">{workout.sheetTitle}</h2>
        <p className="absolute left-[21px] right-[28px] top-[79px] text-[15px] leading-[25px]">{workout.sheetBody}</p>
        <div className="absolute left-[21px] top-[149px] flex gap-[11px]">
          {workout.days.map((d, i) => (
            <DateCard key={d.day} day={d} active={i === workout.selectedDay} />
          ))}
        </div>
        <WheelPicker
          className="absolute inset-x-0 top-[259px]"
          height={118}
          columns={workout.picker}
          step={25}
          radius={75.7}
          fontSize={19}
          selectedFontSize={22}
          color="#222"
          dimColor="#9a9a9a"
          band={{ left: 31, right: 31, height: 34, color: theme.band, radius: 4 }}
        />
        <div className="absolute inset-x-[21px] top-[420px] flex gap-[18px]">
          <PillButton variant="outline">{workout.cancel}</PillButton>
          <PillButton variant="solid">{workout.confirm}</PillButton>
        </div>
      </div>
    </Shell>
  )
}
