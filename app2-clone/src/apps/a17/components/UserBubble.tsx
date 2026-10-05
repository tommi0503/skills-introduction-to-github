/** Right-aligned user message bubble. */
export function UserBubble({ text }: { text: string }) {
  return (
    <div className="flex justify-end">
      <p className="rounded-[22px] bg-[#efeeeb] px-[12px] py-[12px] text-[16.3px] leading-[23px] text-[#141413]">{text}</p>
    </div>
  )
}
