import { AppScreen } from '../../../ui'
import { ChatHeader } from '../components/ChatHeader'
import { ClaudeMark } from '../components/ClaudeMark'
import { Chrome } from '../components/Chrome'
import { Composer } from '../components/Composer'
import { Response } from '../components/Response'
import { ResponseActions } from '../components/ResponseActions'
import { composer, conversation } from '../data'
import { theme } from '../theme'

/** Same thread scrolled to the end of the response. */
export function ResponseEndScreen() {
  return (
    <AppScreen background={theme.bg}>
      <div className="absolute inset-x-[16px] top-[-40px]">
        <Response blocks={conversation.response.slice(4)} />
        <div className="mt-[15px]">
          <ResponseActions />
        </div>
        <div className="mt-[24px] flex items-center justify-between">
          <ClaudeMark size={28} className="ml-[2px]" />
          <p className="text-right text-[12.5px] leading-[19px] whitespace-pre-line text-[#3d3d3a]">{conversation.disclaimer}</p>
        </div>
      </div>
      {/* content fades out under the floating header */}
      <div
        className="absolute inset-x-0 top-0 z-20 h-[118px]"
        style={{ background: `linear-gradient(${theme.bg} 30%, ${theme.bg}cc 60%, ${theme.bg}00)` }}
      />
      <Chrome />
      <ChatHeader variant="chat" />
      {/* thread content fades out behind the composer */}
      <div className="absolute inset-x-0 bottom-0 z-10 h-[126px] bg-[#f9f9f7]/55" />
      <Composer placeholder={composer.replyPlaceholder} trailing="voice" className="z-20" />
    </AppScreen>
  )
}
