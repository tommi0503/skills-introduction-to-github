import { AppScreen } from '../../../ui'
import { ChatHeader } from '../components/ChatHeader'
import { ClaudeMark } from '../components/ClaudeMark'
import { Chrome } from '../components/Chrome'
import { Composer } from '../components/Composer'
import { UpgradeBanner } from '../components/UpgradeBanner'
import { composer, emptyChat } from '../data'
import { theme } from '../theme'

export function EmptyChatScreen() {
  return (
    <AppScreen background={theme.bg}>
      <Chrome />
      <ChatHeader variant="empty" />
      <div className="absolute inset-x-0 top-[335px] flex flex-col items-center">
        <ClaudeMark size={36} />
        <p className="mt-[19px] font-times text-[25.5px] tracking-[-0.3px] text-[#262624]">{emptyChat.greeting}</p>
      </div>
      <Composer
        placeholder={composer.chatPlaceholder}
        trailing="voice"
        banner={<UpgradeBanner {...emptyChat.banner} />}
      />
    </AppScreen>
  )
}
