import { CircleAlert } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'

export interface ImprovementCardProps {
  title: string
  text: string
  tone: string
  procrastinating?: boolean
}

/** Habit banner on the progress screen (illustration + text), optional procrastination flag. */
export function ImprovementCard({ title, text, tone, procrastinating }: ImprovementCardProps) {
  return (
    <div className="relative h-[97px]">
      <div
        className="relative h-full overflow-hidden rounded-[10px] border-2 border-[#cfcfcf]"
        style={{ boxShadow: '3px 3px 0 #d6d6d6' }}
      >
        <ImagePlaceholder tone={tone} label="habit illustration" className="absolute inset-0" />
        <div className="absolute top-[27px] left-[15px] text-[15.5px] font-bold tracking-[-0.3px] text-white">{title}</div>
        <div className="absolute top-[55px] left-[15px] text-[9.5px] font-medium tracking-[-0.2px] text-white/90">{text}</div>
      </div>
      {procrastinating && (
        <div className="absolute top-[67px] left-[189px] flex h-[32px] w-[159px] items-center gap-[7px] rounded-full border-2 border-[#151515] bg-[#e1322a] pl-[8px] text-[12.5px] font-semibold tracking-[-0.2px] text-white">
          <CircleAlert size={18} fill="#fff" stroke="#e1322a" strokeWidth={2.4} />
          I’m procrastinating
        </div>
      )}
    </div>
  )
}
