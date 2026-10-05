/** Small dark hang-tag with a price range. */
export function PriceTag({ label, rotate = 14 }: { label: string; rotate?: number }) {
  return (
    <div
      className="relative flex h-[24px] items-center rounded-[4px] bg-[#1b1b1b] pr-[8px] pl-[18px] text-[9.5px] whitespace-nowrap text-white"
      style={{ transform: `rotate(${rotate}deg)`, transformOrigin: 'left center' }}
    >
      <span className="absolute top-1/2 left-[6px] h-[6px] w-[6px] -translate-y-1/2 rounded-full bg-[#e3a93a]" />
      {label}
    </div>
  )
}
