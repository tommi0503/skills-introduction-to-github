import { ImagePlaceholder } from '../../../ui'
import type { SocialProvider } from '../data'
import { theme } from '../theme'

export interface SignupActionsProps {
  top: number
  cta: string
  or: string
  providers: SocialProvider[]
  haveAccount: string
  signIn: string
  refer: string
  /** Provider whose label is shown highlighted (pressed state). */
  highlightedKey?: string
}

/** Join button, "or" divider, social sign-in buttons and footer links. */
export function SignupActions({ top, cta, or, providers, haveAccount, signIn, refer, highlightedKey }: SignupActionsProps) {
  return (
    <div className="absolute inset-x-0" style={{ top }}>
      <button
        type="button"
        className="absolute flex items-center justify-center rounded-full text-[16px] font-semibold text-white shadow-[0_3px_8px_rgba(123,47,201,0.18)]"
        style={{ left: 19, top: 0, width: 351, height: 55, background: theme.purple }}
      >
        {cta}
      </button>
      <div className="absolute flex items-center gap-[12px]" style={{ left: 19, top: 73, width: 351 }}>
        <span className="h-px flex-1 bg-[#e3e3e6]" />
        <span className="text-[12px] text-[#77777d]">{or}</span>
        <span className="h-px flex-1 bg-[#e3e3e6]" />
      </div>
      {providers.map((p, i) => (
        <div
          key={p.key}
          className="absolute flex items-center justify-center gap-[9px] rounded-full bg-white text-[15px] font-semibold shadow-[0_2px_7px_rgba(0,0,0,0.09)]"
          style={{
            left: 19,
            top: 109 + i * 60,
            width: 351,
            height: 42,
            color: p.key === highlightedKey ? theme.purple : '#222',
          }}
        >
          <ImagePlaceholder className="h-[16px] w-[16px] rounded-full" label={`${p.key} logo`} />
          {p.label}
        </div>
      ))}
      <div className="absolute inset-x-0 text-center text-[14px]" style={{ top: 299 }}>
        <span className="text-[#66666c]">{haveAccount} </span>
        <span className="font-semibold" style={{ color: theme.purple }}>
          {signIn}
        </span>
      </div>
      <div className="absolute inset-x-0 text-center text-[14px] font-semibold" style={{ top: 367, color: theme.purple }}>
        {refer}
      </div>
    </div>
  )
}
