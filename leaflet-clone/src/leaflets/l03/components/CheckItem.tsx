import { SquareCheckBig } from 'lucide-react'
import { cn } from '../../../ui'
import { LineBlock } from './LineBlock'

interface CheckItemProps {
  lines: string[]
  /** When set, text is top-aligned and dropped by this many px instead of centred on the box. */
  textOffset?: number
  className?: string
}

/** Hand-ticked checkbox followed by one or more lines of text. */
export function CheckItem({ lines, textOffset, className }: CheckItemProps) {
  return (
    <div className={cn('flex', textOffset === undefined ? 'items-center' : 'items-start', className)}>
      <SquareCheckBig size={70} strokeWidth={2.8} className="shrink-0 text-[#1b1b1b]" />
      <LineBlock lines={lines} style={textOffset === undefined ? undefined : { marginTop: textOffset }} className="ml-[10px] text-[25px] font-medium leading-[35px] tracking-[0.01em] text-[#1b1b1b]" />
    </div>
  )
}
