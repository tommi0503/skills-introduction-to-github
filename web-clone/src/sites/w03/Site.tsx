import { PageFrame } from '../../ui'
import { theme } from './theme'
import { AnnouncementBar } from './sections/AnnouncementBar'
import { NavBar } from './sections/NavBar'
import { Hero } from './sections/Hero'
import { LogoCloud } from './sections/LogoCloud'
import { Platform } from './sections/Platform'
import { Launch } from './sections/Launch'
import { Innovation } from './sections/Innovation'

export function Site() {
  return (
    <PageFrame background={theme.color.page} style={{ fontFamily: theme.font.sans }}>
      <AnnouncementBar />
      <NavBar />
      <Hero />
      <LogoCloud />
      <Platform />
      <Launch />
      <Innovation />
    </PageFrame>
  )
}
