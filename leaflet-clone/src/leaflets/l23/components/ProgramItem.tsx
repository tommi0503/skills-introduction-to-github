import { ImagePlaceholder } from '../../../ui'
import { OutlineBar } from '../../shared-2223/components/OutlineBar'
import type { Program } from '../data'
import { JustifiedLines } from './JustifiedLines'

export interface ProgramItemProps {
  program: Program
}

/** Tag bar, photo and four justified lines of copy. */
export function ProgramItem({ program }: ProgramItemProps) {
  return (
    <div className="w-[335px]">
      <OutlineBar tag={program.tag} className="text-[19px]">
        <span className="ml-[14px] font-dohyeon text-[20px] text-[#7dbb89]">{program.title}</span>
      </OutlineBar>
      <div className="mt-[24px] flex">
        <ImagePlaceholder label={program.photo} className="h-[95px] w-[155px] rounded-[7px]" />
        <JustifiedLines
          lines={program.lines}
          className="ml-[15px] w-[165px] -translate-y-[6px] text-[17.5px] font-semibold leading-[25.5px] tracking-[-0.04em] text-[#46484b]"
        />
      </div>
    </div>
  )
}
