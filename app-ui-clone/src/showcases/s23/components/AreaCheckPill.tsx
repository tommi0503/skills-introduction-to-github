import { ChevronRight } from 'lucide-react'
import { cn } from '../../../ui'
import { theme } from '../theme'

/** Location pin glyph: lime dot on a stem (no lucide equivalent). */
function PinGlyph() {
  return (
    <span className="flex w-[20px] flex-col items-center">
      <span
        className="flex h-[15px] w-[15px] items-center justify-center rounded-full border-[1.4px] border-[#333]"
        style={{ background: theme.lime }}
      >
        <span className="h-[4px] w-[4px] rounded-full border border-[#333]" />
      </span>
      <span className="h-[7px] w-[1.4px] bg-[#333]" />
    </span>
  )
}

/** Floating "서비스 가능 지역 확인" pill. */
export function AreaCheckPill({ label, className }: { label: string; className?: string }) {
  return (
    <div
      className={cn('absolute z-20 flex h-[42px] items-center rounded-full bg-white/80 pr-[16px] pl-[13px] font-pretendard', className)}
      style={{ boxShadow: '0 2px 10px rgba(0,0,0,0.08)' }}
    >
      <PinGlyph />
      <span className="ml-[10px] text-[13.2px] font-semibold tracking-[-0.2px] text-[#1a1a1a]">{label}</span>
      <ChevronRight size={14} strokeWidth={1.8} color="#333" className="ml-[12px]" />
    </div>
  )
}
