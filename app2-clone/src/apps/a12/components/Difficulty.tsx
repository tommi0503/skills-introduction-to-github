/** Three ascending bars (first filled) + "Difficulty". */
export function Difficulty({ level = 1 }: { level?: number }) {
  return (
    <div className="flex items-center gap-[4px] text-[13px] font-semibold text-white">
      <span className="flex items-end gap-[1.5px]">
        {[5, 8, 11].map((h, i) => (
          <span key={h} className="w-[2.5px] rounded-[1px]" style={{ height: h, background: i < level ? '#fff' : 'rgba(255,255,255,0.4)' }} />
        ))}
      </span>
      Difficulty
    </div>
  )
}
