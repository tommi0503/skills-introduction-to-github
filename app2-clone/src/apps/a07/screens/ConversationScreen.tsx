import { ChevronLeft, Monitor } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { conversation } from '../data'
import { theme } from '../theme'
import { BotStatusBar } from '../components/BotStatusBar'
import { FloatingButton } from '../components/FloatingButton'
import { MessageBubble } from '../components/MessageBubble'
import { FileChip } from '../components/FileChip'
import { OptionList } from '../components/OptionList'
import { Composer } from '../components/Composer'

export function ConversationScreen() {
  const [first, second] = conversation.messages
  return (
    <AppScreen>
      {/* scrolled transcript — the first bubble is partially under the header */}
      <div className="absolute left-[16px] flex flex-col items-start gap-[9px]" style={{ bottom: 844 - 746 }}>
        <MessageBubble>{first}</MessageBubble>
        <MessageBubble>{second}</MessageBubble>
        <FileChip {...conversation.file} />
        <MessageBubble className="pt-[13px] pb-[14px]">
          <p className="mb-[10px]">{conversation.question}</p>
          <OptionList options={conversation.options} />
        </MessageBubble>
      </div>
      <div className="pointer-events-none absolute inset-x-0 top-0 h-[120px] bg-gradient-to-b from-white via-white/80 to-white/0" />
      <BotStatusBar />
      <FloatingButton icon={ChevronLeft} iconSize={22} className="absolute top-[64px] left-[18px]" />
      <div
        className="absolute top-[64px] left-[70px] flex h-[44px] items-center gap-[10px] rounded-full bg-white pr-[16px] pl-[10px]"
        style={{ boxShadow: theme.floatShadow }}
      >
        <ImagePlaceholder label="bot avatar" className="h-[25px] w-[25px] rounded-full" />
        <span className="text-[16px] font-[450] text-[#111]">{conversation.bot}</span>
      </div>
      <FloatingButton icon={Monitor} iconSize={19} className="absolute top-[64px] right-[19px]" />
      <div className="absolute inset-x-[30px] top-[773px]">
        <Composer placeholder={conversation.placeholder} />
      </div>
    </AppScreen>
  )
}
