import { ImagePlaceholder } from '../../../ui'
import { launch } from '../data'
import { Button } from '../components/Button'
import { Serif } from '../components/Type'

export function Launch() {
  return (
    <section className="flex flex-col items-center px-8 pt-[160px]">
      <span className="flex h-7 w-[49px] items-center justify-center rounded-[8px] bg-[#0f0e0d] text-[12px] font-medium uppercase leading-3 text-[#fafaf9]">
        {launch.badge}
      </span>
      <Serif className="mt-[33px] text-[48px] leading-[50.4px] tracking-[0.4px] text-[#0f0e0d]">{launch.title}</Serif>
      <p className="mt-4 w-[560px] text-center text-[20px] leading-[26px] tracking-[-0.3px] text-[#33312c]">{launch.body}</p>
      <Button className="mt-8 h-12 w-[158px] text-[16px]">{launch.cta}</Button>
      <ImagePlaceholder label="Harvey II launch video" className="mt-16 h-[774px] w-full rounded-[10px]" />
    </section>
  )
}
