import { AppScreen, HomeIndicator } from '../../../ui'
import { welcome } from '../data'
import { theme } from '../theme'
import { AppLogo } from '../components/AppLogo'
import { RichText } from '../components/RichText'
import { StatusRow } from '../components/StatusRow'

export function WelcomeScreen() {
  return (
    <AppScreen>
      <StatusRow />
      <AppLogo className="absolute left-[163px] top-[258px] h-[62px] w-[66px]" />
      <div className="absolute inset-x-0 top-[367px] text-center text-[20.8px] leading-[28px] tracking-[-0.2px]">
        <p className="font-semibold" style={{ color: theme.text }}>{welcome.title}</p>
        <p className="font-medium" style={{ color: theme.muted }}>{welcome.subtitle}</p>
      </div>
      <div
        className="absolute left-[23px] right-[24px] top-[594px] flex h-[49px] items-center justify-center rounded-[12px] text-[15px] font-semibold"
        style={{ border: `1px solid ${theme.border}`, color: theme.text }}
      >
        {welcome.cta}
      </div>
      <RichText
        runs={welcome.legal}
        className="absolute left-[20px] right-[20px] top-[726px] text-[12px] leading-[16px] text-[#858585]"
      />
      <HomeIndicator bottom={6} width={138} />
    </AppScreen>
  )
}
