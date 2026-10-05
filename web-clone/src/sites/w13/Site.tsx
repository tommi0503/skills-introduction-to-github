import { PageFrame } from '../../ui'
import { theme } from './theme'
import { Banner } from './sections/Banner'
import { Nav } from './sections/Nav'
import { Hero } from './sections/Hero'
import { Logos } from './sections/Logos'
import { Gallery } from './sections/Gallery'
import { Feature } from './sections/Feature'

/** Sections are absolutely placed on the 1440×4500 frame using reference coordinates. */
export function Site() {
  return (
    <PageFrame background={theme.colors.page} className="font-geist">
      <Hero />
      <Banner />
      <Nav />
      <Logos />
      <Gallery />
      <Feature />
    </PageFrame>
  )
}
