import { ImagePlaceholder } from '../../../ui'
import { GButton } from '../components/GButton'
import { GScreen } from '../components/GScreen'
import { gmailIntro } from '../data'
import { theme } from '../theme'

export function GmailIntroScreen() {
  return (
    <GScreen>
      <ImagePlaceholder label="Gmail travel illustration" className="absolute" style={{ left: 22, top: 100, width: 345, height: 312 }} />
      <div className="absolute inset-x-0 top-[450px] text-center" style={{ color: theme.text }}>
        <h1 className="font-dm text-[24px] leading-[28px]">{gmailIntro.title}</h1>
        <p className="mt-[11px] text-[16px] font-medium leading-[20px]">
          {gmailIntro.body.map((l) => (
            <span key={l} className="block">{l}</span>
          ))}
        </p>
        <p className="mt-[12px] text-[12.5px]" style={{ color: theme.sub }}>{gmailIntro.note}</p>
      </div>
      <GButton className="left-[146px] top-[598px] h-[37px] w-[96px]">{gmailIntro.cta}</GButton>
    </GScreen>
  )
}
