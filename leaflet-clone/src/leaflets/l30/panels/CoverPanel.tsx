import { Panel, Pill, Placed } from '../../../ui'
import { ArtworkLayer } from '../../shared-3031/components/ArtworkLayer'
import { DisplayTitle } from '../../shared-3031/components/DisplayTitle'
import { fonts, growth } from '../../shared-3031/theme'
import { cover } from '../data'

/** Panel 3 — front cover. */
export function CoverPanel() {
  return (
    <Panel background={growth.navyDeep}>
      <Placed x={122} y={117} width={239} height={40}>
        <Pill className={`h-full w-full bg-[#f2f3f4] text-[20px] ${fonts.display}`}>
          <span style={{ color: growth.navyDeep }}>{cover.badge}</span>
        </Pill>
      </Placed>
      <Placed x={0} y={203} width={483}>
        <DisplayTitle lines={cover.title} color="#fff" lineColors={[growth.sky, '#f4f4f4']} className="text-[66px] leading-[82px] tracking-[3px]" />
      </Placed>
      <Placed x={0} y={413} width={483} className="text-center text-[15px] leading-[21px] tracking-[-0.3px]" style={{ color: growth.paleText }}>
        {cover.intro.map((l) => (
          <p key={l} className="m-0">
            {l}
          </p>
        ))}
      </Placed>
      <ArtworkLayer items={[cover.figure]} />
    </Panel>
  )
}
