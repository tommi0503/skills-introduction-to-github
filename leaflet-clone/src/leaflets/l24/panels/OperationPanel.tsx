import { Divider, Panel, Placed } from '../../../ui'
import { library } from '../../shared-2425/theme'
import { IconCircleItem } from '../../shared-2425/components/IconCircleItem'
import { TableBlock } from '../components/TableBlock'
import { digitalClass, operations } from '../data'
import { layout } from '../theme'

const L = layout.p2

/** Panel 2 — 창의/디지털 특강 table + operation info list. */
export function OperationPanel() {
  return (
    <Panel>
      <TableBlock section={digitalClass} tab={L.tab} table={L.table} />
      {operations.map((op, i) => (
        <Placed key={op.title} x={32} y={L.opsY + i * L.opsPitch}>
          <IconCircleItem
            icon={op.icon}
            title={op.title}
            lines={[op.detail]}
            size={58}
            iconSize={26}
            gap={21}
            circleClassName="bg-[#45496f]"
            titleClassName="text-[18px] font-bold leading-[26px] tracking-[-0.02em] text-[#3e4166]"
            lineClassName="text-[14.5px] font-semibold leading-[24px] tracking-[0em] text-[#4b4f72]"
          />
        </Placed>
      ))}
      {operations.slice(1).map((op, i) => (
        <Placed key={op.title} x={111} y={L.opsY + 76 + i * L.opsPitch} width={325}>
          <Divider dashed color={library.rule} thickness={1.5} />
        </Placed>
      ))}
    </Panel>
  )
}
