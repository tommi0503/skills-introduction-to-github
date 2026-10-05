import { ImagePlaceholder } from '../../../ui'
import { chat } from '../data'

/** Fixed support widget pinned to the bottom-right of the first viewport. */
export function ChatWidget() {
  return (
    <div className="absolute left-[976px] top-[820px] z-30 h-[70px] w-[454px] rounded-[35px] bg-white font-inter text-black">
      <div className="absolute left-[37px] top-[12px] text-[15px] leading-[20px] font-bold">{chat.title}</div>
      <div className="absolute left-[37px] top-[39px] text-[15px] leading-[20px] font-semibold tracking-[0.45px] text-[#555]">{chat.body}</div>
      <div className="absolute left-[396px] top-[12px] flex h-[48px] w-[48px] items-center justify-center rounded-full bg-black">
        <ImagePlaceholder label="Origin logo" className="h-[26px] w-[26px] rounded-[8px]" />
      </div>
    </div>
  )
}
