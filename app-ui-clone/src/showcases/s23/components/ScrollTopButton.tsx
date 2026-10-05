import { ArrowUp } from 'lucide-react'
import { cn } from '../../../ui'

export function ScrollTopButton({ className, style }: { className?: string; style?: React.CSSProperties }) {
  return (
    <div
      className={cn('absolute z-20 flex h-[53px] w-[53px] items-center justify-center rounded-full bg-white', className)}
      style={{ boxShadow: '0 2px 10px rgba(0,0,0,0.12)', ...style }}
    >
      <ArrowUp size={22} strokeWidth={1.6} color="#222" />
    </div>
  )
}
