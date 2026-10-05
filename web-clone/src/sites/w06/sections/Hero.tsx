import { ArrowUpRight, ChevronRight } from 'lucide-react'
import { hero } from '../data'
import { theme } from '../theme'
import { PillButton } from '../components/PillButton'

export function Hero() {
  return (
    <section className="flex flex-col items-center" style={{ color: theme.ink, paddingTop: 84 }}>
      <div className="flex h-[38px] items-center rounded-full border border-[#ececec] pl-[10px] pr-[6px]">
        <span
          className="flex h-[17px] items-center rounded-full px-[7px] text-[11px] font-[450]"
          style={{ color: theme.orange, background: 'rgba(255,99,8,0.1)' }}
        >
          {hero.badge}
        </span>
        <span className="ml-[10px] text-[13px] font-[450]">{hero.announcement}</span>
        <span className="mx-[4px] text-[13px] text-black/20">·</span>
        <span className="text-[13px]">{hero.announcementSub}</span>
        <span className="ml-[10px] flex size-6 items-center justify-center rounded-full" style={{ background: '#f5f5f5' }}>
          <ArrowUpRight size={12} strokeWidth={2} />
        </span>
      </div>
      <h1 className="mt-[32px] text-center text-[60px] leading-[60px] tracking-[-1.6px]" style={{ fontWeight: 420 }}>
        {hero.lines[0]}
        <br />
        {hero.lines[1]}{' '}
        <span className="relative">
          {hero.underlined}
          <span className="absolute left-0 h-[3px] w-[128px] rounded-full" style={{ top: 61, background: '#c1c1c1' }} />
        </span>
        {hero.tail}
      </h1>
      <p className="mt-[20px] text-[18px] leading-[29.25px]">{hero.sub}</p>
      <div className="mt-[36px] flex gap-3">
        <PillButton variant="dark" height={44} className="w-[159px] gap-[6px] pl-[4px]">
          {hero.primary}
          <ChevronRight size={16} strokeWidth={2.2} />
        </PillButton>
        <PillButton variant="soft" height={44} className="w-[177px]">
          {hero.secondary}
        </PillButton>
      </div>
    </section>
  )
}
