import { ImagePlaceholder, Panel, Placed, VerticalText } from '../../../ui'
import { InfoBlockList } from '../../shared-1314/components/InfoBlock'
import { WaveBand } from '../../shared-1314/components/WaveBand'
import { fairTheme as t } from '../../shared-1314/theme'
import { directions as d } from '../data'

/** Middle outer panel: map, vertical title, route info and organisers. */
export function DirectionsPanel() {
  return (
    <Panel background={t.cream}>
      {/* map artwork, cropped to a circle */}
      <ImagePlaceholder className="absolute rounded-full" style={{ left: 136, top: -66, width: 354, height: 354 }} label="map" />

      <Placed x={50} y={48}>
        <VerticalText className="font-noto-sans text-[35px] font-medium leading-none tracking-[0.2em]" >
          <span style={{ color: t.ink }}>{d.title.replace(/ /g, '')}</span>
        </VerticalText>
      </Placed>

      <Placed x={52} y={398} width={400}>
        <InfoBlockList
          items={d.routes}
          titleGap={12}
          itemGap={18}
          className="font-noto-sans"
          titleClassName="text-[19px] font-bold leading-[28px] text-[#467379]"
          bodyClassName="text-[19px] leading-[28px] text-[#6b6b6b]"
        />
      </Placed>

      <Placed x={138} y={721} width={320}>
        <InfoBlockList
          items={d.credits}
          titleGap={2}
          itemGap={30}
          className="font-noto-sans"
          titleClassName="text-[18px] font-bold leading-[28px] text-[#467379]"
          bodyClassName="text-[18px] font-medium leading-[28px] text-[#454545]"
        />
      </Placed>

      <WaveBand x={0} y={941} width={480} height={77} strip={{ color: t.band, height: 17 }} />
    </Panel>
  )
}
