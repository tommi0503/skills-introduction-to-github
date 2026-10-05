import { TextAlignStart } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { AiSuggestion } from '../components/AiSuggestion'
import { MailCard } from '../components/MailCard'
import { PriorityEnvelope } from '../components/PriorityEnvelope'
import { ScreenTitle } from '../components/ScreenTitle'
import { SoftIconButton } from '../components/SoftIconButton'
import { SparkFab } from '../components/SparkFab'
import { inbox } from '../data'

export function InboxScreen() {
  return (
    <div className="absolute inset-0 bg-white font-inter">
      <ScreenTitle
        title={inbox.title}
        className="absolute left-[18px] right-[17px] top-[66px]"
        trailing={
          <>
            <SoftIconButton icon={TextAlignStart} />
            <ImagePlaceholder label="profile photo" className="h-[48px] w-[49px] rounded-[10px]" />
          </>
        }
      />

      <div className="absolute left-[18px] top-[136px]">
        <PriorityEnvelope label={inbox.priorityLabel} count={inbox.count} countLabel={inbox.countLabel} />
      </div>

      <p className="absolute left-[18px] top-[405px] text-[15px] text-[#555]">{inbox.sectionLabel}</p>

      <div className="absolute left-[18px] top-[445px] w-[342px]">
        <MailCard {...inbox.mail} footer={<AiSuggestion {...inbox.suggestion} />} />
      </div>

      <div className="absolute left-[147px] top-[687px]">
        <SparkFab />
      </div>
    </div>
  )
}
