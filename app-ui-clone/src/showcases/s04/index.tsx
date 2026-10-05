import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { FoodPhone } from './components/FoodPhone'
import { LetterBlocks } from './components/LetterBlocks'
import { StageCaption } from './components/StageCaption'
import { captions, letterBlocks } from './data'
import { HomeScreen } from './screens/HomeScreen'
import { RestaurantScreen } from './screens/RestaurantScreen'
import { WelcomeScreen } from './screens/WelcomeScreen'
import { theme } from './theme'

const W = 1024
const H = 768

const background = [
  'radial-gradient(ellipse 55% 22% at 50% 0%, rgba(255,58,12,0.95) 0%, rgba(255,58,12,0.5) 50%, rgba(255,58,12,0) 100%)',
  `radial-gradient(768px 435px at 50% 0%, #ff6a08 0%, #ff7806 45%, #fb7406 68%, ${theme.stageDark} 117%)`,
].join(', ')

function Showcase04() {
  return (
    <Stage width={W} height={H} background={background}>
      <LetterBlocks blocks={letterBlocks} top={19} width={134} height={150} />

      <Placed x={49} y={102}>
        <FoodPhone indicatorTone="dark">
          <WelcomeScreen />
        </FoodPhone>
      </Placed>
      <Placed x={369} y={102}>
        <FoodPhone width={285}>
          <HomeScreen />
        </FoodPhone>
      </Placed>
      <Placed x={693} y={102}>
        <FoodPhone showIndicator={false}>
          <RestaurantScreen />
        </FoodPhone>
      </Placed>

      <Placed x={19} y={724} className="font-instrument text-[22px] font-normal tracking-[-1px]" style={{ color: theme.caption }}>
        <StageCaption>{captions.left}</StageCaption>
      </Placed>
      <Placed x={600} y={724} width={392} className="font-instrument text-[22px] font-normal tracking-[-1px]" style={{ color: theme.caption }}>
        <StageCaption align="right">{captions.right}</StageCaption>
      </Placed>
    </Stage>
  )
}

const showcase: ShowcaseDefinition = { id: '04', title: 'Food Zone — food delivery', width: W, height: H, Component: Showcase04 }
export default showcase
