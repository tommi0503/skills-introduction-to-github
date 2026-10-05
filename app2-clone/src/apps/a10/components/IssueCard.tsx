import { ChevronRight, CloudSun, PlaneLanding, PlaneTakeoff, Sparkles, type LucideIcon } from 'lucide-react'
import { cn } from '../../../ui'
import type { Issue, IssueIcon } from '../data'
import { theme } from '../theme'

const icons: Record<IssueIcon, LucideIcon> = { takeoff: PlaneTakeoff, landing: PlaneLanding, weather: CloudSun }

function IssueItem({ issue }: { issue: Issue }) {
  const Icon = icons[issue.icon]
  return (
    <div className="relative pt-[11px] pb-[10px] pl-[52px]">
      <Icon
        size={21}
        strokeWidth={2.2}
        className="absolute top-[11px] left-[17px]"
        style={{ color: theme.maroon }}
        fill={issue.icon === 'weather' ? theme.maroon : 'none'}
      />
      <div className="text-[15px] leading-[20px] font-semibold" style={{ color: theme.maroon }}>
        {issue.title}
      </div>
      <p className="mt-[1px] pr-[8px] text-[13.5px] leading-[20.5px] tracking-[-0.1px] whitespace-pre-line text-[#7a7a7e]">{issue.text}</p>
      <div className="absolute right-0 bottom-0 left-[52px] h-px bg-[#ece6e3]" />
    </div>
  )
}

export interface IssueCardProps {
  title: string
  issues: Issue[]
  linkLabel: string
  className?: string
}

export function IssueCard({ title, issues, linkLabel, className }: IssueCardProps) {
  return (
    <div
      className={cn('relative rounded-[20px] border', className)}
      style={{ background: theme.issueBg, borderColor: theme.issueBorder }}
    >
      <div className="flex h-[55px] items-center pl-[20px]">
        <span className="relative flex h-[18px] w-[18px] items-center justify-center rounded-full bg-[#f6d5cf]">
          <span className="h-[8px] w-[8px] rounded-full bg-[#d8432f]" />
        </span>
        <span className="ml-[14px] text-[19px] font-medium tracking-[-0.2px]" style={{ color: theme.maroon }}>
          {title}
        </span>
        <Sparkles size={15} strokeWidth={2} fill={theme.maroon} className="mr-[22px] ml-auto" style={{ color: theme.maroon }} />
      </div>
      <div className="-mt-[3px]">
        {issues.map((i) => (
          <IssueItem key={i.icon} issue={i} />
        ))}
      </div>
      <div className="flex h-[44px] items-center pb-[3px] pl-[20px] text-[13px] font-medium text-[#8e8e93]">
        {linkLabel}
        <ChevronRight size={14} strokeWidth={2.2} className="ml-[2px]" />
      </div>
    </div>
  )
}
