import { PageFrame } from '../../ui'
import { Header } from './sections/Header'
import { Hero, LogoStrip } from './sections/Hero'
import { ProductDemo } from './sections/ProductDemo'
import { GetStarted } from './sections/GetStarted'
import { SplitFeature } from './sections/SplitFeature'
import { System } from './sections/System'
import { Testimonial } from './sections/Testimonial'
import { Enterprise } from './sections/Enterprise'
import { Overlays } from './sections/Overlays'
import { splits } from './data'
import { colors } from './theme'

/** Vertical layout: [section, page-y start] pairs keep everything aligned to the reference. */
const layout = {
  logos: 470,
  demo: 560,
  getStarted: 1300,
  split1: 1600,
  split2: 2060,
  system: 2520,
  testimonial: 3420,
  enterprise: 3800,
}

export function GitBookSite() {
  return (
    <PageFrame background={colors.page}>
      <Header />
      <Hero />
      <div className="relative" style={{ height: layout.demo - layout.logos }}>
        <LogoStrip top={layout.logos} />
      </div>
      <ProductDemo top={layout.demo} height={layout.getStarted - layout.demo} />
      <GetStarted height={layout.split1 - layout.getStarted} />
      <SplitFeature data={splits[0]} height={layout.split2 - layout.split1} mediaTop={1676 - layout.split1} textTop={1733 - layout.split1} />
      <SplitFeature data={splits[1]} height={layout.system - layout.split2} mediaTop={2129 - layout.split2} textTop={2196 - layout.split2} />
      <System height={layout.testimonial - layout.system} />
      <Testimonial height={layout.enterprise - layout.testimonial} />
      <Enterprise />
      <Overlays />
    </PageFrame>
  )
}
