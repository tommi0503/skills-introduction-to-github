import { PageFrame } from '../../ui'
import { DashedRule } from './components/DashedRule'
import { Benchmark } from './sections/Benchmark'
import { Capability } from './sections/Capability'
import { Hero } from './sections/Hero'
import { Intro } from './sections/Intro'
import { Memory } from './sections/Memory'
import { Passwords } from './sections/Passwords'
import { theme } from './theme'

/** Full-width hairlines between major sections (page y). */
const SOLID_RULES = [1411, 4056]
const DASHED_RULES = [2712, 3407]

export function Site() {
  const { left, width } = theme.column
  return (
    <PageFrame background={theme.page} className={`${theme.fonts.body} antialiased`}>
      <div className="absolute bottom-0 top-[1000px]" style={{ left, width, borderLeft: `1px solid ${theme.rule}`, borderRight: `1px solid ${theme.rule}` }} />
      {SOLID_RULES.map((y) => <div key={y} className="absolute inset-x-0 h-px" style={{ top: y, background: theme.rule }} />)}
      <Intro />
      <Capability />
      <Benchmark />
      <Memory />
      <Passwords />
      {DASHED_RULES.map((y) => <DashedRule key={y} top={y} />)}
      <Hero />
    </PageFrame>
  )
}
