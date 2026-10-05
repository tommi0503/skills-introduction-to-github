import { ChevronDown, FileDiff, MessageSquareCode, MoreHorizontal, Settings } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { diff } from '../data'
import { gh } from '../theme'
import { GhStatusBar } from '../components/GhStatusBar'
import { NavHeader } from '../components/NavHeader'
import { HaloButton, HaloGroup } from '../components/Halo'
import { DiffRow } from '../components/DiffRow'
import { FloatingTabBar } from '../components/FloatingTabBar'

export function DiffScreen() {
  return (
    <AppScreen>
      <GhStatusBar />
      <NavHeader
        centered
        title={diff.title}
        titleClassName="text-[16.5px] leading-[19px] font-medium"
        subtitle={
          <span className="text-[12px] font-medium">
            <span style={{ color: '#3f8f45' }}>{diff.additions}</span> <span style={{ color: '#c4473c' }}>{diff.deletions}</span>
          </span>
        }
        right={<HaloGroup icons={[Settings, MoreHorizontal]} className="w-[98px]" />}
      />
      <div className="absolute inset-x-0 top-[112px] h-px bg-[#efeff1]" />
      <div className="absolute inset-x-0 top-[120px] flex h-[36px] items-center pr-[11px] pl-[22px] text-[#555a62]">
        <ChevronDown size={18} strokeWidth={1.8} />
        <span className="ml-[13px] font-plexmono text-[12.5px] text-[#6b7079]">{diff.file}</span>
        <MoreHorizontal size={20} strokeWidth={2.2} className="ml-auto" />
        <span className="mx-[10px] h-[22px] w-px bg-[#e3e3e6]" />
        <span className="h-[21px] w-[21px] rounded-full border-[1.6px] border-[#1f2328]" />
      </div>
      <div className="absolute inset-x-0 top-[162px] font-plexmono text-[13.3px] leading-none">
        {diff.lines.map((l, i) => (
          <DiffRow key={i} line={l} />
        ))}
      </div>
      <div
        className="absolute top-[707px] left-[149px] z-40 flex h-[41px] items-center gap-[8px] rounded-full px-[15px] text-[14.5px] font-medium text-white"
        style={{ background: gh.green }}
      >
        <MessageSquareCode size={17} strokeWidth={1.8} />
        Finish Review
        <ChevronDown size={15} strokeWidth={2.2} className="ml-[4px]" />
      </div>
      <HaloButton icon={FileDiff} iconSize={19} strokeWidth={1.8} className="absolute top-[706px] right-[17px] z-40" />
      <FloatingTabBar />
    </AppScreen>
  )
}
