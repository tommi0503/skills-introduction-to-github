import { RoundedBox } from '../../shared-1718/components/RoundedBox'
import type { FestivalPalette } from '../../shared-1718/theme'

export interface ProgramsFrameProps {
  title: string
  palette: FestivalPalette
  x: number
  y: number
  width: number
  height: number
}

/** Outlined card spanning both inner panels, with its heading. */
export function ProgramsFrame({ title, palette, x, y, width, height }: ProgramsFrameProps) {
  return (
    <RoundedBox x={x} y={y} width={width} height={height} radius={14} background={palette.card} borderColor={palette.cardBorder}>
      <p className="absolute m-0 text-[22px] font-bold" style={{ left: 38, top: 40, color: palette.accent }}>
        {title}
      </p>
    </RoundedBox>
  )
}
