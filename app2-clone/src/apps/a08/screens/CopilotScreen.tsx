import { ChevronDown, ChevronRight, MoreHorizontal } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { copilot, type SessionStep } from '../data'
import { gh } from '../theme'
import { GhStatusBar } from '../components/GhStatusBar'
import { NavHeader } from '../components/NavHeader'
import { HaloButton } from '../components/Halo'
import { FloatingTabBar } from '../components/FloatingTabBar'

function StepIcon({ step }: { step: SessionStep }) {
  if (step.state === 'active')
    return (
      <span className="flex h-[16px] w-[16px] items-center justify-center rounded-full border-[1.5px] border-[#c4943a]">
        <span className="h-[7px] w-[7px] rounded-full bg-[#c4943a]" />
      </span>
    )
  if (step.state === 'working')
    return (
      <span className="flex h-[16px] w-[16px] items-center justify-center rounded-full bg-[#e7effc]">
        <span className="h-[7px] w-[7px] rounded-full" style={{ background: gh.blue }} />
      </span>
    )
  const Icon = step.icon!
  return <Icon size={17} strokeWidth={1.6} className="text-[#555a62]" />
}

const STEP_HEIGHT = { active: 63, multi: 53, plain: 51, working: 40 }

function StepRow({ step }: { step: SessionStep }) {
  const primary = step.state === 'active'
  return (
    <div className="flex items-center pr-[18px] pl-[17px]" style={{ minHeight: STEP_HEIGHT[step.state ?? (step.key === 'clone' ? 'multi' : 'plain')] }}>
      <span className="flex w-[32px] shrink-0">
        <StepIcon step={step} />
      </span>
      <span className={primary ? 'flex-1 pr-[40px] text-[15.5px] leading-[21px] text-[#1f2328]' : 'flex-1 pr-[40px] text-[14.5px] leading-[20px] text-[#6b7079]'}>
        {step.label}
      </span>
      {step.trailing === 'duration' && (
        <span className="flex items-center gap-[4px] text-[15px] text-[#6b7079]">
          {step.duration}
          <ChevronDown size={14} strokeWidth={2} />
        </span>
      )}
      {step.trailing === 'chevron' && <ChevronRight size={16} strokeWidth={2} className="text-[#555a62]" />}
    </div>
  )
}

export function CopilotScreen() {
  return (
    <AppScreen background={gh.canvas}>
      <GhStatusBar />
      <NavHeader
        centered
        titleInset={70}
        title={copilot.title}
        subtitle={copilot.repo}
        right={<HaloButton icon={MoreHorizontal} iconSize={21} />}
      />
      <p className="absolute inset-x-0 top-[124px] text-center text-[12px] leading-[16px] text-[#7b8088]">{copilot.meta}</p>
      <div className="absolute top-[168px] left-[48px] w-[326px] rounded-[12px] bg-[#ebebee] px-[12px] py-[8px] text-[16px] leading-[21px] text-[#1f2328]">
        {copilot.prompt}
      </div>
      <div className="absolute top-[239px] left-[12px] w-[365px] rounded-[16px] bg-white pb-[4px]">
        {copilot.steps.map((s, i) => (
          <div key={s.key} style={{ borderTop: i === 1 ? '1px solid #f1f1f3' : undefined }}>
            <StepRow step={s} />
          </div>
        ))}
      </div>
      <div className="absolute top-[701px] left-[16px] flex h-[47px] w-[357px] items-center rounded-[14px] bg-[#fbfbfc] pr-[10px] pl-[12px]" style={{ boxShadow: '0 1px 6px rgba(0,0,0,0.04)' }}>
        <span className="flex-1 text-[16px] text-[#6b7079]">{copilot.placeholder}</span>
        <span className="h-[30px] w-[30px] rounded-full bg-[#fbe6e6]" />
      </div>
      <FloatingTabBar />
    </AppScreen>
  )
}
