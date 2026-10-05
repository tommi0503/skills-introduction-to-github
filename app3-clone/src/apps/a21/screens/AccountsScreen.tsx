import { ChevronRight, Plus } from 'lucide-react'
import { Toggle } from '../../../ui'
import { GButton } from '../components/GButton'
import { GScreen } from '../components/GScreen'
import { accounts, onboarding } from '../data'
import { theme } from '../theme'

export function AccountsScreen() {
  return (
    <GScreen>
      <h1 className="absolute left-[67px] top-[62px] font-dm text-[20.3px]" style={{ color: theme.text }}>
        {onboarding.title}
      </h1>
      <div className="absolute inset-x-0 top-[121px]">
        {accounts.map((a) => (
          <div key={a.email} className="flex h-[42px] items-center pl-[13px] pr-[20px]">
            <div
              className="flex size-[40px] items-center justify-center rounded-full text-[21px] text-white"
              style={{ background: theme.avatar }}
            >
              {a.initial}
            </div>
            <div className="ml-[14px] flex-1">
              <div className="text-[15.8px] leading-[22px]" style={{ color: theme.text }}>{a.name}</div>
              <div className="text-[13.6px] leading-[20px]" style={{ color: theme.sub }}>{a.email}</div>
            </div>
            <Toggle on={a.enabled} width={53} height={32} onColor={theme.blue} />
          </div>
        ))}
        <div className="mt-[16px] flex h-[40px] items-center pl-[13px] pr-[24px]">
          <div className="flex size-[40px] items-center justify-center rounded-full border border-[#9aa0a6]">
            <Plus size={22} strokeWidth={1.2} color="#80868b" />
          </div>
          <span className="ml-[14px] flex-1 text-[15.8px]" style={{ color: theme.text }}>{onboarding.addAccount}</span>
          <ChevronRight size={16} strokeWidth={2} color="#444" />
        </div>
      </div>
      <GButton className="left-[130px] top-[776px] h-[37px] w-[129px]">{onboarding.cta}</GButton>
    </GScreen>
  )
}
