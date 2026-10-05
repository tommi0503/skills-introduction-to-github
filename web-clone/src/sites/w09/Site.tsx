import { PageFrame } from '../../ui'
import { Cta } from './sections/Cta'
import { Hero } from './sections/Hero'
import { Know } from './sections/Know'
import { Nav } from './sections/Nav'
import { Teams } from './sections/Teams'
import { Think } from './sections/Think'
import { World } from './sections/World'
import { theme } from './theme'

const CTA_TOP = 4177

export function Site() {
  return (
    <PageFrame background={theme.color.canvas} className={theme.font}>
      <div className="absolute left-0 top-0 bg-white" style={{ width: theme.contentWidth, height: CTA_TOP }} />
      <Hero />
      <Nav />
      <World />
      <Think />
      <Know />
      <Teams />
      <Cta top={CTA_TOP} />
    </PageFrame>
  )
}
