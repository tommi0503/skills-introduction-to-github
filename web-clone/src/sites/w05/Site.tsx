import { PageFrame, cn } from '../../ui'
import { theme } from './theme'
import { Etch } from './components/Etch'
import { Nav } from './sections/Nav'
import { Announcement } from './sections/Announcement'
import { Hero } from './sections/Hero'
import { ProductDemo } from './sections/ProductDemo'
import { Logos } from './sections/Logos'
import { Manifesto } from './sections/Manifesto'
import { DictationFeature } from './sections/DictationFeature'

/** Page-y positions of the engraved horizontal rules (dark-first when true). */
const rules: [number, boolean][] = [
  [111, true],
  [172, false],
  [618, true],
  [1322, false],
  [1523, false],
  [2284, false],
]

/** Page-y spans where the column rules run (the logo marquee is full-bleed). */
const columnSpans: [number, number][] = [
  [16, 1322],
  [1525, 4500],
]

export default function Site() {
  const inset = theme.frameInset
  return (
    <PageFrame background={theme.page} className={cn(theme.mono)} style={{ color: theme.ink }}>
      <div
        className="absolute overflow-hidden rounded-t-[24px]"
        style={{ left: inset, top: inset, right: inset, bottom: 0, background: theme.frame, boxShadow: 'inset 1px 1px 0 #686868, inset -1px 0 0 #535353' }}
      >
        <Nav />
        <Announcement />
        <Hero />
        <ProductDemo />
        <Logos />
        <Manifesto />
        <DictationFeature />
        {rules.map(([y, dark]) => (
          <Etch key={y} darkFirst={dark} style={{ top: y - inset, left: 0, right: 0 }} />
        ))}
        {columnSpans.map(([from, to]) => (
          <div key={from}>
            <Etch orientation="vertical" darkFirst={false} style={{ left: theme.columnLeft - 1 - inset, top: from - inset, height: to - from }} />
            <Etch orientation="vertical" style={{ left: theme.columnRight - 1 - inset, top: from - inset, height: to - from }} />
          </div>
        ))}
      </div>
    </PageFrame>
  )
}
