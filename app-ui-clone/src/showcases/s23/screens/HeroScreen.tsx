import { ImagePlaceholder } from '../../../ui'
import { AppHeader } from '../components/AppHeader'
import { AreaCheckPill } from '../components/AreaCheckPill'
import { BottomNav } from '../components/BottomNav'
import { SectionIntro } from '../components/SectionIntro'
import { ServiceList } from '../components/ServiceList'
import { areaCheck, hero, monthlyIntro, services } from '../data'
import { theme } from '../theme'

/** Home: full-bleed hero photo, white sheet with the monthly plans. */
export function HeroScreen() {
  return (
    <div className="relative h-full w-full overflow-hidden bg-white font-pretendard">
      <ImagePlaceholder label="손 씻는 사진" tone={theme.placeholderOnDark} className="absolute inset-x-0 top-0 h-[440px]" />
      <AppHeader time="12:38" tone="light" solid={false} />
      <div className="absolute top-[139px] left-[19px] text-white">
        <div className="text-[15px] font-normal leading-[18px] tracking-[0.6px]">{hero.eyebrow}</div>
        <div className="mt-[15px] font-pretendard text-[34px] font-normal leading-[34px] tracking-[0.5px]">{hero.headline}</div>
        <div className="mt-[6px] flex items-baseline text-[34px] font-normal leading-[34px]">
          {hero.brand.map((part) => (
            <span
              key={part.text}
              className={part.script ? 'mr-[4px] font-playfair font-light italic tracking-[10px]' : 'tracking-[12.5px]'}
              style={part.script ? { fontSize: 38 } : undefined}
            >
              {part.text}
            </span>
          ))}
        </div>
        <div className="mt-[28px] text-[15.2px] leading-[25px] tracking-[0px]">
          {hero.body.map((line) => (
            <div key={line}>{line}</div>
          ))}
        </div>
      </div>
      <div className="absolute top-[377px] left-[320px] flex h-[22px] w-[42px] items-center justify-center rounded-full bg-black/55 text-[11.5px] font-semibold text-white">
        {hero.pager}
      </div>
      <div className="absolute inset-x-0 top-[411.5px] bottom-0 rounded-t-[24px] bg-white">
        <SectionIntro title={monthlyIntro.title} subtitle={monthlyIntro.subtitle} className="pt-[36px]" />
        <ServiceList items={[services.allInOne, services.shirtsDry]} className="mt-[27px]" />
      </div>
      <AreaCheckPill label={areaCheck} className="top-[701px] left-[95px]" />
      <BottomNav />
    </div>
  )
}
