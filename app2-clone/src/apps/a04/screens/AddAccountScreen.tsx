import { AppScreen } from '../../../ui'
import { providers, sheet } from '../data'
import { theme } from '../theme'
import { AppLogo } from '../components/AppLogo'
import { BrowserSheet } from '../components/BrowserSheet'
import { ProviderList } from '../components/ProviderList'

export function AddAccountScreen() {
  return (
    <AppScreen>
      <BrowserSheet host={sheet.host}>
        <AppLogo className="absolute left-[152px] top-[48px] h-[86px] w-[93px]" />
        <div className="absolute inset-x-0 top-[171px] text-center text-[21.5px] font-semibold leading-[26px]">
          <p style={{ color: theme.text }}>{sheet.title}</p>
          {sheet.subtitle.map((l) => (
            <p key={l} style={{ color: theme.faint }}>{l}</p>
          ))}
        </div>
        <ProviderList items={providers} className="absolute left-[20px] right-[22px] top-[279px]" />
      </BrowserSheet>
    </AppScreen>
  )
}
