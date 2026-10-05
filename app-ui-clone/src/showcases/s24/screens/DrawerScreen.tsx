import { HomeIndicator } from '../../../ui'
import { SideDrawer } from '../components/SideDrawer'
import { TadaStatusBar } from '../components/TadaStatusBar'
import { theme } from '../theme'
import { MapHomeScreen } from './MapHomeScreen'

/** Side menu open over the dimmed home screen. */
export function DrawerScreen() {
  return (
    <div className="relative h-full w-full overflow-hidden">
      <div className="isolate h-full w-full">
        <MapHomeScreen showStatusBar={false} showLocate={false} />
      </div>
      <div className="absolute inset-0 z-10" style={{ background: theme.dim }} />
      <SideDrawer />
      <div className="absolute inset-x-0 top-0 z-30">
        <TadaStatusBar time="2:39" battery={{ level: 0.35 }} paddingX={28.6} />
      </div>
      <HomeIndicator width={138} bottom={9} />
    </div>
  )
}
