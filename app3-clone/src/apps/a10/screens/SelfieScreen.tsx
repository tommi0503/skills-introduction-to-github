import { AppScreen, HomeIndicator } from '../../../ui'
import { BackButton } from '../components/BackButton'
import { BottomAction } from '../components/BottomAction'
import { CheckList } from '../components/CheckList'
import { ExamplePhotoCard } from '../components/ExamplePhotoCard'
import { PhoneStatusBar } from '../components/PhoneStatusBar'
import { ScreenTitle } from '../components/ScreenTitle'
import { selfieScreen as d } from '../data'
import { theme } from '../theme'

export function SelfieScreen() {
  return (
    <AppScreen className="font-inter">
      <PhoneStatusBar />
      <BackButton />
      <ScreenTitle lines={d.title} className="top-[125px]" />
      <div className="absolute top-[221px] right-[17px] left-[17px] flex justify-between">
        {d.examples.map((p) => (
          <ExamplePhotoCard key={p.verdict} photo={p} />
        ))}
      </div>
      <CheckList items={d.tips} className="absolute top-[507px] right-[30px] left-[18px]" />
      <div className="absolute top-[667px] left-[17px] h-[120px] w-[356px] rounded-[3px] border-[1.5px]" style={{ borderColor: theme.greenSoft }} />
      <BottomAction label={d.action} />
      <HomeIndicator bottom={5} width={138} />
    </AppScreen>
  )
}
