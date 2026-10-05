import { PageFrame } from '../../ui'
import './fonts.css'
import { theme } from './theme'
import { Hero } from './sections/Hero'
import { ChatWidget } from './sections/ChatWidget'
import { Think } from './sections/Think'
import { Logos } from './sections/Logos'
import { Track } from './sections/Track'
import { Features } from './sections/Features'
import { Advice } from './sections/Advice'
import { Analyze } from './sections/Analyze'

export function Site() {
  return (
    <PageFrame background={theme.colors.page} className="font-inter text-white">
      <Hero />
      <Think />
      <Logos />
      <Track />
      <Features />
      <Advice />
      <Analyze />
      <ChatWidget />
    </PageFrame>
  )
}
