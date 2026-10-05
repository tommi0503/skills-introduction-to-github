import { BriefcasePlus, ChevronDown, Map, MapPin, Share, Sparkle, Star, Utensils } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { BottomPanel } from '../components/BottomPanel'
import { MenuGlyph } from '../components/MenuGlyph'
import { PhotoTile } from '../components/PhotoTile'
import { TopBar } from '../components/TopBar'
import { chat } from '../data'
import { theme } from '../theme'

export function ChatScreen() {
  return (
    <AppScreen className="font-inter" background={theme.chatBg}>
      <TopBar />
      <MenuGlyph x={22} y={76} />
      <div className="absolute flex items-center gap-[4px] text-[12.5px] font-semibold" style={{ left: 59, top: 74 }}>
        {chat.title}
        <ChevronDown size={14} strokeWidth={2} />
      </div>
      <BriefcasePlus size={20} strokeWidth={1.7} className="absolute" style={{ left: 310, top: 72 }} />
      <Share size={19} strokeWidth={1.7} className="absolute" style={{ left: 349, top: 71 }} />

      <div className="absolute flex items-center gap-[9px]" style={{ left: 16, top: 144 }}>
        <span className="flex h-[19px] w-[19px] items-center justify-center rounded-full bg-[#e5edf9] text-[10px] text-[#4a6aa8]">
          {chat.userInitial}
        </span>
        <span className="text-[16px]">{chat.question}</span>
      </div>

      <span className="absolute flex h-[19px] w-[19px] items-center justify-center rounded-full bg-black text-white" style={{ left: 16, top: 215 }}>
        <Sparkle size={11} fill="#fff" strokeWidth={0} />
      </span>
      <p className="absolute text-[15.5px] leading-[23.7px] text-[#151515]" style={{ left: 44, top: 212, width: 330 }}>
        {chat.answerLead} <MapPin size={15} strokeWidth={1.8} className="inline -mt-[3px]" />{' '}
        <b className="font-semibold">{chat.answerPlace}</b>
        {chat.answerRest}
      </p>
      <div className="absolute h-px bg-[#e2e2e2]" style={{ left: 44, right: 16, top: 320 }} />

      <div className="absolute flex items-center justify-between" style={{ left: 44, right: 16, top: 339 }}>
        <span className="flex items-center gap-[3px] text-[16px] font-medium">
          <Utensils size={15} strokeWidth={1.8} />
          {chat.place.name}
        </span>
        <span className="flex items-center gap-[3px] text-[15px]">
          <Star size={15} fill="#111" strokeWidth={0} />
          {chat.place.rating}
        </span>
      </div>
      <span className="absolute text-[12.5px] text-[#9a9a9e]" style={{ left: 44, top: 362 }}>
        {chat.place.meta}
      </span>
      <p className="absolute text-[15.5px] leading-[24.4px]" style={{ left: 44, top: 392, width: 318 }}>
        {chat.place.body}
      </p>
      <div className="absolute" style={{ left: 44, top: 527 }}>
        <PhotoTile width={330} height={200} radius={12} actions tone="#d4d4d8" />
      </div>
      <div
        className="absolute flex items-center justify-center gap-[8px] rounded-full bg-black text-[14px] text-white"
        style={{ left: 157, top: 652, width: 75, height: 30 }}
      >
        <Map size={13} strokeWidth={1.8} />
        {chat.mapLabel}
      </div>
      <BottomPanel active="chats" top={700} />
    </AppScreen>
  )
}
