import type { ComponentType } from 'react'
import { PhoneFrame, Placed, Stage, type ShowcaseDefinition, DynamicIsland } from '../../ui'
import { ExploreScreen } from './screens/ExploreScreen'
import { HomeScreen } from './screens/HomeScreen'
import { OnboardingScreen } from './screens/OnboardingScreen'
import { font, phone, theme } from './theme'

const phones: { x: number; y: number; Screen: ComponentType }[] = [
  { x: 38, y: 78, Screen: OnboardingScreen },
  { x: 277, y: 51, Screen: HomeScreen },
  { x: 514, y: 78, Screen: ExploreScreen },
]

function Showcase10() {
  return (
    <Stage width={752} height={564} background={theme.stage} className={font}>
      {phones.map(({ x, y, Screen }) => (
        <Placed key={x} x={x} y={y}>
          <PhoneFrame
            width={phone.width}
            height={phone.height}
            logicalWidth={phone.logicalWidth}
            screenRadius={phone.radius}
            screenBackground={theme.screen}
            style={{ boxShadow: theme.phoneShadow }}
          >
            <Screen />
            <DynamicIsland width={114} height={35} top={12} />
          </PhoneFrame>
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '10',
  title: 'Snacks app — onboarding, home & explore',
  width: 752,
  height: 564,
  Component: Showcase10,
}

export default showcase
