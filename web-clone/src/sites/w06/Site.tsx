import { PageFrame, cn } from '../../ui'
import { theme } from './theme'
import { Nav } from './sections/Nav'
import { Hero } from './sections/Hero'
import { ProductGrid } from './sections/ProductGrid'
import { Developers } from './sections/Developers'
import { Stats } from './sections/Stats'
import { News } from './sections/News'
import { GetStarted } from './sections/GetStarted'
import { Footer } from './sections/Footer'
import { CookieBanner } from './sections/CookieBanner'

export default function Site() {
  return (
    <PageFrame background={theme.page} className={cn(theme.font)} style={{ color: theme.ink }}>
      <Nav />
      <Hero />
      <ProductGrid />
      <Developers />
      <Stats />
      <News />
      <GetStarted />
      <Footer />
      <CookieBanner />
    </PageFrame>
  )
}
