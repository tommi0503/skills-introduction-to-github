import type { CSSProperties } from 'react'
import { Divider, ImagePlaceholder, Panel, Placed } from '../../../ui'
import { FareTable } from '../../shared-0407/components/FareTable'
import { PanelFrame, SerifHeading } from '../components'
import { content } from '../data'
import { frame, theme } from '../theme'

const STEP = { top: 106, pitch: 84, height: 84 }

/** Inside-left: 이용 안내 numbered steps + 운항 요금 table + wave art. */
export function GuidePanel() {
  const { guide, fares } = content
  return (
    <Panel background={theme.light} style={{ color: theme.ink }}>
      <PanelFrame color={theme.frameOnLight} />
      <SerifHeading y={64} className="text-[27px] leading-[40px]">
        {guide.heading}
      </SerifHeading>
      {guide.steps.map((step, i) => (
        <Placed key={step} x={46} y={STEP.top + i * STEP.pitch} width={380} height={STEP.height}>
          <div className="flex h-full items-center">
            <span className="w-[97px] pl-[38px] font-noto-serif text-[29px] leading-none">{i + 1}</span>
            <span className="font-noto-sans text-[17px] font-bold tracking-[0.01em]">{step}</span>
          </div>
          {i < guide.steps.length - 1 && <Divider color={theme.frameOnLight} thickness={2} className="absolute bottom-0" />}
        </Placed>
      ))}
      <SerifHeading y={469} className="text-[27px] leading-[40px]">
        {fares.heading}
      </SerifHeading>
      <Placed x={frame.x} y={525} width={frame.width} style={{ '--navy': theme.navy, '--rule': theme.frameOnLight } as CSSProperties}>
        <FareTable
          rows={fares.rows}
          columns={fares.columns}
          widths={['26%', '25%', '25%', '24%']}
          headClassName="text-white"
          headCellClassName="h-[52px] font-noto-sans text-[16px] font-bold"
          rowClassName="border-b-2"
          className="[&_thead]:bg-[var(--navy)] [&_tbody_tr]:border-[var(--rule)]"
          cellClassName="h-[76px] font-noto-sans text-[16px] leading-[23px]"
          typeCellClassName="font-bold"
          valueCellClassName="text-[#5a6584]"
        />
      </Placed>
      <ImagePlaceholder label="wave pattern" className="absolute" style={{ left: frame.x + 1, top: 832, width: frame.width - 2, height: 156 }} />
    </Panel>
  )
}
