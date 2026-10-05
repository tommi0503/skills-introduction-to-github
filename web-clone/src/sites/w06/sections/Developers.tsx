import { ImagePlaceholder, cn } from '../../../ui'
import { developers, pythonSample } from '../data'
import { theme } from '../theme'
import { PillButton } from '../components/PillButton'
import { CodeWindow } from '../components/CodeWindow'

export function Developers() {
  return (
    <section className="relative mx-auto mt-[192px] h-[470px]" style={{ width: theme.content, color: theme.ink }}>
      <div className="absolute left-0" style={{ top: 64, width: 568 }}>
        <p className="text-[14px] font-[450] leading-5" style={{ color: theme.muted }}>
          {developers.eyebrow}
        </p>
        <h2 className="mt-[16px] text-[48px] font-[450] leading-[48px] tracking-[-0.48px]">
          {developers.title[0]}
          <br />
          {developers.title[1]}
        </h2>
        <p className="mt-[16px] w-[448px] text-[16px] leading-[26px]">{developers.body}</p>
        <div className="mt-[32px] flex gap-3">
          <PillButton variant="dark" className="w-[114px]">
            {developers.primary}
          </PillButton>
          <PillButton variant="soft" className="w-[107px]">
            {developers.secondary}
          </PillButton>
        </div>
        <dl className="mt-[32px] flex gap-[24px]">
          {developers.stats.map((s) => (
            <div key={s.label}>
              <dt className="text-[14px] font-[450] leading-5">{s.value}</dt>
              <dd className="mt-[2px] text-[12px] leading-4" style={{ color: theme.faint }}>
                {s.label}
              </dd>
            </div>
          ))}
        </dl>
      </div>
      <div className="absolute" style={{ left: 664, top: 0, width: 568 }}>
        <ImagePlaceholder label="gradient artwork" className="h-[417px] w-[568px]" />
        <CodeWindow lines={pythonSample} className="absolute left-[48px] top-[48px] h-[321px] w-[472px]" />
        <div className="mt-[20px] flex gap-[4px]">
          {developers.tabs.map((t, i) => (
            <span
              key={t}
              className={cn('flex h-8 items-center rounded-full px-[12px] text-[14px] font-[450]')}
              style={i === 0 ? { background: '#f1f1f1', color: theme.ink } : { color: 'rgb(125,129,135)' }}
            >
              {t}
            </span>
          ))}
        </div>
      </div>
    </section>
  )
}
