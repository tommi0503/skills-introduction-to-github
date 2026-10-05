import { PhoneFrame, Placed, Stage, StatusBar, type ShowcaseDefinition } from '../../ui'

function Showcase() {
  return (
    <Stage width={1024} height={768} background="#efe8df">
      <Placed x={111} y={125}>
        <PhoneFrame width={239} height={517} logicalWidth={375} screenRadius={0}>
          <StatusBar />
        </PhoneFrame>
      </Placed>
    </Stage>
  )
}

const showcase: ShowcaseDefinition = { id: '03', title: 'Streak habits', width: 1024, height: 768, Component: Showcase }
export default showcase
