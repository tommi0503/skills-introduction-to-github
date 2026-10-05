import { ImagePlaceholder } from '../../../ui'
import { Prose } from '../components/Prose'
import { memory } from '../data'
import { theme } from '../theme'

export function Memory() {
  return (
    <section className="absolute inset-x-0 top-[3408px] h-[648px] overflow-hidden">
      <div className="absolute inset-y-0" style={{ left: theme.column.left + 1, width: theme.column.width - 2, background: 'linear-gradient(#ffffff 22%, #fafafa)' }} />
      <h3 className={`${theme.fonts.display} absolute left-[361px] top-[64px] text-[30px] leading-10 font-medium`} style={{ color: theme.ink }}>
        <span style={{ color: theme.faint }}>{memory.title.faint}</span> {memory.title.rest}
      </h3>
      <Prose className="absolute left-[361px] top-[116px] w-[718px] text-[18px] leading-7" rest={memory.body} more={memory.more} />
      <div className="absolute left-[272px] top-[280px] w-[320px] rounded-[16.8px] px-[16px] py-[10px] text-[16px] leading-6 font-medium" style={{ background: '#f5f5f5', color: theme.ink }}>
        {memory.prompt}
      </div>
      <ImagePlaceholder label="history panel screenshot" className="absolute left-[625px] top-[305px] h-[383px] w-[430px] rounded-[16px]" />
      <ImagePlaceholder label="agent steps screenshot" tone="#eef0f2" className="absolute left-[737px] top-[265px] h-[383px] w-[430px] rounded-[16px]" />
    </section>
  )
}
