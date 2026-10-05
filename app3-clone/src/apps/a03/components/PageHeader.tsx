import { ArrowLeft, Plus } from 'lucide-react'
import { nd } from '../theme'
import { CircleButton } from './CircleButton'

export interface PageHeaderProps {
  title: string
  subtitle: string
}

/** Back · centred title/subtitle · add. */
export function PageHeader({ title, subtitle }: PageHeaderProps) {
  return (
    <div className="absolute inset-x-[18px] top-[57px] flex items-center justify-between">
      <CircleButton icon={ArrowLeft} />
      <div className="text-center">
        <p className="text-[14px] font-medium">{title}</p>
        <p className="mt-[3px] text-[10px]" style={{ color: nd.muted }}>
          {subtitle}
        </p>
      </div>
      <CircleButton icon={Plus} />
    </div>
  )
}
