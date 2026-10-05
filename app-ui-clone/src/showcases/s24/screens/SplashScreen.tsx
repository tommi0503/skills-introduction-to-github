import { HomeIndicator, ImagePlaceholder } from '../../../ui'
import { TadaStatusBar } from '../components/TadaStatusBar'

/** Launch screen: centred TADA wordmark. */
export function SplashScreen() {
  return (
    <div className="relative h-full w-full bg-white">
      <TadaStatusBar time="2:15" location="badge" battery={{ level: 0.45 }} paddingX={30} paddingTop={23} />
      <ImagePlaceholder label="타다 로고" className="absolute top-[292px] left-[140px] h-[29px] w-[116px]" />
      <HomeIndicator width={138} bottom={11} className="!bg-[#9d9d9d]" />
    </div>
  )
}
