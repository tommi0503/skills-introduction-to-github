import { Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { latestReleases, tracks } from './data'
import { MoodHomeScreen } from './screens/MoodHomeScreen'
import { PlayerScreen } from './screens/PlayerScreen'
import { moodThemes, palette } from './theme'

/** Measured placement (stage px) and tilt of each device. */
const devices = [
  { key: 'blue', x: 35, y: 45, rotate: 4.9, node: <MoodHomeScreen theme={moodThemes.blue} latest={latestReleases.neon} /> },
  { key: 'teal', x: 272.5, y: 40.5, rotate: -3.1, zIndex: 2, node: <PlayerScreen theme={moodThemes.teal} track={tracks[0]} played={9} /> },
  { key: 'red', x: 501, y: 42.5, rotate: 4.0, node: <MoodHomeScreen theme={moodThemes.red} latest={latestReleases.crimson} /> },
]

function MoodShowcase() {
  return (
    <Stage width={752} height={564} background={palette.stage}>
      {devices.map((d) => (
        <Placed key={d.key} x={d.x} y={d.y} rotate={d.rotate} zIndex={'zIndex' in d ? d.zIndex : 1}>
          {d.node}
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '14',
  title: 'Mood music app',
  width: 752,
  height: 564,
  Component: MoodShowcase,
}
export default showcase
