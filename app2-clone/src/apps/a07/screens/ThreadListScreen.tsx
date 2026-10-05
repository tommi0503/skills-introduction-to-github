import { Plus, Search } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { me, threads } from '../data'
import { theme } from '../theme'
import { BotStatusBar } from '../components/BotStatusBar'
import { FloatingButton } from '../components/FloatingButton'
import { ThreadRow } from '../components/ThreadRow'

export function ThreadListScreen() {
  return (
    <AppScreen>
      <BotStatusBar />
      <div
        className="absolute top-[66px] left-[17px] flex h-[40px] w-[40px] items-center justify-center rounded-full border-2 border-white bg-[#f2f2f2] text-[15px] text-[#555]"
        style={{ boxShadow: theme.floatShadow }}
      >
        {me.initials}
      </div>
      <div className="absolute top-[64px] right-[19px] flex gap-[8px]">
        <FloatingButton icon={Search} iconSize={19} />
        <FloatingButton icon={Plus} iconSize={22} />
      </div>
      <div className="absolute inset-x-0 top-[136px]">
        {threads.map((t) => (
          <ThreadRow key={t.id} thread={t} />
        ))}
      </div>
    </AppScreen>
  )
}
