import type { ReactNode } from 'react'
import { MailCheck } from 'lucide-react'
import { softShadow, theme } from '../theme'

export interface MailCardProps {
  subject: string
  from: string
  time: string
  preview: string
  footer?: ReactNode
}

export function MailCard({ subject, from, time, preview, footer }: MailCardProps) {
  return (
    <div className="rounded-[18px] px-[16px] pt-[14px] pb-[16px]" style={{ background: theme.card, boxShadow: softShadow }}>
      <div className="flex items-start">
        <span className="flex h-[44px] w-[44px] items-center justify-center rounded-[11px] text-white" style={{ background: theme.blue }}>
          <MailCheck size={20} strokeWidth={1.8} />
        </span>
        <div className="ml-[9px] flex-1">
          <p className="text-[15.5px] font-medium tracking-[-0.2px] text-[#111]">{subject}</p>
          <p className="mt-[2px] text-[12px] text-[#b0b0b0]">{from}</p>
        </div>
        <span className="-mt-[1px] text-[15.5px] tracking-[-0.2px] text-[#111]">{time}</span>
      </div>
      <p className="mt-[25px] mb-[20px] text-center text-[14px] text-[#9a9a9a]">{preview}</p>
      {footer}
    </div>
  )
}
