import { CalendarDays, ChevronLeft, CirclePlus, EllipsisVertical, Phone, Plus, SendHorizontal, Smile } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { ChatEntry } from '../components/ChatParts'
import { Chrome } from '../components/Chrome'
import { EmojiGlyph } from '../components/EmojiGlyph'
import { chat, messages } from '../data'
import { kr } from '../theme'

const actionIcons = {
  date: <CalendarDays size={14} strokeWidth={2.2} fill="#222" stroke="#fff" />,
  pay: <span className="h-[13px] w-[13px] rounded-full bg-[#222]" />,
  add: <CirclePlus size={15} strokeWidth={2} fill="#222" stroke="#fff" />,
} as const

function ChatHeader() {
  return (
    <div className="absolute inset-x-0 top-0 z-30 bg-white pt-[52px] shadow-[0_4px_8px_rgba(0,0,0,0.04)]">
      <div className="relative flex h-[46px] items-center border-b px-[16px]" style={{ borderColor: kr.line }}>
        <ChevronLeft size={27} strokeWidth={1.7} />
        <div className="absolute left-1/2 top-[2px] -translate-x-1/2 text-center">
          <div className="flex items-center justify-center gap-[5px]">
            <span className="text-[15px] font-bold">{chat.partner}</span>
            <span className="rounded-[4px] px-[4px] text-[9.5px] leading-[15px] font-semibold" style={{ background: kr.tempBg, color: kr.temp }}>
              {chat.temp}
            </span>
          </div>
          <p className="mt-[3px] text-[11px]" style={{ color: kr.sub }}>
            {chat.response}
          </p>
        </div>
        <Phone size={22} strokeWidth={1.6} className="mr-[22px] ml-auto" />
        <EllipsisVertical size={20} strokeWidth={2.2} />
      </div>
      <div className="flex items-center gap-[12px] px-[16px] pt-[12px]">
        <ImagePlaceholder className="h-[40px] w-[40px] rounded-[4px]" label="product" />
        <div className="min-w-0 flex-1 text-[13.5px] leading-[20px]">
          <div className="truncate">
            <b className="mr-[5px] font-bold">{chat.product.status}</b>
            <EmojiGlyph size={16} className="mr-[4px]" />
            {chat.product.title}
          </div>
          <p>
            <b className="font-bold">{chat.product.price}</b> <span style={{ color: kr.sub }}>{chat.product.note}</span>
          </p>
        </div>
      </div>
      <div className="flex gap-[9px] px-[16px] pt-[11px] pb-[10px]">
        {chat.actions.map((a, i) => (
          <span
            key={a.key}
            className="flex h-[36px] items-center justify-center gap-[6px] rounded-[6px] border text-[12.5px] font-semibold"
            style={{ borderColor: '#dcdee3', width: i === 0 ? 157 : 90 }}
          >
            {actionIcons[a.key as keyof typeof actionIcons]}
            {a.label}
          </span>
        ))}
      </div>
    </div>
  )
}

function Composer() {
  return (
    <div className="absolute inset-x-0 top-[769px] flex items-center gap-[10px] pr-[14px] pl-[14px]">
      <Plus size={24} strokeWidth={1.5} className="text-[#555]" />
      <div className="flex h-[37px] flex-1 items-center rounded-full pr-[10px] pl-[12px]" style={{ background: kr.chip }}>
        <span className="flex-1 text-[14px]" style={{ color: kr.faint }}>
          {chat.input}
        </span>
        <Smile size={22} strokeWidth={1.6} className="text-[#555]" />
      </div>
      <SendHorizontal size={22} strokeWidth={1.6} fill={kr.faint} stroke={kr.faint} />
    </div>
  )
}

/** Buyer/seller chat with product header, appointment card and composer. */
export function ChatScreen() {
  return (
    <AppScreen className="font-pretendard" style={{ color: kr.text }}>
      <Chrome />
      <div className="absolute inset-x-0 top-[194px] flex flex-col gap-[14px]">
        {messages.map((m) => (
          <ChatEntry key={m.key} item={m} />
        ))}
      </div>
      <ChatHeader />
      <Composer />
    </AppScreen>
  )
}
