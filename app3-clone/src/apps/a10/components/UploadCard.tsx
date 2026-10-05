import { ArrowUpToLine } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

export function UploadCard({ label, className }: { label: string; className?: string }) {
  return (
    <div
      className={cn('flex h-[251px] w-[322px] shrink-0 flex-col items-center justify-center rounded-[3px] border-[1.5px]', className)}
      style={{ borderColor: theme.greenSoft }}
    >
      <ArrowUpToLine size={22} strokeWidth={1.6} style={{ color: theme.greenIcon }} />
      <p className="mt-[11px] w-[240px] text-center text-[15.5px] leading-[25px] font-semibold tracking-[-0.2px] text-[#161616]">{label}</p>
    </div>
  )
}
