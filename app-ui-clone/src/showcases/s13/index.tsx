import { ImagePlaceholder, Placed, Stage, type ShowcaseDefinition } from '../../ui'
import { BookingScreen } from './screens/BookingScreen'
import { HomeScreen } from './screens/HomeScreen'
import { SplashScreen } from './screens/SplashScreen'
import { theme } from './theme'

const phones = [
  { key: 'splash', x: 48, y: 40, Screen: SplashScreen },
  { key: 'home', x: 275, y: 63, Screen: HomeScreen },
  { key: 'booking', x: 501, y: 79, Screen: BookingScreen },
]

function BarberShowcase() {
  return (
    <Stage width={752} height={564}>
      <ImagePlaceholder label="Blurred barbershop background photo" tone={theme.stageTone} className="absolute inset-0" />
      {phones.map(({ key, x, y, Screen }) => (
        <Placed key={key} x={x} y={y}>
          <Screen />
        </Placed>
      ))}
    </Stage>
  )
}

const showcase: ShowcaseDefinition = {
  id: '13',
  title: 'Branja barber booking',
  width: 752,
  height: 564,
  Component: BarberShowcase,
}
export default showcase
