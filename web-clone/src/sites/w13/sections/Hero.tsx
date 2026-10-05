import { ArrowRight, ChevronDown, Play, Snowflake } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { hero } from '../data'
import { theme } from '../theme'
import { Badge } from '../components/Badge'
import { IconStack } from '../components/IconStack'

/** Video hero with prompt composer. */
export function Hero() {
  const p = hero.prompt
  return (
    <section className="absolute left-[40px] top-[40px] h-[824px] w-[1345px] overflow-hidden rounded-b-[36px] text-[#e9ebdf]">
      <ImagePlaceholder label="Product video" tone={theme.tones.hero} className="absolute inset-0" />
      <h1 className="absolute left-0 top-[200px] m-0 w-full text-center font-inter text-[72px] leading-[75.6px] font-light tracking-[-4px]">
        {hero.title}
      </h1>
      <div className="absolute left-[508px] top-[308px] flex items-center gap-[8px]">
        <Badge>{hero.badge}</Badge>
        <span className="font-geist text-[14px] tracking-[0.14px]">{hero.tagline}</span>
      </div>

      <div className="absolute left-[352px] top-[353px] h-[186px] w-[642px] rounded-[18px] border-[3px] border-[#d8d6cf] bg-[#e7e8dc] text-[#151515]">
        <p className="m-0 ml-[13px] mt-[14px] w-[560px] font-inter text-[16px] leading-[24px] font-light tracking-[0.1px] text-[#151515]/70">
          {p.before}{' '}
          <span className="whitespace-nowrap">
            <Snowflake size={11} className="mb-[2px] inline text-[#29b5e8]" /> <span className="text-[#151515]/40">@</span>
            <span className="underline decoration-[#151515]/40 underline-offset-2">{p.mention}</span>
          </span>{' '}
          {p.after}
        </p>
        <span className="absolute left-[14px] top-[141px] flex h-[28px] items-center gap-[4px] rounded-[6px] border border-black/10 bg-black/[0.05] px-[8px] font-geist text-[14px] text-[#242424]">
          {hero.starter}
          <ChevronDown size={14} />
        </span>
        <span className="absolute left-[590px] top-[134px] flex h-[40px] w-[40px] items-center justify-center rounded-full text-white" style={{ background: theme.colors.accent }}>
          <ArrowRight size={18} />
        </span>
      </div>

      {hero.chips.map((c) => (
        <span
          key={c.label}
          className="absolute top-[550px] flex h-[38px] items-center gap-[8px] rounded-[8px] bg-[#e9e7ea]/90 pl-[12px] font-geist text-[14px] tracking-[0.14px] text-[#151515]/60"
          style={{ left: c.x - 40, width: c.w }}
        >
          <IconStack count={c.icons} />
          {c.label}
          <ChevronDown size={14} />
        </span>
      ))}

      <span className="absolute left-[540px] top-[752px] flex h-[40px] w-[265px] items-center rounded-full bg-[#151515] pl-[16px] font-geist text-[14px] tracking-[0.14px]">
        <span className="text-[#e9ebdf]/70">{hero.film.lead}</span>
        <span className="ml-[6px]">{hero.film.cta}</span>
        <span className="ml-[12px] flex h-[24px] w-[24px] items-center justify-center rounded-full bg-[#e9ebdf] text-[#242424]">
          <Play size={12} fill="currentColor" className="ml-[2px]" />
        </span>
      </span>
      <span className="absolute left-[40px] top-[762px] flex h-[30px] w-[30px] items-center justify-center rounded-full border border-white/20 bg-black/20">
        <Play size={11} fill="currentColor" className="ml-[2px]" />
      </span>
    </section>
  )
}
