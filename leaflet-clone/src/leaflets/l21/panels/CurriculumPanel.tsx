import { Panel, Placed } from '../../../ui'
import { CardSheet } from '../../shared-2021/components/CardSheet'
import { CenteredRow } from '../../shared-2021/components/CenteredRow'
import { HeadPill } from '../../shared-2021/components/HeadPill'
import { ScheduleTable } from '../components/ScheduleTable'
import { cards, curriculumPanel as c } from '../data'

const INFO_TOP = 490
const INFO_STEP = 93

export function CurriculumPanel() {
  return (
    <Panel>
      <CardSheet insets={cards[0]} />
      <CenteredRow top={68} centerX={243}>
        <HeadPill variant="soft" className="h-[40px] w-[130px] text-[27px]">
          {c.heading}
        </HeadPill>
      </CenteredRow>
      <Placed x={70} y={142} width={343}>
        <ScheduleTable title={c.tableTitle} rows={c.rows} />
      </Placed>
      {c.info.map((item, i) => (
        <CenteredRow key={item.label} top={INFO_TOP + i * INFO_STEP} centerX={242}>
          <div className="flex flex-col items-center">
            <HeadPill className="h-[28px] px-[15px] text-[20px]">{item.label}</HeadPill>
            <span className="mt-[12px] text-[23px] font-bold leading-[30px] tracking-[-0.03em] text-[#3b5c80]">{item.value}</span>
          </div>
        </CenteredRow>
      ))}
      <Placed
        x={93}
        y={873}
        width={302}
        height={65}
        className="flex items-center justify-center rounded-[12px] bg-[#d5e3f1] text-[15.5px] font-semibold tracking-[-0.03em] text-[#3b5c80]"
      >
        {c.notice}
      </Placed>
    </Panel>
  )
}
