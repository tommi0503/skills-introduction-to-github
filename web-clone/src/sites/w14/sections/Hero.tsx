import { ArrowRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { hero, logoStrip } from '../data'
import { colors, fonts } from '../theme'
import { PillButton, Text } from '../components/primitives'

/** Announcement pill, headline, subtitle and CTAs. */
export function Hero() {
  return (
    <section className={`flex h-[422px] flex-col items-center pt-[72px] ${fonts.sans}`}>
      <span
        className="flex h-[32px] items-center rounded-full border pl-[4px] pr-[8px]"
        style={{ background: colors.subtle, borderColor: colors.border }}
      >
        <span className="rounded-full px-[7px] py-[2px] text-[12px] leading-[19.2px] font-semibold text-white" style={{ background: colors.orange }}>
          {hero.badge.tag}
        </span>
        <span className="ml-[8px] text-[14px] leading-[22.4px] font-medium" style={{ color: colors.body }}>
          {hero.badge.label}
        </span>
        <ArrowRight className="ml-[10px]" size={13} strokeWidth={2} color={colors.ink} />
      </span>
      <Text role="h1" as="h1" className="mt-[24px] text-center">
        {hero.title.map((line, i) => (
          <span key={i} className="block">
            {line.map((seg) => (
              <span key={seg.text} style={seg.accent ? { color: colors.orange } : undefined}>
                {seg.text}
              </span>
            ))}
          </span>
        ))}
      </Text>
      <Text role="lead" className="mt-[24px]">
        {hero.subtitle}
      </Text>
      <div className="mt-[24px] flex gap-[10px]">
        <PillButton arrow>{hero.primary}</PillButton>
        <PillButton variant="light" leading={<ImagePlaceholder label="GitHub" className="mr-[10px] rounded-full" style={{ width: 16, height: 16 }} />}>
          {hero.github}
        </PillButton>
      </div>
    </section>
  )
}

/** Customer logos marquee (frozen) — logos are placeholders at captured positions. */
export function LogoStrip({ top }: { top: number }) {
  return (
    <>
      {logoStrip.map((r) => (
        <ImagePlaceholder key={r.x} label="customer logo" className="absolute" style={{ left: r.x, top: r.y - top, width: r.w, height: r.h }} />
      ))}
    </>
  )
}
