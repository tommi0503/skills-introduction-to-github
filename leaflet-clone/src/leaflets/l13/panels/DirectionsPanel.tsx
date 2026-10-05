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
      <ImagePlaceholder className="absolute" style={{ left: 137, top: -200, width: 360, height: 487, borderRadius: '0 0 180px 180px' }} label="map" />

      <Placed x={50} y={48}>
        <VerticalText className="font-nanum-gothic text-[35px] font-bold leading-none tracking-[0.2em]">
          <span style={{ color: t.ink }}>{d.title.replace(/ /g, '')}</span>
        </VerticalText>
      </Placed>

      <Placed x={52} y={398} width={400}>
        <InfoBlockList
          items={d.routes}
          titleGap={12}
          itemGap={18}
          className="font-nanum-gothic"
          titleClassName="text-[19px] font-bold leading-[28px]"
          bodyClassName="text-[19px] leading-[28px]"
          titleStyle={{ color: t.teal }}
          bodyStyle={{ color: t.body }}
        />
      </Placed>

      <Placed x={138} y={721} width={320}>
        <InfoBlockList
          items={d.credits}
          titleGap={2}
          itemGap={30}
          className="font-nanum-gothic"
          titleClassName="text-[18px] font-bold leading-[28px]"
          bodyClassName="text-[18px] font-bold leading-[28px]"
          titleStyle={{ color: t.teal }}
          bodyStyle={{ color: t.ink }}
        />
      </Placed>

      <WaveBand x={0} y={941} width={480} height={77} strip={{ color: t.band, height: 17 }} />
    </Panel>
  )
}
