import { AppScreen, HomeIndicator } from '../../../ui'
import { BackButton } from '../components/BackButton'
import { BottomAction } from '../components/BottomAction'
import { PageDots } from '../components/PageDots'
import { PhoneStatusBar } from '../components/PhoneStatusBar'
import { ScreenTitle } from '../components/ScreenTitle'
import { UploadCard } from '../components/UploadCard'
import { nationalIdScreen as d } from '../data'
import { theme } from '../theme'

export function NationalIdScreen() {
  return (
    <AppScreen className="font-inter">
      <PhoneStatusBar />
      <BackButton />
      <ScreenTitle lines={[d.title]} className="top-[125px]" />
      <p className="absolute top-[171px] left-[17px] text-[16px] leading-[22px] tracking-[-0.15px]" style={{ color: theme.body }}>
        {d.subtitle}
      </p>
      <p
        className="absolute inset-x-0 top-[244px] text-center text-[16px] font-semibold tracking-[-0.2px] underline underline-offset-[3px]"
        style={{ color: theme.greenInk }}
      >
        {d.link}
      </p>
      <div className="absolute top-[307px] left-[17px] flex gap-[17px]">
        {d.slides.map((s) => (
          <UploadCard key={s} label={s} />
        ))}
      </div>
      <PageDots count={d.slides.length} active={d.activeSlide} className="absolute inset-x-0 top-[585px]" />
      <BottomAction label={d.action} />
      <HomeIndicator bottom={5} width={138} />
    </AppScreen>
  )
}
