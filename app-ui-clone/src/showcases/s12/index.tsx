import type { ComponentType } from 'react'
import { DynamicIsland, HomeIndicator, PhoneFrame, Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { FaqScreen } from './screens/FaqScreen'
import { GrowScreen } from './screens/GrowScreen'
import { LikesScreen } from './screens/LikesScreen'
import { WhyScreen } from './screens/WhyScreen'
import { device, theme } from './theme'

const screens: ComponentType[] = [LikesScreen, GrowScreen, WhyScreen, FaqScreen]
const FIRST_X = 39
const STEP = 173.67

function Showcase12() {
  return (
    <Stage width={752} height={564} background={theme.stage} className="font-geist">
      {screens.map((Screen, i) => (
        <Placed key={i} x={FIRST_X + STEP * i} y={122}>
          <PhoneFrame
            width={device.width}
            height={device.height}
            logicalWidth={device.logicalWidth}
            screenRadius={device.screenRadius}
            bezel={device.bezel}
          >
            <Screen />
            <DynamicIsland width={123} height={35} top={12.6} />
            <HomeIndicator width={147} bottom={6} />
          </PhoneFrame>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '12',
  title: 'blastup — social growth app',
  width: 752,
  height: 564,
  Component: Showcase12,
}

export default showcase
