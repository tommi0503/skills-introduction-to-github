import { AudioLines, ChevronLeft, Plus } from 'lucide-react'
import { PhoneStatus } from '../components/PhoneStatus'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { CircleButton } from '../components/CircleButton'
import { Keyboard } from '../components/Keyboard'
import { SuggestionChip } from '../components/SuggestionChip'
import { keyboard, suggestionRows } from '../data'
import { theme } from '../theme'

export function AskScreen() {
  return (
    <AppScreen>
      <PhoneStatus />
      <CircleButton icon={ChevronLeft} variant="floating" size={40} iconSize={22} className="absolute top-[56px] left-[20px]" />
      <ImagePlaceholder label="Beside AI orb" className="absolute top-[86px] left-[161px] h-[68px] w-[68px] rounded-full" />
      <h1 className="absolute inset-x-0 top-[174px] text-center text-[17px] font-bold text-[#111]">Ask anything</h1>
      <p className="absolute inset-x-0 top-[213px] text-center text-[13px] leading-[18px] text-[#9a9a9a]">
        Search and get insights from all your
        <br />
        past Beside conversations.
      </p>
      <div className="absolute top-[273px] left-[10px] flex flex-col gap-[9px]">
        {suggestionRows.map((row, i) => (
          <div key={i} className="flex gap-[12px]">
            {row.map((s) => (
              <SuggestionChip key={s.key} label={s.label} />
            ))}
          </div>
        ))}
      </div>
      <CircleButton icon={Plus} variant="floating" size={40} iconSize={22} className="absolute top-[459px] left-[19px]" />
      <div
        className="absolute top-[459px] left-[73px] flex h-[41px] w-[297px] items-center rounded-full bg-white pr-[4px] pl-[11px]"
        style={{ boxShadow: '0 2px 12px rgba(0,0,0,0.10)' }}
      >
        <span className="h-[20px] w-[2px] rounded bg-[#3aa0f0]" />
        <span className="ml-[1px] flex-1 text-[15px] text-[#c4c4c4]">Message</span>
        <CircleButton icon={AudioLines} size={33} iconSize={15} />
      </div>
      <Keyboard suggestions={keyboard.suggestions} rows={keyboard.rows} background={theme.keyboardBg} />
    </AppScreen>
  )
}
