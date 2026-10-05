import { AppScreen } from '../../../ui'
import { StationTopBar } from '../components/StationTopBar'
import { StatusOverlay } from '../components/StatusOverlay'
import { TideCurve } from '../components/TideCurve'
import { TideSummary } from '../components/TideSummary'
import { TideTabBar } from '../components/TideTabBar'
import { currentStation, fallingTide, tideConditions } from '../data'

const X0 = 0
const PX_PER_HOUR = 25.6

export function FallingTideScreen() {
  const scrubX = X0 + fallingTide.scrub.hour * PX_PER_HOUR
  return (
    <AppScreen background="linear-gradient(#2e4272 0%, #44568a 45%, #4e5f8e 65%, #4f6b9c 100%)" className="font-inter text-white">
      <StatusOverlay chipClassName="bg-[#4f5f84]!" />
      <StationTopBar station={currentStation} conditions={tideConditions} />
      <TideSummary />
      <TideCurve
        className="absolute top-0 left-0"
        extremes={fallingTide.curve}
        width={390}
        height={844}
        x0={X0}
        pxPerHour={PX_PER_HOUR}
        yHigh={505.8}
        yLow={682.5}
        nowHour={6.5}
        strokeWidth={4}
        futureColor="#3a8ae0"
        pastColor="#f2f4f8"
        fillTop="rgba(60,120,190,0.5)"
        fillBottom="rgba(80,130,190,0.45)"
        labels={{ timeSize: 17, heightSize: 14, timeGap: 17, heightGap: 17, unit: 'm', heightColor: 'rgba(255,255,255,0.6)' }}
        dotRadius={3.5}
      />
      <div
        className="absolute flex items-center justify-center rounded-full border border-white/40 bg-white/25"
        style={{ left: scrubX - 13, top: 497, width: 26, height: 26 }}
      >
        <span className="flex h-[11px] w-[11px] items-center justify-center rounded-full bg-white">
          <span className="h-[5px] w-[5px] rounded-full bg-[#3a8ae0]" />
        </span>
      </div>
      <div className="absolute leading-none whitespace-nowrap" style={{ left: scrubX - 24, top: 434 }}>
        <div className="text-[17px] font-bold">{fallingTide.scrub.value}</div>
        <div className="mt-[3px] pl-[6px] text-[10.5px] font-semibold text-white/85">{fallingTide.scrub.time}</div>
        <div className="mt-[2px] pl-[6px] text-[9.5px] text-white/55">{fallingTide.scrub.day}</div>
      </div>
      <TideTabBar active="today" className="top-[763px] left-[20px] w-[347px]" />
    </AppScreen>
  )
}
