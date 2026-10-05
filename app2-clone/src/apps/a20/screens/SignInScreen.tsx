import { CircleHelp } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { GnStatusBar } from '../components/GnStatusBar'
import { IconCircle } from '../components/IconCircle'
import { AuthButton } from '../components/AuthButton'
import { signIn } from '../data'
import { gn } from '../theme'

export function SignInScreen() {
  return (
    <AppScreen className="font-dm">
      <GnStatusBar />
      <IconCircle
        icon={CircleHelp}
        size={46}
        iconSize={22}
        strokeWidth={1.5}
        className="absolute left-[329px] top-[56px] bg-white shadow-[0_2px_14px_rgba(0,0,0,0.08)]"
      />
      <h1 className="absolute inset-x-0 top-[302px] text-center text-[20px] font-semibold text-black">{signIn.title}</h1>
      <div className="absolute left-[24px] right-[24px] top-[370px] flex flex-col gap-[12px]">
        {signIn.options.map((o) => (
          <AuthButton key={o.key} option={o} />
        ))}
      </div>
      <div className="absolute left-[27px] right-[24px] top-[596px] flex items-center justify-between text-[15px]">
        <span className="flex items-center gap-[9px] font-medium text-[#222]">
          <span className="h-[18px] w-[18px] rounded-[4px] border-[1.5px] border-[#999]" />
          {signIn.remember}
        </span>
        <span style={{ color: gn.link }}>{signIn.trouble}</span>
      </div>
    </AppScreen>
  )
}
