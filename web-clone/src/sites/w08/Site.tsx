import { PageFrame, cn } from '../../ui'
import { ChatLauncher } from './sections/ChatLauncher'
import { FeatureShowcase } from './sections/FeatureShowcase'
import { Hero } from './sections/Hero'
import { Management } from './sections/Management'
import { Nav } from './sections/Nav'
import { theme } from './theme'

export function Site() {
  return (
    <PageFrame background={theme.page} className={cn(theme.body)}>
      {/* Rounded hero panel; its lower part is an empty sticky-scroll area in the capture. */}
      <div className="absolute" style={{ left: 24, top: 108, width: 1392, height: 3642, borderRadius: 40, background: theme.panel }} />
      {/* Soft tint behind the meeting-management section. */}
      <div className="absolute" style={{ left: 24, top: 3830, width: 1392, height: 700, borderRadius: 40, background: theme.panel, opacity: 0.6 }} />
      <Nav />
      <Hero />
      <FeatureShowcase />
      <ChatLauncher />
      <Management />
    </PageFrame>
  )
}
