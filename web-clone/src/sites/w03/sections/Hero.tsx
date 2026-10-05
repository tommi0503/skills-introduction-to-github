import { ImagePlaceholder } from '../../../ui'
import { hero } from '../data'
import { Button } from '../components/Button'
import { Serif } from '../components/Type'

export function Hero() {
  return (
    <section className="px-8 pt-16">
      <div className="flex">
        <Serif as="h1" className="w-[696px] text-[72px] leading-[75.6px] tracking-[0.9px] text-[#0f0e0d]">
          {hero.title.map((line) => (
            <span key={line} className="block">
              {line}
            </span>
          ))}
        </Serif>
        <div className="w-[680px] pt-[11px]">
          <p className="w-[660px] text-[20px] leading-[26px] tracking-[-0.2px] text-[#33312c]">{hero.body}</p>
          <Button className="mt-8 h-12 w-[158px] text-[16px]">{hero.cta}</Button>
        </div>
      </div>
      <ImagePlaceholder label="Harvey Command Center product screenshot" className="mt-[64px] h-[750px] w-full rounded-[8px]" />
    </section>
  )
}
