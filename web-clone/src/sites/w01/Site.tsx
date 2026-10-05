import { PageFrame } from '../../ui'
import { Ruler } from './components/Ruler'
import { CookieBanner } from './sections/CookieBanner'
import { Customers } from './sections/Customers'
import { Deploy } from './sections/Deploy'
import { GetStarted } from './sections/GetStarted'
import { Hero } from './sections/Hero'
import { Industries } from './sections/Industries'
import { Nav } from './sections/Nav'
import { Research } from './sections/Research'
import { Stack } from './sections/Stack'
import { theme } from './theme'

const sections = [Hero, Industries, Customers, Stack, Research, Deploy, GetStarted]

export function Site() {
  const { left, width } = theme.column
  return (
    <PageFrame background={theme.page} className={`${theme.fonts.sans} antialiased`}>
      <Nav />
      {sections.map((S, i) => (
        <div key={i}>
          <S />
          {i > 0 && <Ruler />}
        </div>
      ))}
      {/* Page-long vertical rules framing the content column. */}
      <div className="pointer-events-none absolute inset-y-0" style={{ left, width, borderLeft: `1px solid ${theme.rule}`, borderRight: `1px solid ${theme.rule}` }} />
      <CookieBanner />
    </PageFrame>
  )
}
