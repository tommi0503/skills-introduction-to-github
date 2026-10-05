import { cn } from '../../../ui'
import { Lines } from '../../shared-0812'

export interface SectionHeadingProps {
  title: string
  body: string[]
  className?: string
  titleClassName?: string
  bodyClassName?: string
}

/** Centered heavy title followed by grey copy. */
export function SectionHeading({ title, body, className, titleClassName, bodyClassName }: SectionHeadingProps) {
  return (
    <div className={cn('text-center', className)}>
      <h2 className={cn('m-0 font-black text-[#262626]', titleClassName)}>{title}</h2>
      <Lines lines={body} className={cn('font-medium text-[#727272]', bodyClassName)} />
    </div>
  )
}
