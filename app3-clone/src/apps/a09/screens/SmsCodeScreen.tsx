import { ArrowLeft } from 'lucide-react'
import { AppScreen, HomeIndicator, IconButton, ImagePlaceholder } from '../../../ui'
import { CodeBoxes } from '../components/CodeBoxes'
import { NumberPad } from '../components/NumberPad'
import { PhoneStatusBar } from '../components/PhoneStatusBar'
import { smsScreen as d } from '../data'
import { theme } from '../theme'

export function SmsCodeScreen() {
  return (
    <AppScreen background="#fff" className="font-inter">
      <PhoneStatusBar />
      <IconButton
        icon={ArrowLeft}
        size={42}
        iconSize={24}
        strokeWidth={1.6}
        className="absolute top-[47px] left-[19px] bg-[#ececec] text-[#1d2a12]"
      />
      <div
        className="absolute top-[53px] right-[17px] flex h-[32px] items-center rounded-full px-[13px] text-[14px] font-medium"
        style={{ background: theme.green, color: theme.greenInk }}
      >
        {d.help}
      </div>
      <h1 className="absolute top-[121px] left-[17px] text-[30px] leading-[36px] font-semibold tracking-[-0.5px] text-[#111]">
        {d.title}
      </h1>
      <p className="absolute top-[178px] left-[17px] text-[15.5px] leading-[22px] tracking-[0.1px] text-[#505257]">
        {d.subtitle}
      </p>
      <div className="absolute top-[202px] left-[17px] flex items-center">
        <span className="text-[14px] leading-[22px] tracking-[0.5px] text-[#505257]">{d.masked}</span>
        <ImagePlaceholder className="h-[14px] w-[46px]" label="redacted phone" />
      </div>
      <CodeBoxes
        groups={[d.codeLength]}
        gap={9}
        className="absolute top-[244px] left-[17px]"
        boxClassName="h-[50px] w-[52px] rounded-[9px] border border-[#8f9094]"
        activeClassName="!border-[2.5px] !border-[#1d2a12]"
      />
      <p
        className="absolute inset-x-0 top-[337px] text-center text-[15.5px] font-semibold underline underline-offset-[3px]"
        style={{ color: theme.greenInk }}
      >
        {d.link}
      </p>
      <NumberPad
        top={488}
        accessory={
          <div
            className="flex h-[55px] items-center justify-center text-[15.5px] font-medium"
            style={{ background: theme.green, color: theme.greenInk }}
          >
            {d.action}
          </div>
        }
      />
      <HomeIndicator bottom={5} width={138} />
    </AppScreen>
  )
}
