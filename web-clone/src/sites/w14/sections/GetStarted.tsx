import { Copy } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { getStarted } from '../data'
import { colors, fonts } from '../theme'
import { Text } from '../components/primitives'

/** "Get started with AI" agent picker. */
export function GetStarted({ height }: { height: number }) {
  return (
    <section className={`flex flex-col items-center pt-[85px] ${fonts.sans}`} style={{ height }}>
      <Text role="h2" as="h3">
        {getStarted.title}
      </Text>
      <div
        className="mt-[17px] flex h-[70px] w-[749px] items-center gap-[12px] rounded-full border px-[15px]"
        style={{ borderColor: colors.orange, background: colors.orangeTint }}
      >
        {getStarted.agents.map((a) => (
          <span key={a} className="flex h-[38px] flex-1 items-center justify-center gap-[6px] rounded-full bg-white text-[14px] leading-[22.4px] font-semibold" style={{ color: colors.ink }}>
            <ImagePlaceholder label={`${a} logo`} style={{ width: 18, height: 18 }} />
            {a}
          </span>
        ))}
      </div>
      <div className="mt-[21px] flex items-center gap-[8px]">
        <span className="text-[14px] leading-[22.4px] font-semibold" style={{ color: colors.ink }}>
          {getStarted.setup}
        </span>
        <span className="flex h-[28px] items-center gap-[8px] rounded-full px-[12px] text-[14px] leading-[14px] font-medium tracking-[-0.28px]" style={{ background: colors.subtle, color: colors.body }}>
          <Copy size={14} strokeWidth={1.6} />
          {getStarted.copy}
        </span>
      </div>
    </section>
  )
}
