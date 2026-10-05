import { ArrowLeft } from 'lucide-react'
import { AppScreen, HomeIndicator } from '../../../ui'
import { CodeBoxes } from '../components/CodeBoxes'
import { NumberPad } from '../components/NumberPad'
import { PhoneStatusBar } from '../components/PhoneStatusBar'
import { digitScreen as d } from '../data'
import { theme } from '../theme'

function MessageSuggestion() {
  return (
    <div className="relative flex h-[47px] flex-col items-center justify-center pt-[2px] text-black">
      <span className="absolute top-[10px] left-[30px] h-[26px] w-px bg-[#b9bac0]" />
      <span className="absolute top-[10px] right-[30px] h-[26px] w-px bg-[#b9bac0]" />
      <span className="text-[12.5px] leading-[15px]">{d.suggestionLabel}</span>
      <span className="text-[16px] leading-[19px]">{d.suggestionCode}</span>
    </div>
  )
}

export function DigitCodeScreen() {
  return (
    <AppScreen background={theme.paper} className="font-inter">
      <PhoneStatusBar />
      <ArrowLeft size={22} strokeWidth={1.8} className="absolute top-[57px] left-[15px] text-[#111]" />
      <h1 className="absolute top-[96px] left-[17px] text-[30px] leading-[38px] font-bold tracking-[0.4px] text-[#161616]">
        {d.title}
      </h1>
      <p className="absolute top-[146px] right-[24px] left-[17px] text-[13px] leading-[21px] tracking-[0.15px] text-[#8b8c90]">
        {d.subtitle}
      </p>
      <CodeBoxes
        groups={d.groups}
        gap={9}
        className="absolute top-[219px] left-[17px]"
        boxClassName="h-[50px] w-[41px] rounded-[12px] bg-[#edeef2]"
        activeClassName="!bg-[#e1e2e6]"
        caretColor={theme.link}
        separator="-"
        separatorClassName="w-[7px] text-center text-[12px] text-[#9a9a9a]"
      />
      <p className="absolute top-[287px] left-[17px] text-[13px] leading-[20px] font-medium text-[#222]">{d.resend}</p>
      <p className="absolute top-[314px] left-[17px] text-[13.5px] leading-[20px]" style={{ color: theme.link }}>
        {d.link}
      </p>
      <NumberPad top={496} accessory={<MessageSuggestion />} />
      <HomeIndicator bottom={5} width={138} />
    </AppScreen>
  )
}
