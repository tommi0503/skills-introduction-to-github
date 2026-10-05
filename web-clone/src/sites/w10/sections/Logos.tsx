import { ImagePlaceholder } from '../../../ui'
import { Box } from '../components/Box'
import { logos } from '../data'
import { theme } from '../theme'

/** Customer logo marquee (frozen frame). */
export function Logos() {
  return (
    <>
      {logos.map((r) => (
        <Box key={r.x} rect={r}>
          <ImagePlaceholder label="customer logo" tone={theme.color.logo} className="h-full w-full" />
        </Box>
      ))}
    </>
  )
}
