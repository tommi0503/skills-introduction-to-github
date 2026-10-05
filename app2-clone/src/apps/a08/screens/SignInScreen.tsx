import { AppScreen, ImagePlaceholder } from '../../../ui'
import { signIn } from '../data'
import { gh } from '../theme'
import { GhStatusBar } from '../components/GhStatusBar'
import { CaptionedButton } from '../components/Captioned'

export function SignInScreen() {
  const { legal } = signIn
  return (
    <AppScreen>
      <GhStatusBar />
      <ImagePlaceholder label="GitHub mark" className="absolute top-[239px] left-[159px] h-[72px] w-[72px] rounded-full" />
      <CaptionedButton
        {...signIn.primary}
        className="absolute inset-x-0 top-[492px]"
        buttonClassName="bg-[#24292f] text-white"
      />
      <CaptionedButton
        {...signIn.secondary}
        className="absolute inset-x-0 top-[603px]"
        buttonClassName="bg-[#f6f7f9] text-[#1f2328]"
      />
      <p className="absolute inset-x-[30px] top-[753px] text-center text-[12.5px] leading-[18px] text-[#1f2328]">
        {legal.before}
        <span style={{ color: gh.link }}>{legal.terms}</span>
        {legal.middle}
        <span style={{ color: gh.link }}>{legal.privacy}</span>
        {legal.after}
      </p>
    </AppScreen>
  )
}
