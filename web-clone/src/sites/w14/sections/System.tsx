import { ImagePlaceholder } from '../../../ui'
import { system } from '../data'
import { colors, fonts } from '../theme'
import { Chip, IconTile, Lines, Text } from '../components/primitives'

/** Section heading, platform diagram (placeholder) and four capability cards. */
export function System({ height }: { height: number }) {
  return (
    <section className={`relative flex flex-col items-center pt-[63px] ${fonts.sans}`} style={{ height }}>
      <Text role="h2lg" as="h2" className="text-center">
        <Lines lines={system.title} />
      </Text>
      <ImagePlaceholder label="system diagram" className="mt-[32px] rounded-[16px]" style={{ width: 928, height: 334 }} />
      <div className="mt-[35px] grid grid-cols-4 gap-[24px]" style={{ width: 1160 }}>
        {system.cards.map((c) => (
          <article key={c.title} className="relative h-[329px] rounded-[16px] border px-[23px] pt-[23px]" style={{ borderColor: colors.border }}>
            <IconTile icon={c.icon}>
              <ImagePlaceholder label="GitHub logo" style={{ width: 22, height: 22 }} className="rounded-full" />
            </IconTile>
            <Text role="h3" as="h3" className="mt-[16px] w-[224px]">
              {c.title}
            </Text>
            <Text role="body" className="mt-[10px] w-[224px]">
              {c.text}
            </Text>
            <Chip className="absolute bottom-[22px] left-[23px]">{c.chip}</Chip>
          </article>
        ))}
      </div>
    </section>
  )
}
