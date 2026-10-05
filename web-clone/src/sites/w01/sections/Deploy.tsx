import { ChevronDown, ChevronUp } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { Column } from '../components/Column'
import { TwoTone } from '../components/TwoTone'
import { deploy } from '../data'
import { theme } from '../theme'

export function Deploy() {
  return (
    <Column height={586}>
      <ImagePlaceholder label="deployment illustration" className="absolute left-[200px] top-[89px] h-[356px] w-[317px]" />
      <div className="absolute left-[716px] top-[55px] w-[514px]">
        <TwoTone muted={deploy.muted} strong={deploy.strong} stacked />
        <p className="mt-[24px] w-[506px] text-[16px] leading-5" style={{ color: theme.muted }}>{deploy.body}</p>
        <div className="mt-[64px]">
          {deploy.options.map((o, i) => {
            const Icon = o.icon
            const Chevron = o.open ? ChevronUp : ChevronDown
            const color = o.open ? theme.ink : theme.muted
            return (
              <div
                key={o.label}
                style={{ borderTop: i ? `1px solid ${theme.rule}` : undefined }}
                className={i ? 'pt-[25px] pb-[25px]' : 'pb-[25px]'}
              >
                <div className="flex h-6 items-center text-[16px] leading-6 font-medium" style={{ color }}>
                  <Icon className="ml-px size-[22px]" fill="currentColor" strokeWidth={1.5} />
                  <span className="ml-[17px]">{o.label}</span>
                  <Chevron className="ml-auto mr-px size-4" style={{ color: theme.muted }} />
                </div>
                {o.body && (
                  <p className="mt-[25px] text-[14px] leading-[17.5px]" style={{ color: theme.muted }}>{o.body}</p>
                )}
              </div>
            )
          })}
        </div>
      </div>
    </Column>
  )
}
