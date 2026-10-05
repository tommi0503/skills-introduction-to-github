import type { ChatOption } from '../data'

/** White lettered answer list inside a question bubble. */
export function OptionList({ options }: { options: ChatOption[] }) {
  return (
    <div className="overflow-hidden rounded-[10px] bg-white">
      {options.map((o, i) => (
        <div key={o.key} className="flex h-[40.6px] items-center gap-[9px] pl-[9px]" style={{ borderTop: i ? '1px solid #efefef' : undefined }}>
          <span className="flex h-[22px] w-[22px] items-center justify-center rounded-[5px] bg-[#f4f4f4] text-[11px] text-[#c4c4c4]">{o.key}</span>
          <span className="text-[16px] text-[#111]">{o.label}</span>
        </div>
      ))}
    </div>
  )
}
