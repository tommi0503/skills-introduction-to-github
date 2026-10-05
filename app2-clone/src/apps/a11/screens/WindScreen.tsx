import { AppScreen } from '../../../ui'
import { Compass } from '../components/Compass'
import { DirectionBadge } from '../components/DirectionBadge'
import { StationTopBar } from '../components/StationTopBar'
import { StatusOverlay } from '../components/StatusOverlay'
import { TideCurve } from '../components/TideCurve'
import { TideTabBar } from '../components/TideTabBar'
import { currentStation, wind, windConditions, windDayCurve } from '../data'

export function WindScreen() {
  return (
    <AppScreen background="linear-gradient(#3d4b70 0%, #56627f 40%, #6a7187 75%, #6c7488 100%)" className="font-inter text-white">
      <StatusOverlay chipClassName="bg-[#5d6680]!" />
      <StationTopBar station={currentStation} conditions={windConditions} />
      <Compass cx={194} cy={335.5} size={197} speed={wind.speed} direction={wind.direction} gusts={wind.gusts} />
      <DirectionBadge x={54} y={323} size={38} value={wind.badge} caption="WIND" arrow={{ x: 85, y: 326, rotate: 0 }} />
      <DirectionBadge x={318} y={397} size={36} value={wind.swell} caption="SWELL" arrow={{ x: 291, y: 386, rotate: 90 }} />
      <TideCurve
        className="absolute top-0 left-0"
        extremes={windDayCurve}
        width={390}
        height={844}
        x0={-307.6}
        pxPerHour={26.5}
        yHigh={510.5}
        yLow={622.5}
        nowHour={17.95}
        strokeWidth={4}
        futureColor="#3f8ad8"
        pastColor="#f2f4f8"
        fillTop="rgba(70,125,185,0.75)"
        fillBottom="rgba(100,130,165,0.45)"
        labels={{ timeSize: 17, heightSize: 14, timeGap: 17, heightGap: 17.5, unit: 'm', heightColor: 'rgba(255,255,255,0.6)' }}
        dotRadius={3.5}
      />
      <TideTabBar active="today" className="top-[765px] left-[20px] w-[347px]" />
    </AppScreen>
  )
}
