import { cn } from '../../../ui'

export function SheetGrabber({ className }: { className?: string }) {
  return <div className={cn('mx-auto h-[4px] w-[57px] rounded-full bg-[#e6e8ef]', className)} />
}
