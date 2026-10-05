import { CircleCheck } from 'lucide-react'
import { BulletList, Divider, Panel, Placed } from '../../../ui'
import { BlobCard } from '../../shared-2223/components/BlobCard'
import { SectionTitle } from '../../shared-2223/components/SectionTitle'
import { ProgramItem } from '../components/ProgramItem'
import { programPanel as d } from '../data'

const PROGRAM_TOP = 153
const PROGRAM_STEP = 192.5

export function ProgramPanel() {
  return (
    <Panel>
      <BlobCard x={26} y={40} width={414} height={936} radius="62px 66px 56px 48px / 56px 86px 44px 44px" />
      <SectionTitle top={80} centerX={236} className="text-[35px] text-[#62a871]">
        {d.heading}
      </SectionTitle>
      {d.programs.map((p, i) => (
        <Placed key={p.id} x={70} y={PROGRAM_TOP + i * PROGRAM_STEP}>
          <ProgramItem program={p} />
        </Placed>
      ))}
      <Placed x={70} y={727} width={335}>
        <Divider color="#d6dbd6" thickness={2} />
      </Placed>
      <Placed x={70} y={760} className="font-jua text-[22.5px] leading-none text-[#76b282]">
        {d.checklistHeading}
      </Placed>
      <Placed x={70} y={812}>
        <BulletList
          className="gap-[11px]"
          itemClassName="items-center text-[18.5px] font-semibold leading-[28px] tracking-[-0.03em] text-[#46484b]"
          markerClassName="mr-[8px] flex self-center text-[#76b282]"
          marker={<CircleCheck size={17} strokeWidth={2.4} fill="#76b282" color="#fff" />}
          items={d.checklist}
        />
      </Placed>
    </Panel>
  )
}
