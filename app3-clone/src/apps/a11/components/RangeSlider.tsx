/** Track + filled part + large black knob with white ring. */
export function RangeSlider({ value, width, className }: { value: number; width: number; className?: string }) {
  const knob = value * width
  return (
    <div className={className}>
      <div className="relative h-[10px] rounded-full bg-[#e9e9ee]" style={{ width }}>
        <div className="absolute inset-y-0 left-0 rounded-full bg-black" style={{ width: knob }} />
        <div
          className="absolute top-1/2 h-[60px] w-[60px] -translate-x-1/2 -translate-y-1/2 rounded-full border-[8.5px] border-white bg-black"
          style={{ left: knob, boxShadow: '0 2px 10px rgba(0,0,0,0.12)' }}
        />
      </div>
    </div>
  )
}
