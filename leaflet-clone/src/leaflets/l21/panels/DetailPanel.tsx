import { Panel, Placed } from '../../../ui'
import { CardSheet } from '../../shared-2021/components/CardSheet'
import { CenteredRow } from '../../shared-2021/components/CenteredRow'
import { HeadPill } from '../../shared-2021/components/HeadPill'
import { CourseCard } from '../components/CourseCard'
import { cards, detailPanel as d } from '../data'

const COURSE_TOP = 138
const COURSE_STEP = 206

export function DetailPanel() {
  return (
    <Panel>
      <CardSheet insets={cards[2]} />
      <CenteredRow top={68} centerX={245}>
        <HeadPill variant="soft" className="h-[40px] w-[133px] text-[27px]">
          {d.heading}
        </HeadPill>
      </CenteredRow>
      {d.courses.map((course, i) => (
        <Placed key={course.id} x={88} y={COURSE_TOP + i * COURSE_STEP}>
          <CourseCard course={course} />
        </Placed>
      ))}
    </Panel>
  )
}
