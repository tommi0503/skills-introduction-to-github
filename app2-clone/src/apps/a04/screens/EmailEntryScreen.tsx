import { AppScreen } from '../../../ui'
import { emailForm, providers, sheet } from '../data'
import { theme } from '../theme'
import { BrowserSheet } from '../components/BrowserSheet'
import { ProviderList } from '../components/ProviderList'
import { RichText } from '../components/RichText'

/** Same sheet scrolled down: Google row has scrolled away, email form revealed. */
export function EmailEntryScreen() {
  return (
    <AppScreen>
      <BrowserSheet host={sheet.host}>
        <ProviderList items={providers} className="absolute left-[20px] right-[20px] top-[-38px]" />
        <div className="absolute left-[20px] right-[20px] top-[328px] h-px" style={{ background: theme.border }} />
        <p className="absolute left-[20px] top-[347px] text-[14px]" style={{ color: theme.muted }}>
          {emailForm.label}
        </p>
        <div
          className="absolute left-[20px] right-[20px] top-[376px] flex h-[40px] items-center rounded-[8px] px-[15px] text-[14px]"
          style={{ border: `2px solid ${theme.inputBorder}`, background: theme.inputFill, color: '#a5a6a3' }}
        >
          {emailForm.placeholder}
        </div>
        <p className="absolute left-[20px] right-[60px] top-[424px] text-[11px] leading-[16px]" style={{ color: '#a3a3a0' }}>
          {emailForm.hint}
        </p>
        <div
          className="absolute left-[20px] right-[20px] top-[480px] flex h-[40px] items-center justify-center rounded-[8px] text-[16px] font-medium text-white"
          style={{ background: theme.blue }}
        >
          {emailForm.cta}
        </div>
        <RichText
          runs={emailForm.legal}
          className="absolute left-[44px] right-[44px] top-[548px] text-[11.5px] leading-[16px] text-[#858585]"
        />
      </BrowserSheet>
    </AppScreen>
  )
}
