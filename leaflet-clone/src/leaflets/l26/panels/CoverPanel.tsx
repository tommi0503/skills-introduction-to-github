import { Panel, Placed } from '../../../ui'
import { seoul } from '../../shared-2627/theme'
import { Photo } from '../../shared-2627/components/Photo'
import { cover } from '../data'

/** Panel 3 — SEOUL: TRAVEL GUIDE cover. */
export function CoverPanel() {
  return (
    <Panel background={seoul.paper}>
      <Placed x={32} y={40} className="font-montserrat font-extrabold leading-none" style={{ color: seoul.sky }}>
        <p className="m-0 text-[92px] tracking-[0.01em]">{cover.title[0]}</p>
        <p className="m-0 mt-[2px] text-[52px] tracking-[0.02em]">{cover.title[1]}</p>
      </Placed>
      <Placed x={18} y={201} width={462} height={3.5} style={{ background: seoul.skyLight }} />
      <Placed x={0} y={232} width={496} className="text-center text-[20px] font-bold leading-none tracking-[-0.03em]" style={{ color: seoul.slate }}>
        {cover.tagline}
      </Placed>
      <Photo box={cover.photo} />
    </Panel>
  )
}
