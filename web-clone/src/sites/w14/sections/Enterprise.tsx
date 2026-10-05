import type { LucideIcon } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { enterprise } from '../data'
import { fonts } from '../theme'
import { IconTile, Lines, PillButton, Text } from '../components/primitives'

function FeatureColumn({ items }: { items: Array<{ icon: LucideIcon; title: string; text: string }> }) {
  return (
    <div className="flex w-[232px] flex-col gap-[100px]">
      {items.map((f) => (
        <div key={f.title} className="h-[190px]">
          <IconTile icon={f.icon} />
          <Text role="h3" as="h5" className="mt-[10px]">
            {f.title}
          </Text>
          <Text role="body" className="mt-[12px]">
            {f.text}
          </Text>
        </div>
      ))}
    </div>
  )
}

/** Enterprise pitch: heading, CTA and feature list around a placeholder visual. */
export function Enterprise() {
  return (
    <section className={`flex flex-col items-center pt-[82px] ${fonts.sans}`}>
      <Text role="h2lg" as="h2">
        {enterprise.title}
      </Text>
      <Text role="lead" className="mt-[16px] text-center">
        <Lines lines={enterprise.text} />
      </Text>
      <PillButton arrow className="mt-[15px]">
        {enterprise.cta}
      </PillButton>
      <div className="mt-[48px] flex w-[1160px] justify-between">
        <FeatureColumn items={enterprise.left} />
        <ImagePlaceholder label="security & compliance visual" className="rounded-[24px]" style={{ width: 568, height: 480 }} />
        <FeatureColumn items={enterprise.right} />
      </div>
    </section>
  )
}
