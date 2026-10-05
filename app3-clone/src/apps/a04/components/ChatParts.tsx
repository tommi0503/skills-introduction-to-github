import { ImagePlaceholder, cn } from '../../../ui'
import type { ChatItem } from '../data'
import { kr } from '../theme'

function Time({ children, className }: { children: string; className?: string }) {
  return (
    <span className={cn('shrink-0 text-[10.5px] leading-none', className)} style={{ color: kr.faint }}>
      {children}
    </span>
  )
}

const avatarSlot = <span className="w-[31px] shrink-0" />
const avatar = <ImagePlaceholder className="h-[31px] w-[31px] shrink-0 rounded-full" label="partner avatar" />

/** Renders one chat timeline entry (bubbles, notices, appointment card, sticker). */
export function ChatEntry({ item }: { item: ChatItem }) {
  switch (item.kind) {
    case 'in':
      return (
        <div className="flex items-start gap-[10px] px-[16px]">
          {item.avatar ? avatar : avatarSlot}
          <div className="flex items-end gap-[5px]">
            <span className="rounded-[18px] px-[11px] py-[9px] text-[15px] leading-[18px]" style={{ background: kr.chip }}>
              {item.text}
            </span>
            <Time className="mb-[3px]">{item.time}</Time>
          </div>
        </div>
      )
    case 'out':
      return (
        <div className="flex items-end justify-end gap-[5px] px-[16px]">
          <Time className="mb-[3px]">{item.time}</Time>
          <span className="rounded-[18px] px-[13px] py-[9px] text-[15px] leading-[18px] text-white" style={{ background: kr.orange }}>
            {item.text}
          </span>
        </div>
      )
    case 'notice':
      return (
        <div className="mx-[16px] rounded-[8px] px-[15px] py-[10px] text-[14px] leading-[22px]" style={{ background: kr.noticeBg, color: kr.noticeText }}>
          <b className="mr-[7px] font-bold">{item.label}</b>
          {item.text} <span className="underline">{item.link}</span>
        </div>
      )
    case 'appointment':
      return (
        <div className="flex items-start gap-[10px] px-[16px]">
          {avatar}
          <div className="flex items-end gap-[5px]">
            <div className="w-[236px] rounded-[14px] border bg-white px-[13px] pt-[13px] pb-[13px]" style={{ borderColor: kr.line }}>
              <p className="text-[15.5px] leading-[22px] font-bold">{item.title}</p>
              {item.lines.map((l) => (
                <p key={l} className="text-[15.5px] leading-[22px]">
                  {l}
                </p>
              ))}
              <span className="mt-[12px] flex h-[36px] items-center justify-center rounded-[6px] text-[13px] font-semibold" style={{ background: kr.chip }}>
                {item.action}
              </span>
            </div>
            <Time className="mb-[3px]">{item.time}</Time>
          </div>
        </div>
      )
    case 'system':
      return (
        <p className="text-center text-[12px]" style={{ color: kr.sub }}>
          {item.text} <span className="underline">{item.link}</span>
        </p>
      )
    case 'sticker':
      return (
        <div className="flex items-end justify-end gap-[30px] pr-[44px]">
          <div className="mb-[-8px] flex flex-col items-end gap-[6px]">
            <Time>{item.status}</Time>
            <Time>{item.time}</Time>
          </div>
          <ImagePlaceholder className="mt-[24px] h-[102px] w-[86px] rounded-[10px]" label="sticker" />
        </div>
      )
  }
}
