import { SquareCheckBig } from 'lucide-react'
import { cn } from '../../../ui'
import { LineBlock } from './LineBlock'

interface CheckItemProps {
  lines: string[]
  className?: string
}

/** Hand-ticked checkbox followed by one or more lines of text. */
export function CheckItem({ lines, className }: CheckItemProps) {
  return (
    <div className={cn('flex items-center', className)}>
      <SquareCheckBig size={74} strokeWidth={2.6} className="shrink-0 text-[#1b1b1b]" />
      <LineBlock lines={lines} className="ml-[10px] text-[25.5px] leading-[35px] tracking-[0.01em] text-[#1b1b1b]" />
    </div>
  )
}
