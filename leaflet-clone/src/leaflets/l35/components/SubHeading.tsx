import { cn } from '../../../ui'
import { larana } from '../../shared-3435/theme'

/** Left-aligned navy sub-heading (검진 절차 / 진료 예약 방법 / 자주 묻는 질문 …). */
export function SubHeading({ children, className }: { children: string; className?: string }) {
  return (
    <h3 className={cn('m-0 text-[23.5px] font-bold leading-[30px]', className)} style={{ color: larana.navy }}>
      {children}
    </h3>
  )
}
