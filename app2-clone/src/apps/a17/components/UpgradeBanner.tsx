/** Inline upsell banner shown inside the composer. */
export function UpgradeBanner({ text, action }: { text: string; action: string }) {
  return (
    <div className="flex h-[53px] items-center justify-between rounded-[16px] bg-[#f1f0ec] pr-[11px] pl-[12px]">
      <span className="text-[13px] text-[#3d3d3a]">{text}</span>
      <span className="rounded-full border border-[#dcdbd6] bg-[#f6f5f2] px-[12px] py-[6px] text-[15px] font-semibold text-[#141413]">
        {action}
      </span>
    </div>
  )
}
