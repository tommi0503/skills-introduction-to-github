import { ChevronRight } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { news } from '../data'
import { theme } from '../theme'

export function News() {
  return (
    <section className="mx-auto mt-[120px]" style={{ width: theme.content, color: theme.ink }}>
      <div className="flex items-end justify-between">
        <h2 className="text-[30px] font-[450] leading-9 tracking-[-0.3px]">{news.title}</h2>
        <span className="flex items-center gap-[6px] pb-[0px] text-[14px] font-[450] leading-5">
          {news.all}
          <ChevronRight size={14} strokeWidth={2} />
        </span>
      </div>
      <div className="mt-[41px] grid grid-cols-4 gap-[20px]">
        {news.items.map((n) => (
          <article key={n.title}>
            <ImagePlaceholder label={n.title} className="h-[153px] w-[293px] rounded-[8px]" />
            <div className="mt-[17px] flex items-center gap-[8px] text-[12px] leading-4">
              {n.category && (
                <>
                  <span className="font-[450]">{n.category}</span>
                  <span className="text-black/25">·</span>
                </>
              )}
              <time>{n.date}</time>
            </div>
            <h3 className="mt-[8px] pr-[24px] text-[16px] font-[450] leading-[22px] tracking-[-0.16px]">
              {n.title}
              <ChevronRight size={14} strokeWidth={2} className="ml-[6px] inline-block align-[-1px] text-black/60" />
            </h3>
          </article>
        ))}
      </div>
    </section>
  )
}
