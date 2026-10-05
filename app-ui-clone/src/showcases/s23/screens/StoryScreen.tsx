import { AppHeader } from '../components/AppHeader'
import { BottomNav } from '../components/BottomNav'
import { CompanyFooter } from '../components/CompanyFooter'
import { ScrollTopButton } from '../components/ScrollTopButton'
import { SectionIntro } from '../components/SectionIntro'
import { StoryCard } from '../components/StoryCard'
import { footerButton, footerLines, stories, storyIntro } from '../data'

/** Bottom of home: story carousel and company footer. */
export function StoryScreen() {
  return (
    <div className="relative h-full w-full overflow-hidden bg-white">
      <AppHeader time="12:39" />
      <SectionIntro title={storyIntro.title} subtitle={storyIntro.subtitle} className="absolute top-[121px]" />
      <div className="absolute top-[203.4px] left-[25px] flex gap-[13px]">
        {stories.map((s) => (
          <StoryCard key={s.id} story={s} />
        ))}
      </div>
      <CompanyFooter lines={footerLines} buttonLabel={footerButton} className="absolute top-[523px]" />
      <ScrollTopButton className="top-[649px] left-[312px]" />
      <BottomNav />
    </div>
  )
}
