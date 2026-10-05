import { Panel, Placed } from '../../../ui'
import { library } from '../../shared-2425/theme'
import { ContactFooter } from '../../shared-2425/components/ContactFooter'
import { ApplyBox } from '../components/ApplyBox'
import { InfoPillList } from '../components/InfoPillList'
import { TableBlock } from '../components/TableBlock'
import { academy, childClass, footer } from '../data'
import { layout } from '../theme'

const L = layout.p1

/** Panel 1 — 어린이 배움 특강 table + 그림책 마음 여행 아카데미. */
export function ProgramPanel() {
  return (
    <Panel>
      <TableBlock section={childClass} tab={L.tab} table={L.table} />
      <Placed x={50} y={L.titleY} className="whitespace-nowrap font-dohyeon text-[37px] leading-none tracking-[-0.02em]">
        <span style={{ color: library.coral, WebkitTextStroke: `0.6px ${library.coral}` }}>{academy.title.accent}</span>
        <span style={{ color: library.title, WebkitTextStroke: `0.6px ${library.title}` }}>{academy.title.rest}</span>
      </Placed>
      <Placed x={52} y={L.introY} className="text-[14.5px] font-semibold leading-[21px] tracking-[-0.02em]" style={{ color: library.deep }}>
        {academy.intro.map((l) => (
          <p key={l} className="m-0">
            {l}
          </p>
        ))}
      </Placed>
      <Placed x={46} y={L.factsY}>
        <InfoPillList
          items={academy.facts}
          fill={library.yellow}
          pillWidth={66}
          pillHeight={29}
          pitch={38}
          gap={10}
          labelClassName="font-dohyeon text-[14px] text-[#3e4166]"
          valueClassName="text-[16px] font-medium tracking-[-0.01em] text-[#4b4f72]"
        />
      </Placed>
      <ApplyBox {...academy.apply} style={{ left: L.box.x, top: L.box.y, width: L.box.width, height: L.box.height }} />
      <ContactFooter items={footer} y={L.footerY} className="text-[13px] font-semibold text-[#4b5070]" />
    </Panel>
  )
}
