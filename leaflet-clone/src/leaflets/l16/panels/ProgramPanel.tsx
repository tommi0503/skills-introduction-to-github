import { Panel, Placed } from '../../../ui'
import { EyebrowHeading } from '../../shared-1516/components/EyebrowHeading'
import { concertTheme as t } from '../../shared-1516/theme'
import { ProgramList } from '../components/ProgramList'
import { program as d } from '../data'

const frame = '#d9c3b8'

/** Inside middle panel: framed concert programme. */
export function ProgramPanel() {
  return (
    <Panel background={t.burgundy}>
      <div className="absolute" style={{ left: 27, top: 25, right: 27, bottom: 25, border: `2px solid ${frame}` }} />
      <Placed x={0} y={81} width={480}>
        <EyebrowHeading eyebrow={d.eyebrow} title={d.title} eyebrowColor={t.onDarkMuted} titleColor={t.onDark} align="center" />
      </Placed>
      {d.parts.map((part) => (
        <Placed key={part.title} x={0} y={part.y} width={480}>
          <ProgramList part={part} />
        </Placed>
      ))}
      <Placed
        x={114}
        y={d.intermission.y}
        width={250}
        height={59}
        className="flex items-center justify-center gap-[12px] font-montserrat text-[15px] font-semibold tracking-[0.04em]"
        style={{ border: `2px solid ${frame}`, color: t.onDark }}
      >
        <span>{d.intermission.label}</span>
        <span className="font-pretendard tracking-normal">{d.intermission.length}</span>
      </Placed>
    </Panel>
  )
}
