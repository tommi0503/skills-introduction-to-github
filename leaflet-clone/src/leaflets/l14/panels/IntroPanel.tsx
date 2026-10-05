import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { fairTheme as t } from '../../shared-1314/theme'
import { intro as d } from '../data'

/** Inside left panel: headline, description, venue photo and key facts. */
export function IntroPanel() {
  return (
    <Panel background={t.slate} style={{ color: t.onSlate }} className="font-nanum-gothic">
      <Placed x={0} y={45} width={434} className="text-right text-[41px] font-bold leading-[57px] tracking-[0.02em]">
        {d.headline.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </Placed>

      <Placed x={40} y={261} className="text-[19.5px] leading-[29.5px]" style={{ color: t.onSlateMuted }}>
        {d.body.map((l) => (
          <div key={l}>{l}</div>
        ))}
      </Placed>

      <ImagePlaceholder
        className="absolute"
        style={{ left: 0, top: 425, width: 437, height: 370, borderRadius: '0 190px 190px 0 / 0 185px 185px 0' }}
        label="venue aerial photo"
      />

      <Placed x={131} y={838} width={349}>
        {d.facts.map((f) => (
          <div key={f} className="text-[20px] leading-[30px]" style={{ height: 39, borderBottom: `2px solid ${t.ruleOnSlate}` }}>
            {f}
          </div>
        ))}
      </Placed>
    </Panel>
  )
}
