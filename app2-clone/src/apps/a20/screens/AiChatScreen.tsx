import { ArrowUp, CircleEllipsis, CornerDownRight, PenLine, Sparkle, SquarePen, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { GnStatusBar } from '../components/GnStatusBar'
import { Grabber } from '../components/Grabber'
import { IconCircle } from '../components/IconCircle'
import { Chip } from '../components/Chip'
import { FeedbackIcons } from '../components/FeedbackIcons'
import { aiChat } from '../data'
import { gn } from '../theme'

export function AiChatScreen() {
  const c = aiChat
  return (
    <AppScreen background="#263b5c" className="font-dm">
      <GnStatusBar color="#fff" chipClassName="[&>span]:!bg-[#64676d]" />
      {/* the other editor tab peeking behind the sheet */}
      <div className="absolute left-[222px] top-[59px] h-[40px] w-[170px] rounded-tl-[8px] bg-[#cfcfcf]" />

      <section className="absolute inset-x-0 top-[66px] bottom-0 overflow-hidden rounded-t-[30px] bg-white">
        {/* user bubble, scrolled under the header */}
        <div className="absolute left-[77px] right-[14px] top-[44px] h-[54px] rounded-b-[12px] bg-[#e8f4fb] pl-[19px] pt-[19px] text-[16.5px] text-[#222]">
          {c.prompt}
        </div>
        <div className="absolute inset-x-0 top-0 h-[59px] bg-white">
          <Grabber className="absolute left-1/2 top-[7px] -translate-x-1/2" />
          <CircleEllipsis size={23} strokeWidth={1.5} className="absolute left-[23px] top-[24px] text-[#444]" />
          <IconCircle icon={X} size={30} iconSize={16} strokeWidth={1.6} className="absolute left-[340px] top-[20px] bg-[#ececec] text-[#666]" />
        </div>

        {/* answer card */}
        <div className="absolute left-[12px] top-[111px] h-[410px] w-[336px] rounded-[12px] border border-[#e8e8e8]">
          <p className="absolute left-[20px] right-[18px] top-[16px] text-[16.5px] leading-[21.5px] text-[#222]">{c.answer}</p>
          <div className="absolute inset-x-0 top-[181px] border-t border-[#efefef]" />
          <ImagePlaceholder className="absolute left-[107px] top-[202px] h-[136px] w-[128px] rounded-[8px]" label="mind map image" />
          <Chip className="absolute left-[232px] top-[321px] h-[31px] bg-[#2f73d0] px-[13px] text-[15px] font-medium text-white">
            <SquarePen size={16} strokeWidth={1.8} />
            {c.review}
          </Chip>
          <div className="absolute inset-x-0 top-[361px] border-t border-[#efefef]" />
          <FeedbackIcons share className="absolute left-[25px] top-[378px]" gap={26} size={16} />
          <span className="absolute left-[264px] top-[379px] rounded-[4px] bg-[#efefef] px-[4px] py-[2px] text-[9px] font-semibold text-[#444]">
            {c.badge}
          </span>
        </div>

        {/* actions */}
        <div className="absolute left-[12px] top-[535px] flex gap-[9px]">
          <Chip className="h-[30px] bg-[#efefef] pl-[10px] pr-[13px] text-[15px] font-medium text-[#222]">
            <CornerDownRight size={15} strokeWidth={2} className="text-[#3e72c8]" />
            {c.insert}
          </Chip>
          <Chip className="h-[30px] bg-[#efefef] pl-[13px] pr-[14px] text-[15px] font-medium" >
            <X size={15} strokeWidth={1.8} style={{ color: gn.red }} />
            <span style={{ color: gn.red }}>{c.discard}</span>
          </Chip>
        </div>

        {/* composer */}
        <div className="absolute left-[12px] right-[12px] top-[591px] h-[114px] rounded-[14px] border border-[#e3e3e3]">
          <span className="absolute left-[15px] top-[16px] text-[16px] text-[#9a9a9a]">{c.placeholder}</span>
          <IconCircle icon={Sparkle} size={24} iconSize={14} strokeWidth={1.8} className="absolute left-[15px] top-[77px] bg-[#e3f2fb] text-[#3e7fd0]" />
          <Chip className="absolute left-[47px] top-[75px] h-[29px] border border-[#5aa9de] bg-[#dff2fb] pl-[10px] pr-[9px] text-[15px] font-medium text-[#2f73b8]">
            <PenLine size={14} strokeWidth={1.8} />
            {c.create}
            <X size={13} strokeWidth={1.8} className="ml-[3px]" />
          </Chip>
          <IconCircle icon={ArrowUp} size={26} iconSize={13} strokeWidth={1.8} className="absolute left-[323px] top-[77px] bg-[#efefef] text-[#c4c4c4]" />
        </div>
        <div className="absolute inset-x-0 top-[716px] text-center text-[12.5px] text-[#9a9a9a]">{c.disclaimer}</div>
      </section>
    </AppScreen>
  )
}
