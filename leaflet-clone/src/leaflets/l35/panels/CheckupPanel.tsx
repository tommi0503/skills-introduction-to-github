import { Panel, Placed } from '../../../ui'
import { PanelTitle } from '../../shared-3435/components/PanelTitle'
import { larana } from '../../shared-3435/theme'
import { ProgramTable } from '../components/ProgramTable'
import { StepFlow } from '../components/StepFlow'
import { SubHeading } from '../components/SubHeading'
import { checkup } from '../data'

/** Inside middle panel (tinted): checkup programme table and the 4-step procedure. */
export function CheckupPanel() {
  return (
    <Panel background="linear-gradient(180deg, #e4e8f2 0%, #e8ecf5 60%, #e6eaf4 100%)">
      <Placed x={0} y={50} width={480}>
        <PanelTitle>{checkup.title}</PanelTitle>
        <p className="m-0 mt-[6px] text-center text-[12px] font-medium leading-[16px]" style={{ color: larana.inkSoft }}>
          {checkup.subtitle}
        </p>
      </Placed>
      <Placed x={36} y={150} width={410}>
        <ProgramTable headers={checkup.headers} rows={checkup.rows} />
      </Placed>
      <Placed x={65} y={513}>
        <SubHeading>{checkup.stepsTitle}</SubHeading>
      </Placed>
      <Placed x={37} y={570} width={408}>
        <StepFlow steps={checkup.steps} />
      </Placed>
    </Panel>
  )
}
