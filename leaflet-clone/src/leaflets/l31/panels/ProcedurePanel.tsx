import { Panel, Pill, Placed } from '../../../ui'
import { DisplayTitle } from '../../shared-3031/components/DisplayTitle'
import { growth } from '../../shared-3031/theme'
import { procedure } from '../data'

/** Panel 3 — application steps as stacked pills. */
export function ProcedurePanel() {
  return (
    <Panel>
      <Placed x={0} y={103} width={474}>
        <DisplayTitle lines={procedure.title} color={growth.ink} className="text-[33px] leading-[50px] tracking-[2.5px]" />
      </Placed>
      <Placed x={116} y={178} width={249} className="flex flex-col gap-[15px]">
        {procedure.steps.map((s) => (
          <span key={s.no} className="block h-[33px] rounded-[9px]" style={{ background: growth.stepFill }}>
            <Pill className="h-full w-full justify-start gap-[11px] rounded-none pl-[34px] text-[17.5px] font-bold text-white">
              <span className="tracking-[0.3px]">STEP {s.no}</span>
              <span>{s.label}</span>
            </Pill>
          </span>
        ))}
      </Placed>
    </Panel>
  )
}
