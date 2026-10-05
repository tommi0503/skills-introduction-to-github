import { ImagePlaceholder } from '../../../ui'
import { platform, type AudienceCard } from '../data'
import { Button } from '../components/Button'
import { Serif } from '../components/Type'

function Card({ card }: { card: AudienceCard }) {
  return (
    <ImagePlaceholder
      tone={card.tone}
      label={`${card.title} background`}
      className="h-[688px] w-[680px] rounded-[8px]"
    />
  )
}

function CardContent({ card }: { card: AudienceCard }) {
  return (
    <div className="absolute inset-0 p-8 text-[#fafaf9]">
      <Serif as="h3" className="text-[32px] leading-[33.6px] tracking-[0.2px]">
        {card.title}
      </Serif>
      <p className="mt-4 w-[300px] text-[16px] leading-[20.8px] tracking-[-0.16px]">{card.body}</p>
      <Button variant="outline" className="mt-4 h-8 px-[12px] text-[14px] font-normal leading-5 tracking-[-0.2px]">
        {card.cta}
      </Button>
      <ImagePlaceholder label={`${card.title} product screenshot`} className="absolute left-[84px] top-[224px] h-[547px] w-[979px] rounded-[8px]" />
    </div>
  )
}

export function Platform() {
  return (
    <section className="px-8">
      <Serif className="text-center text-[48px] leading-[50.4px] tracking-[0.4px] text-[#0f0e0d]">{platform.title}</Serif>
      <p className="mx-auto mt-4 w-[560px] text-center text-[16px] leading-[20.8px] tracking-[-0.16px] text-[#0f0e0d]">{platform.body}</p>
      <div className="mt-[68px] flex gap-4">
        {platform.cards.map((card) => (
          <div key={card.title} className="relative overflow-hidden rounded-[8px]">
            <Card card={card} />
            <CardContent card={card} />
          </div>
        ))}
      </div>
    </section>
  )
}
