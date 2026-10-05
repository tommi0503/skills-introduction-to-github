import { Button } from '../components/Button'
import { cookie } from '../data'
import { theme } from '../theme'

/** Consent toast captured in the bottom-right of the first viewport. */
export function CookieBanner() {
  return (
    <div
      className="absolute left-[1010px] top-[755px] h-[129px] w-[414px] rounded-[12px] px-[16px] pt-[16px]"
      style={{ background: theme.panel, border: '1px solid #e7e7e7', boxShadow: '0 4px 16px rgba(0,0,0,0.08)' }}
    >
      <p className="text-[14px] leading-[22.75px] font-medium" style={{ color: theme.ink }}>{cookie.title}</p>
      <p className="mt-[3px] text-[14px] leading-[22.75px] tracking-[-0.15px] whitespace-nowrap" style={{ color: theme.muted }}>
        {cookie.body} <span className="underline underline-offset-2">{cookie.link}</span>
      </p>
      <div className="mt-[16px] flex justify-end gap-[8px]">
        {cookie.actions.map((a) => (
          <Button key={a.label} variant={a.variant} size="sm" className={a.variant === 'outline' ? 'font-medium' : ''}>
            {a.label}
          </Button>
        ))}
      </div>
    </div>
  )
}
