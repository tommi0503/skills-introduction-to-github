import './fonts.css'
import { PageFrame } from '../../ui'
import { Agents } from './sections/Agents'
import { Header } from './sections/Header'
import { Hero } from './sections/Hero'
import { Industries } from './sections/Industries'
import { Logos } from './sections/Logos'
import { theme } from './theme'

export function Site() {
  return (
    <PageFrame background={theme.color.page} className={`text-white ${theme.font.sans}`}>
      <Hero />
      <Header />
      <Logos />
      <Industries />
      <Agents />
    </PageFrame>
  )
}
