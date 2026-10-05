import type { ComponentType } from 'react'
import { PhoneFrame, Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { EventScreen } from './screens/EventScreen'
import { HeroScreen } from './screens/HeroScreen'
import { ServiceListScreen } from './screens/ServiceListScreen'
import { StoryScreen } from './screens/StoryScreen'
import { device, theme } from './theme'

const phones: { x: number; Screen: ComponentType }[] = [
  { x: 58, Screen: HeroScreen },
  { x: 426, Screen: ServiceListScreen },
  { x: 794, Screen: EventScreen },
  { x: 1163, Screen: StoryScreen },
]

function Showcase23() {
  return (
    <Stage width={1536} height={752} background={theme.stage}>
      {phones.map(({ x, Screen }) => (
        <Placed key={x} x={x} y={device.top}>
          <PhoneFrame
            width={device.width}
            height={device.height}
            logicalWidth={device.logicalWidth}
            screenRadius={device.radius}
          >
            <Screen />
          </PhoneFrame>
        </Placed>
      ))}
      {/* Bottom sheet edge peeking below the third phone (captured in the reference). */}
      <Placed x={893} y={736} width={101} height={20} className="rounded-t-[10px] border border-[#c6c6c6] bg-[#fafafa]" />
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '23',
  title: 'Laundrygo — 월정액 서비스',
  width: 1536,
  height: 752,
  Component: Showcase23,
}
export default showcase
