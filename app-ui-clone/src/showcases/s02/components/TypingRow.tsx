import { AiOrb } from './AiOrb'

/** "AI is planning your trip •••" status line. */
export function TypingRow({ label }: { label: string }) {
  return (
    <div className="flex items-center gap-[7px]">
      <AiOrb size={29} />
      <span className="text-[13.7px] text-[#8e8e8e]">{label}</span>
      <span className="ml-[3px] flex items-center gap-[3px]">
        {[1, 0.75, 0.5, 0.3].map((o) => (
          <span key={o} className="h-[3.5px] w-[3.5px] rounded-full bg-[#555]" style={{ opacity: o }} />
        ))}
      </span>
    </div>
  )
}
