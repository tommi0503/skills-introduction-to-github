import { Check } from 'lucide-react'

/** "Everything in Free, plus:" check list. */
export function IncludesList({ title, items, footnote }: { title: string; items: string[]; footnote: string }) {
  return (
    <div>
      <p className="text-[13px] font-medium text-[#262624]">{title}</p>
      <ul className="mt-[7px] flex flex-col gap-[11px]">
        {items.map((t) => (
          <li key={t} className="flex items-center gap-[11px] text-[12.6px] leading-[18px] text-[#3d3d3a]">
            <Check size={19} strokeWidth={1.5} className="ml-[1px] shrink-0 text-[#55544f]" />
            <span className="w-[240px]">{t}</span>
          </li>
        ))}
      </ul>
      <p className="mt-[12px] text-[13px] text-[#8d8c87] underline underline-offset-2">{footnote}</p>
    </div>
  )
}
