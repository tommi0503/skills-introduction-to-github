import { Ship } from 'lucide-react'
import { Panel, Placed } from '../../../ui'
import { TextLines } from '../../shared-0407/components/TextLines'
import { brand, content } from '../data'
import { theme } from '../theme'

const X = 42

/** Front cover: brand lockup over the photo, big title, rule and tagline. */
export function CoverPanel() {
  return (
    <Panel style={{ color: theme.ink }}>
      <Placed x={207} y={42} className="z-10 flex items-center gap-[6px]">
        <Ship size={48} strokeWidth={2.4} />
        <TextLines className="font-noto-sans text-[20px] font-semibold" lines={brand} lineClassName="leading-[29px]" />
      </Placed>
      <TextLines
        className="absolute font-noto-sans text-[68px] font-normal"
        style={{ left: X, top: 625 }}
        lines={[...content.title, content.subtitle]}
        lineClassName="leading-[87px] tracking-[0.01em]"
      />
      <div className="absolute right-0" style={{ left: X, top: 905, height: 2, background: theme.muted }} />
      <Placed x={X} y={936} className="whitespace-nowrap font-noto-sans text-[21px] leading-[30px]" style={{ color: theme.muted }}>
        {content.tagline}
      </Placed>
    </Panel>
  )
}
