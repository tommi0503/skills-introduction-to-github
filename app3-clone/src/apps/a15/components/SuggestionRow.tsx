import { ImagePlaceholder } from '../../../ui'
import type { Suggestion } from '../data'
import { palette as c } from '../theme'

export function SuggestionRow({ item }: { item: Suggestion }) {
  const Icon = item.icon
  return (
    <div className="flex items-center gap-[16px]">
      {Icon ? (
        <div className="flex h-[55px] w-[55px] shrink-0 items-center justify-center rounded-[11px] bg-[#edf2fa]">
          <Icon size={22} strokeWidth={1.6} color="#4c74b8" className="-rotate-[0deg]" />
        </div>
      ) : (
        <ImagePlaceholder className="rounded-[11px]" style={{ width: 55, height: 55 }} label={`${item.title} illustration`} />
      )}
      <div>
        <div className="text-[13.5px] leading-[18px] font-semibold" style={{ color: c.text }}>
          {item.title}
        </div>
        {item.lines.map((l) => (
          <div key={l} className="mt-[1px] text-[13px] leading-[19px]" style={{ color: c.faint }}>
            {l}
          </div>
        ))}
      </div>
    </div>
  )
}
