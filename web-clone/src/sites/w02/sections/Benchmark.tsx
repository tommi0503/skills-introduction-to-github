import { ImagePlaceholder, cn } from '../../../ui'
import { Prose } from '../components/Prose'
import { benchmark } from '../data'
import { theme } from '../theme'

const TRACK = 610

export function Benchmark() {
  const { min, max } = benchmark.scale
  return (
    <section className="absolute inset-x-0 top-[2713px] h-[694px]">
      <h3 className={`${theme.fonts.display} absolute left-[361px] top-[64px] text-[30px] leading-10 font-medium`} style={{ color: theme.ink }}>
        {benchmark.title.before} <span style={{ color: theme.faint }}>{benchmark.title.faint}</span> {benchmark.title.after}
      </h3>
      <Prose className="absolute left-[361px] top-[116px] w-[718px] text-[18px] leading-7" rest={benchmark.body} more={benchmark.more} />
      <div className="absolute left-[241px] top-[236px] w-[958px]">
        {benchmark.rows.map((r) => (
          <div key={r.name} className="relative flex h-[56px] items-center" style={{ borderTop: `1px solid ${theme.rule}` }}>
            <ImagePlaceholder label={`${r.name} logo`} className="size-[28px] rounded-full" />
            <span className="ml-[8px] text-[16px] leading-6 font-medium" style={{ color: theme.ink }}>{r.name}</span>
            <div
              className="absolute left-[216px] h-[24px]"
              style={{ width: Math.round(((r.score - min) / (max - min)) * TRACK), background: r.highlight ? theme.barActive : theme.barIdle }}
            />
            <span className="ml-auto text-[16px] leading-6 font-medium" style={{ color: theme.ink }}>{r.score.toFixed(1)}%</span>
          </div>
        ))}
        <div style={{ borderTop: `1px solid ${theme.rule}` }} />
      </div>
      <div className="absolute left-[549px] top-[558px] flex h-[40px] items-center rounded-[14px] bg-[#f2f2f2] px-[4px]">
        {benchmark.tabs.map((t, i) => (
          <span
            key={t}
            className={cn('flex h-[32px] items-center rounded-[11.2px] px-[13px] text-[14px] leading-5 font-medium', i === benchmark.activeTab && 'bg-white shadow-[0_1px_2px_rgba(0,0,0,0.12)]')}
            style={{ color: i === benchmark.activeTab ? theme.ink : 'rgba(10,10,10,0.6)' }}
          >
            {t}
          </span>
        ))}
      </div>
    </section>
  )
}
