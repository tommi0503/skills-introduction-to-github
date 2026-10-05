import { ImagePlaceholder, cn } from '../../../ui'
import { Column } from '../components/Column'
import { TwoTone } from '../components/TwoTone'
import { industries } from '../data'
import { theme } from '../theme'

export function Industries() {
  return (
    <Column height={664}>
      <div className="absolute left-[48px] right-[48px] top-[20px] flex items-center justify-between">
        <TwoTone muted={industries.muted} strong={industries.strong} />
        <div className="flex gap-[40px] pr-[-12px]">
          {industries.tabs.map((t, i) => (
            <span
              key={t}
              className={cn('text-[14px] leading-[16.8px] font-medium tracking-[0.14px]')}
              style={{ color: i === industries.active ? theme.ink : theme.faded }}
            >
              {t}
            </span>
          ))}
        </div>
      </div>
      <div className="absolute left-[16px] right-[16px] top-[73px] h-[576px]" style={{ background: theme.panel }}>
        <p className="absolute left-[32px] top-[32px] text-[20px] leading-[26px] font-medium" style={{ color: theme.ink }}>
          {industries.panel.title}
        </p>
        <p className="absolute left-[32px] top-[90px] w-[360px] text-[16px] leading-5 tracking-[-0.2px]" style={{ color: theme.ink }}>
          {industries.panel.body}
        </p>
        <ImagePlaceholder label="industry illustration" className="absolute left-[502px] top-[66px] h-[443px] w-[712px] rounded-[24px]" />
      </div>
    </Column>
  )
}
