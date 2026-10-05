import { theme } from '../theme'

export interface HomeTab {
  key: string
  label: string
  badge?: string
}

/** Two-tab underline header with an optional pill badge above a tab label. */
export function HomeTabs({ tabs, activeKey }: { tabs: HomeTab[]; activeKey: string }) {
  return (
    <div className="absolute inset-x-0" style={{ top: 108, height: 42 }}>
      <div className="absolute inset-x-0 bottom-0 h-[2px]" style={{ background: theme.line }} />
      <div className="flex h-full px-[20px]">
        {tabs.map((t) => {
          const active = t.key === activeKey
          return (
            <div key={t.key} className="relative flex flex-1 items-center justify-center pb-[3px]">
              <span
                className="relative text-[14px]"
                style={{ color: active ? theme.text : theme.muted, fontWeight: active ? 600 : 400 }}
              >
                {t.label}
                {t.badge && (
                  <span
                    className="absolute -top-[14px] left-[27px] rounded-full px-[7px] py-[3px] text-[10.5px] leading-none font-semibold text-white"
                    style={{ background: theme.purpleDeep }}
                  >
                    {t.badge}
                  </span>
                )}
              </span>
              {active && <span className="absolute inset-x-0 bottom-0 h-[2px] bg-[#5e5d66]" />}
            </div>
          )
        })}
      </div>
    </div>
  )
}
