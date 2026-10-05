import { PageFrame, cn } from '../../ui'
import { Header } from './sections/Header'
import { Hero } from './sections/Hero'
import { Library } from './sections/Library'
import { Mcp } from './sections/Mcp'
import { ProductPreview } from './sections/ProductPreview'
import { Showcase } from './sections/Showcase'
import { Story } from './sections/Story'
import { Trusted } from './sections/Trusted'
import { theme } from './theme'

export function Site() {
  return (
    <PageFrame background={theme.white} className={cn(theme.font)}>
      <Header />
      <Hero />
      <ProductPreview />
      <Trusted />
      <Story />
      <Showcase />
      <Library />
      <Mcp />
    </PageFrame>
  )
}
