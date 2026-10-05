import { GoogleLogo } from '../components/GoogleLogo'
import { GScreen } from '../components/GScreen'
import { splash } from '../data'
import { theme } from '../theme'

export function SplashScreen() {
  return (
    <GScreen>
      <GoogleLogo />
      <p className="absolute inset-x-0 top-[454px] text-center text-[14px]" style={{ color: theme.text }}>
        {splash.text}
      </p>
    </GScreen>
  )
}
