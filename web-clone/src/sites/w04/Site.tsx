import { FRAME, PageFrame } from '../../ui'
import { theme } from './theme'
import { DashedLine } from './components/Dashed'
import { NavBar } from './sections/NavBar'
import { Hero } from './sections/Hero'
import { Region } from './sections/Region'
import { Customers } from './sections/Customers'
import { WhyChoose } from './sections/WhyChoose'
import { Pricing } from './sections/Pricing'

/** Page-level dashed guide rails framing the content column. */
function Rails() {
  return (
    <>
      <DashedLine style={{ left: 0, right: 0, top: 72 }} />
      <DashedLine style={{ left: 0, right: 0, top: 848 }} />
      <DashedLine vertical style={{ left: theme.rail.left, top: 864, height: FRAME.height }} />
      <DashedLine vertical style={{ left: theme.rail.right, top: 864, height: FRAME.height }} />
    </>
  )
}

export function Site() {
  return (
    <PageFrame background={theme.color.page} style={{ fontFamily: theme.font.sans }}>
      <Rails />
      <div className="relative">
        <NavBar />
        <Hero />
        <Region />
        <Customers />
        <WhyChoose />
        <Pricing />
      </div>
    </PageFrame>
  )
}
