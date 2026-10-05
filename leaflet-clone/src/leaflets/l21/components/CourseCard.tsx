import { KeyValueList, cn } from '../../../ui'
import { HeadPill } from '../../shared-2021/components/HeadPill'
import type { CourseDetail } from '../data'

export interface CourseCardProps {
  course: CourseDetail
  className?: string
}

/** Pale box with a solid pill title overlapping its top edge and [label] value rows. */
export function CourseCard({ course, className }: CourseCardProps) {
  return (
    <div className={cn('relative h-[182px] w-[312px]', className)}>
      <div className="absolute inset-x-0 bottom-0 top-[19px] rounded-[14px] bg-[#e4ecf5]" />
      <div className="absolute left-0 top-0 flex w-[234px] justify-center pt-[1px]">
        <HeadPill className="h-[35px] px-[17px] text-[24px] tracking-[0.06em]">{course.title}</HeadPill>
      </div>
      <KeyValueList
        className="absolute left-[30px] top-[52px] gap-[18px]"
        labelWidth={60}
        labelClassName="text-[16px] font-bold leading-[23.5px] text-[#3b5c80]"
        valueClassName="whitespace-pre-line text-[16px] font-semibold leading-[23.5px] tracking-[-0.02em] text-[#3b5c80]"
        items={course.rows.map((r) => ({ key: r.label, label: r.label, value: r.value }))}
      />
    </div>
  )
}
