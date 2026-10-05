import {
  ChevronDown,
  CircleEllipsis,
  FileSearch,
  House,
  Lasso,
  PanelLeft,
  PenLine,
  Share,
  Undo2,
  WandSparkles,
  X,
} from 'lucide-react'
import { cn } from '../../../ui'
import type { editor } from '../data'

const navy = '#3b4f7e'
const navyTab = '#4a5f91'

/** Document editor background: navy tab strip + toolbar, sub-toolbar and grid paper. */
export function EditorChrome({ tabs, className }: { tabs: typeof editor.tabs; className?: string }) {
  const tool = 'flex h-[32px] w-[32px] items-center justify-center'
  return (
    <div className={cn('absolute inset-0', className)}>
      <div className="absolute inset-x-0 top-0 h-[138px]" style={{ background: navy }} />
      {/* tabs */}
      <House size={16} strokeWidth={1.6} className="absolute left-[22px] top-[69px] text-white/55" />
      <div className="absolute left-[65px] top-[59px] flex">
        {tabs.map((t) => (
          <div
            key={t.label}
            className={cn(
              'flex h-[36px] items-center gap-[6px] rounded-t-[10px] pl-[14px] text-[13.5px]',
              t.active ? 'w-[157px] text-white/90' : 'w-[166px] text-white/55',
            )}
            style={{ background: t.active ? navyTab : 'transparent' }}
          >
            <span className="flex-1 truncate">
              {t.label}
              {t.menu && <ChevronDown size={11} strokeWidth={2} className="ml-[8px] inline" />}
            </span>
            <X size={13} strokeWidth={1.6} className="mr-[12px] shrink-0" />
          </div>
        ))}
      </div>
      {/* toolbar */}
      <div className="absolute inset-x-0 top-[95px] flex h-[43px] items-center pl-[5px] text-white" style={{ background: navyTab }}>
        <span className={cn(tool, 'ml-[0px] rounded-[8px] bg-white/10')}><PanelLeft size={20} strokeWidth={1.5} /></span>
        <span className={cn(tool, 'ml-[12px]')}><WandSparkles size={19} strokeWidth={1.5} /></span>
        <span className={cn(tool, 'ml-[10px]')}><FileSearch size={20} strokeWidth={1.5} /></span>
        <span className="ml-[8px] flex h-[34px] w-[45px] items-center justify-center gap-[1px] rounded-[9px] bg-white/85 text-[#333]">
          <Lasso size={19} strokeWidth={1.5} />
          <ChevronDown size={10} strokeWidth={1.8} />
        </span>
        <span className={cn(tool, 'ml-[14px]')}><PenLine size={20} strokeWidth={1.5} /></span>
        <span className="ml-[18px] flex h-[22px] w-[22px] items-center justify-center rounded-full bg-white/25">
          <ChevronDown size={13} strokeWidth={2} />
        </span>
        <span className={cn(tool, 'ml-[46px]')}><Share size={20} strokeWidth={1.5} /></span>
        <span className={cn(tool, 'ml-[10px]')}><CircleEllipsis size={21} strokeWidth={1.5} /></span>
      </div>
      {/* sub toolbar + canvas */}
      <div className="absolute inset-x-0 top-[138px] h-[46px] border-b border-[#d8d8d8] bg-white">
        <Undo2 size={20} strokeWidth={1.6} className="absolute left-[20px] top-[13px]" />
        <span className="absolute left-[56px] top-[9px] h-[28px] w-px bg-[#e2e2e2]" />
      </div>
      <div className="absolute inset-x-0 top-[184px] h-[61px] bg-[#fefefe]" />
      <div
        className="absolute inset-x-0 top-[245px] bottom-0"
        style={{
          backgroundColor: '#f8f8ee',
          backgroundImage:
            'linear-gradient(#dcdccf 1px, transparent 1px), linear-gradient(90deg, #dcdccf 1px, transparent 1px)',
          backgroundSize: '13.6px 13.6px',
          backgroundPosition: '6px 0',
        }}
      />
    </div>
  )
}
