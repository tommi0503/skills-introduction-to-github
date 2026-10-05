import { ArrowUp, Smile } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { HighlightStatusBar } from '../components/HighlightStatusBar'
import { Keyboard } from '../components/Keyboard'
import { NavHeader } from '../components/NavHeader'
import { CountPill, PromptBar } from '../components/PromptBar'
import { discover, qwertyRows, suggestions } from '../data'
import { bond } from '../theme'

function SuggestionPill({ emoji, text }: { emoji: string; text: string }) {
  return (
    <div className="flex h-[46px] items-center gap-[7px] rounded-full bg-[#ececec] px-[13px] text-[15.5px] text-[#222]" style={{ letterSpacing: -0.2 }}>
      <span className="text-[16px]">{emoji}</span>
      {text}
    </div>
  )
}

function ParticipantPill({ initials }: { initials: string }) {
  return (
    <div className="flex h-[39px] items-center rounded-full bg-white pr-[8px] pl-[7px]" style={{ boxShadow: '0 2px 8px rgba(0,0,0,0.05)' }}>
      <ImagePlaceholder label="avatar" className="h-[24px] w-[24px] rounded-full" />
      <span className="-ml-[5px] flex h-[24px] w-[24px] items-center justify-center rounded-full bg-[#ececec] text-[14px] text-[#222]">
        {initials}
      </span>
    </div>
  )
}

export function DiscoverScreen() {
  return (
    <div className="relative h-full font-inter" style={{ background: bond.screen }}>
      <HighlightStatusBar />
      <NavHeader center={<span className="text-[20.5px] text-[#3a3a3a]">{discover.title}</span>} />

      <div className="absolute inset-x-0 flex flex-col items-center gap-[8.3px]" style={{ top: 189 }}>
        {suggestions.map((s) => (
          <SuggestionPill key={s.text} {...s} />
        ))}
      </div>

      <div className="absolute inset-x-0 flex justify-center gap-[9px]" style={{ top: 427 }}>
        <CountPill count={discover.memoryCount} className="h-[39px] bg-white px-[11px] shadow-[0_2px_8px_rgba(0,0,0,0.06)]" />
        <ParticipantPill initials={discover.participant} />
      </div>

      <PromptBar
        text={discover.query}
        className="absolute"
        style={{ left: 16, width: 360, top: 478.5 }}
        trailing={
          <div className="flex h-[40px] w-[40px] items-center justify-center rounded-full bg-black text-white">
            <ArrowUp size={22} strokeWidth={1.8} />
          </div>
        }
      />

      <Keyboard
        rows={qwertyRows}
        className="absolute inset-x-0 bottom-0"
        style={{ top: 544 }}
        footer={<Smile className="absolute text-[#222]" size={28} strokeWidth={2} style={{ left: 28, top: 252 }} />}
      />
    </div>
  )
}
