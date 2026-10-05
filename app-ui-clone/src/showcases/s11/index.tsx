import type { ComponentType } from 'react'
import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { Device } from './components/Device'
import { GridPaper } from './components/GridPaper'
import { captions } from './data'
import { LibraryScreen } from './screens/LibraryScreen'
import { ReaderScreen } from './screens/ReaderScreen'
import { theme } from './theme'

const phones: { x: number; Screen: ComponentType }[] = [
  { x: 119, Screen: LibraryScreen },
  { x: 396, Screen: ReaderScreen },
]

function Showcase11() {
  return (
    <Stage width={752} height={564}>
      <GridPaper color={theme.paper} line={theme.gridLine} size={theme.gridSize} offsetX={0} offsetY={31} />
      {phones.map(({ x, Screen }) => (
        <Placed key={x} x={x} y={31}>
          <Device>
            <Screen />
          </Device>
        </Placed>
      ))}
      <Placed x={12} y={539} className="font-inter text-[13.5px] tracking-[-0.02em]" style={{ color: theme.caption }}>
        {captions.left}
      </Placed>
      <Placed x={682} y={539} className="font-inter text-[13.5px] tracking-[-0.02em]" style={{ color: theme.caption }}>
        {captions.right}
      </Placed>
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '11',
  title: 'Books app — favourite shelves & reader',
  width: 752,
  height: 564,
  Component: Showcase11,
}

export default showcase
