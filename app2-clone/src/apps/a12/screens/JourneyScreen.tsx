import { Gift, ImageIcon, Play, Video } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { BottomNav } from '../components/BottomNav'
import { DayHeader, EmojiFace, JourneyPanel, TaskTile } from '../components/JourneyParts'
import { StatusOverlay } from '../components/StatusOverlay'
import { journeyDays } from '../data'

const L = 69
const R = 221

export function JourneyScreen() {
  const [d1, d2] = journeyDays
  return (
    <AppScreen background="#fff" className="font-sora text-[#111]">
      <div className="absolute inset-x-0 top-0 h-[127px] bg-[#f2f2f2]" />
      <StatusOverlay />
      <div className="absolute top-[74px] left-[19px] flex items-start">
        <span className="text-[30px] leading-[40px] font-bold tracking-[-0.8px]">Journey</span>
        <ImagePlaceholder tone="#151515" label="app badge" className="mt-[7px] ml-[1px] h-[19px] w-[26px] rounded-[3px]" />
      </div>

      {/* Day 1 */}
      <DayHeader date={d1.date} title={d1.title} current top={145} />
      <div className="absolute top-[208px] left-[39.5px] h-[336px] w-[2px] bg-[#e8792f]" />
      <div className="absolute top-[358px] left-[22px] flex h-[36px] w-[36px] items-center justify-center rounded-full border-[1.5px] border-[#e8792f] bg-white text-[#e8792f]">
        <Gift size={16} strokeWidth={2} />
      </div>
      <JourneyPanel dashed className="h-[139px]" style={{ left: L, top: 222 }}>
        <div className="mt-[17px] text-center text-[9.5px] font-medium">{d1.mood!.title}</div>
        <div className="mt-[13.5px] flex items-center justify-center gap-[6px]">
          <EmojiFace size={32} className="-ml-[14px]" />
          <EmojiFace size={32} />
          <EmojiFace size={46} ring="#f6e98d" border />
          <EmojiFace size={32} />
          <EmojiFace size={32} className="-mr-[14px]" />
        </div>
        <div className="mt-[12px] text-center text-[11.5px] font-semibold">{d1.mood!.label}</div>
      </JourneyPanel>
      <JourneyPanel dashed className="h-[139px]" style={{ left: R, top: 222 }}>
        <div className="mt-[13px] text-center text-[8.5px] font-medium">Tasks</div>
        <div className="mt-[9px] grid grid-cols-3 justify-items-center gap-y-[8px] px-[8px]">
          {d1.tasks.map((t, i) => (
            <TaskTile key={i} tile={t} />
          ))}
        </div>
      </JourneyPanel>
      <JourneyPanel dashed className="h-[139px]" style={{ left: L, top: 373 }}>
        <div className="mt-[22px] text-center text-[10px] font-medium">Your media</div>
        <div className="mt-[7px] flex gap-[9px] px-[7px]">
          <ImagePlaceholder label="photo" className="h-[58px] w-[57px] rounded-[8px] border-[1.5px] border-[#151515]" />
          <div className="relative">
            <ImagePlaceholder tone="#5a5a5a" label="video" className="h-[58px] w-[57px] rounded-[8px] border-[1.5px] border-[#151515]" />
            <div className="absolute inset-0 flex items-center justify-center">
              <span className="flex h-[36px] w-[36px] items-center justify-center rounded-full border-2 border-white">
                <Play size={16} fill="#fff" stroke="none" className="ml-[2px]" />
              </span>
            </div>
          </div>
        </div>
        <div className="mt-[5px] flex gap-[25px] pl-[17px] text-[8.5px] text-[#aaa]">
          <span className="flex items-center gap-[3px]">
            <ImageIcon size={10} /> Photo
          </span>
          <span className="flex items-center gap-[3px]">
            <Video size={10} /> Vlog
          </span>
        </div>
      </JourneyPanel>
      <JourneyPanel dashed className="h-[139px]" style={{ left: R, top: 373 }}>
        <div className="mt-[21px] text-center text-[8.5px] font-medium">Your text journey</div>
        <div className="mx-[7px] mt-[6px] h-[78px] rounded-[8px] border-[1.5px] border-[#151515] bg-white px-[8px] pt-[7px] text-[7.5px] leading-[11px]">
          {d1.journal!.map((l, i) => (
            <div key={i} className={i === d1.journal!.length - 1 ? 'text-[#aaa]' : ''}>
              {l}
            </div>
          ))}
        </div>
      </JourneyPanel>

      {/* Day 2 */}
      <DayHeader date={d2.date} title={d2.title} current={false} top={562} />
      <div className="absolute top-[625px] left-[40px] h-[150px] border-l-[1.5px] border-dashed border-[#777]" />
      <JourneyPanel className="h-[140px]" style={{ left: L, top: 638 }}>
        <div className="mt-[20px] text-center text-[9.5px] leading-[12px] font-medium">
          {d2.question!.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
        <div className="mt-[6px] grid grid-cols-3 justify-items-center gap-y-[5px] px-[15px]">
          {Array.from({ length: 6 }, (_, i) => (
            <EmojiFace key={i} size={31} border />
          ))}
        </div>
      </JourneyPanel>
      <JourneyPanel className="h-[140px]" style={{ left: R, top: 638 }}>
        <div className="mt-[13px] text-center text-[8.5px] font-medium">Tasks</div>
        <div className="mt-[39px] flex justify-center gap-[6px]">
          {d2.tasks.map((t, i) => (
            <TaskTile key={i} tile={t} />
          ))}
        </div>
      </JourneyPanel>
      <BottomNav active="journal" />
    </AppScreen>
  )
}
