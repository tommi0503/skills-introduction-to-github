import { ArrowDown } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { ChatHeader } from '../components/ChatHeader'
import { Chrome } from '../components/Chrome'
import { Composer } from '../components/Composer'
import { NotificationCard } from '../components/NotificationCard'
import { Response } from '../components/Response'
import { UserBubble } from '../components/UserBubble'
import { composer, conversation } from '../data'
import { floatShadow, theme } from '../theme'

/** Chat while the response is streaming (top of the thread). */
export function ConversationScreen() {
  return (
    <AppScreen background={theme.bg}>
      <Chrome />
      <ChatHeader variant="chat" />
      <div className="absolute inset-x-[16px] top-[122px]">
        <UserBubble text={conversation.prompt} />
        <div className="mt-[12px]">
          <NotificationCard {...conversation.notification} />
        </div>
        <Response blocks={conversation.response.slice(0, 8)} className="mt-[24px]" />
      </div>
      <span
        className={`absolute top-[664px] left-[174px] z-10 flex size-[40px] items-center justify-center rounded-full bg-white text-[#3d3d3a] ${floatShadow}`}
      >
        <ArrowDown size={19} strokeWidth={1.6} />
      </span>
      {/* thread content fades out behind the composer */}
      <div className="absolute inset-x-0 bottom-0 z-10 h-[126px] bg-[#f9f9f7]/55" />
      <Composer placeholder={composer.replyPlaceholder} trailing="stop" className="z-20" />
    </AppScreen>
  )
}
