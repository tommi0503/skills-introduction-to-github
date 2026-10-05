import { Panel, Placed } from '../../../ui'
import { donationInfo, programs } from '../data'
import { theme } from '../theme'
import { OutlinedPill } from '../components/OutlinedPill'
import { InfoBox } from '../components/InfoBox'

/** Panel 1 — donation programmes inside a white framed card. */
export function ProgramPanel() {
  return (
    <Panel>
      <Placed x={22} y={21} width={426} height={974} className="border-2 border-[#2b2b2b]" style={{ background: theme.card }} />
      <Placed x={22} y={78} width={426} className="flex flex-col items-center">
        <h2 className="m-0 text-[47px] font-medium leading-none tracking-[0.01em] text-[#111]">{programs.title}</h2>
        <p className="m-0 mt-[16px] text-center text-[17px] font-bold leading-[26px] tracking-[0.01em]" style={{ color: theme.accent }}>
          {programs.note.map((l) => (
            <span key={l} className="block">{l}</span>
          ))}
        </p>
      </Placed>
      {programs.buttons.map((b, i) => (
        <Placed key={b.label} x={97} y={223 + i * 90.5} width={275} height={63}>
          <OutlinedPill label={b.label} fill={b.fill} className="h-full w-full text-[19px]" />
        </Placed>
      ))}
      <Placed x={56} y={607} width={357} height={355}>
        <InfoBox sections={donationInfo} className="h-full w-full bg-[#f4f4f4] pt-[42px]" />
      </Placed>
    </Panel>
  )
}
