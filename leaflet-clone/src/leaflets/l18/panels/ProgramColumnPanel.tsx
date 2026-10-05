import { Panel, Placed } from '../../../ui'
import type { FestivalPalette } from '../../shared-1718/theme'
import { ProgramBlock } from '../components/ProgramBlock'
import type { ProgramDetail } from '../data'

export interface ProgramColumnPanelProps {
  programs: ProgramDetail[]
  palette: FestivalPalette
  /** Left edge of the column inside the panel. */
  x: number
  width: number
  /** Top of each programme block (panel px). */
  tops: number[]
}

/** One inner panel's column of programme descriptions (sits inside the spanning card). */
export function ProgramColumnPanel({ programs, palette, x, width, tops }: ProgramColumnPanelProps) {
  return (
    <Panel>
      {programs.map((program, i) => (
        <Placed key={program.title} x={x} y={tops[i]} width={width}>
          <ProgramBlock program={program} palette={palette} />
        </Placed>
      ))}
    </Panel>
  )
}
