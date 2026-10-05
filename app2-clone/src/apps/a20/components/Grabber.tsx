import { cn } from '../../../ui'

/** Sheet drag handle. */
export function Grabber({ className }: { className?: string }) {
  return <span className={cn('h-[4px] w-[32px] rounded-full bg-[#cfcfcf]', className)} />
}
