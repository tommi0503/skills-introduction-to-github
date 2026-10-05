import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { WaveBand } from '../../shared-1314/components/WaveBand'
import { fairTheme as t } from '../../shared-1314/theme'
import { cover as d } from '../data'

/** Front cover: title block, date/venue and arched photo. */
export function CoverPanel() {
  return (
    <Panel background={t.cream}>
      <Placed x={0} y={46} width={440} className="text-right font-noto-sans">
        <div className="text-[72px] font-semibold leading-[78px] tracking-[0.01em]" style={{ color: t.teal }}>
          {d.year}
        </div>
        <div className="text-[62px] font-semibold leading-[72px]" style={{ color: '#454545' }}>
          {d.titleLines.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
      </Placed>

      <Placed x={37} y={333} className="font-noto-sans text-[19px] font-semibold leading-[33px]" style={{ color: '#454545' }}>
        {d.details.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </Placed>

      <ImagePlaceholder
        className="absolute"
        style={{ left: 15, top: 462, width: 480, height: 479, borderRadius: '240px 240px 0 0' }}
        label="hanbok photo"
      />

      <WaveBand x={0} y={941} width={480} height={77} strip={{ color: t.band, height: 17 }} />
    </Panel>
  )
}
