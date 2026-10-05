import { AppScreen, HomeIndicator, ImagePlaceholder } from '../../../ui'
import { CapsuleButton } from '../components/CapsuleButton'
import { MiniProfileCard } from '../components/MiniProfileCard'
import { PageDots } from '../components/PageDots'
import { TopBar } from '../components/TopBar'
import { welcome } from '../data'

export function WelcomeScreen() {
  return (
    <AppScreen className="font-inter">
      <ImagePlaceholder className="absolute inset-x-0 top-0 h-[472px] rounded-b-[24px]" label="travel collage" />
      <ImagePlaceholder tone="#d1d5db" className="absolute rounded-[4px]" style={{ left: 131, top: 70, width: 127, height: 25 }} label="mindtrip logo" />
      <ImagePlaceholder tone="#d1d5db" className="absolute rounded-[6px]" style={{ left: 156, top: 182, width: 29, height: 28, transform: 'rotate(12deg)' }} label="heart sticker" />
      {welcome.cards.map((c) => (
        <MiniProfileCard key={c.key} card={c} />
      ))}
      <PageDots count={welcome.pages} active={welcome.activePage} top={446} />
      <TopBar />
      <h1 className="absolute inset-x-0 text-center text-[28.5px] leading-[35px] font-[650] tracking-[-0.4px]" style={{ top: 517 }}>
        {welcome.title.map((l) => (
          <span key={l} className="block">
            {l}
          </span>
        ))}
      </h1>
      <p className="absolute inset-x-0 text-center text-[15px]" style={{ top: 614 }}>
        {welcome.subtitle}
      </p>
      <CapsuleButton top={699} className="inset-x-[16px] h-[46px]">
        {welcome.next}
      </CapsuleButton>
      <CapsuleButton top={755} variant="secondary" className="inset-x-[16px] h-[46px]">
        {welcome.skip}
      </CapsuleButton>
      <HomeIndicator width={137} bottom={6} className="!bg-[#4a4a4a]" />
    </AppScreen>
  )
}
