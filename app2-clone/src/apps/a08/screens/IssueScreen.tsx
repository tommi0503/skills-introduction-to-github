import { ChevronDown, ChevronRight, CircleCheck, Info, MessageSquare, MoreHorizontal, Share, Signpost, Smile, UserRound } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { issue } from '../data'
import { gh } from '../theme'
import { GhStatusBar } from '../components/GhStatusBar'
import { NavHeader } from '../components/NavHeader'
import { Halo, HaloButton, HaloGroup } from '../components/Halo'
import { ProgressChip, StateChip } from '../components/Chips'
import { FloatingTabBar } from '../components/FloatingTabBar'

const timelineIcons = [Signpost, UserRound]

export function IssueScreen() {
  return (
    <AppScreen>
      <GhStatusBar />
      <NavHeader
        title={issue.title}
        subtitle={`${issue.owner}/${issue.repo}`}
        right={<HaloGroup icons={[Share, MoreHorizontal]} className="w-[98px]" />}
      />

      {/* header block */}
      <div className="absolute inset-x-0 top-[133px] px-[17px]">
        <div className="flex items-center gap-[8px] text-[14.5px] leading-[22px] font-medium text-[#1f2328]">
          <ImagePlaceholder label="avatar" className="h-[17px] w-[17px] rounded-[4px]" />
          <span>
            {issue.owner} / {issue.repo} <span className="font-normal text-[#6b7079]">#{issue.number}</span>
          </span>
        </div>
        <h1 className="mt-[12px] text-[21px] leading-[26px] font-semibold text-[#1f2328]">{issue.title}</h1>
        <div className="mt-[12px] flex items-center gap-[9px]">
          <StateChip label={issue.state} />
          <ProgressChip label={issue.progress} height={26} />
        </div>
      </div>
      <div className="absolute inset-x-0 top-[247px] h-[8px] bg-[#f4f4f6]" />

      {/* comment */}
      <div className="absolute inset-x-0 top-[272px] px-[17px]">
        <div className="flex items-start gap-[11px]">
          <ImagePlaceholder label="avatar" className="h-[42px] w-[42px] rounded-full" />
          <div className="flex-1">
            <div className="text-[16px] leading-[22px] text-[#1f2328]">
              {issue.author}
              <span className="text-[#6b7079]">{issue.meta}</span>
            </div>
            <span className="mt-[2px] inline-block rounded-full border border-[#e3e3e6] px-[8px] text-[11px] leading-[16px] text-[#6b7079]">
              {issue.role}
            </span>
          </div>
          <MoreHorizontal size={20} strokeWidth={2.2} className="mt-[2px] text-[#555a62]" />
        </div>
        <h3 className="mt-[14px] text-[16px] leading-[22px] font-bold text-[#1f2328]">{issue.bodyHeading}</h3>
        <ul className="mt-[18px] flex flex-col gap-[5px] pr-[4px] pl-[30px]">
          {issue.criteria.map((c) => (
            <li key={c} className="relative text-[15.5px] leading-[24.5px] text-[#1f2328]">
              <span className="absolute top-[10px] -left-[17px] h-[5px] w-[5px] rounded-full bg-[#1f2328]" />
              {c}
            </li>
          ))}
        </ul>
        <span className="mt-[12px] flex h-[30px] w-[30px] items-center justify-center rounded-full bg-[#f1f1f3] text-[#555a62]">
          <Smile size={20} strokeWidth={1.6} />
        </span>
      </div>
      <div className="absolute inset-x-0 top-[570px] h-[8px] bg-[#f4f4f6]" />

      {/* sub-issues */}
      <div className="absolute inset-x-0 top-[584px] flex items-center pr-[20px] pl-[17px]">
        <ChevronDown size={17} strokeWidth={2} className="text-[#555a62]" />
        <span className="ml-[7px] text-[17px] leading-[26px] font-semibold text-[#1f2328]">Sub-issues</span>
        <ProgressChip label={issue.progress} className="ml-[9px]" />
        <MoreHorizontal size={20} strokeWidth={2.2} className="ml-auto text-[#555a62]" />
      </div>
      {issue.subIssues.map((s) => (
        <div key={s.number} className="absolute inset-x-0 top-[627px] flex pr-[13px] pl-[40px]">
          <CircleCheck size={17} strokeWidth={1.8} style={{ color: gh.purple }} className="mt-[3px]" />
          <div className="ml-[19px] flex-1">
            <div className="text-[15px] leading-[22px] font-semibold text-[#1f2328]">
              {s.title} <span className="font-normal text-[#6b7079]">#{s.number}</span>
            </div>
            <ImagePlaceholder label="avatar" className="mt-[6px] h-[14px] w-[14px] rounded-[3px]" />
          </div>
          <ChevronRight size={17} strokeWidth={2} className="mt-[17px] text-[#b4b8be]" />
        </div>
      ))}

      {/* timeline */}
      <div className="absolute inset-x-0 top-[682px] bottom-0 bg-[#f6f6f8]">
        {issue.timeline.map((e, i) => {
          const Icon = timelineIcons[i % timelineIcons.length]
          return (
            <div key={i} className="flex h-[54px] items-center gap-[17px] pl-[25px]" style={{ marginTop: i ? 0 : 3 }}>
              <Icon size={18} strokeWidth={1.8} className="text-[#555a62]" />
              <span className="text-[14.5px] text-[#1f2328]">
                {e.actor}
                <span className="text-[#6b7079]">{e.text}</span>
              </span>
            </div>
          )
        })}
      </div>
      <Halo className="absolute top-[705px] left-[200px] h-[44px] gap-[8px] rounded-full px-[15px] text-[15.5px] font-medium text-[#1f2328]">
        <MessageSquare size={17} strokeWidth={2} />
        Comment
      </Halo>
      <HaloButton icon={Info} iconSize={19} className="absolute top-[705px] right-[17px]" />
      <FloatingTabBar />
    </AppScreen>
  )
}
