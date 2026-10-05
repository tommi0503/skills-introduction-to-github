import { ImagePlaceholder } from '../../../ui'
import { Button } from '../components/Button'
import { Column } from '../components/Column'
import { research } from '../data'
import { serifStyle, theme } from '../theme'

export function Research() {
  return (
    <Column height={307} background={theme.panel} className="flex gap-[48px] px-[48px] pt-[54px]">
      <div className={`${theme.fonts.serif} w-[567px]`} style={serifStyle(26)}>
        <p style={{ color: theme.ink }}>{research.title}</p>
        <p className="mt-[16px]" style={{ color: theme.faded }}>{research.subtitle}</p>
      </div>
      <div className="relative w-[567px] pt-[2px]">
        <p className="text-[16px] leading-5" style={{ color: theme.muted }}>{research.body}</p>
        <Button variant="outline" className="mt-[32px]">{research.cta}</Button>
        <ImagePlaceholder label="research mark" className="absolute right-0 top-[90px] h-[108px] w-[79px]" />
      </div>
    </Column>
  )
}
