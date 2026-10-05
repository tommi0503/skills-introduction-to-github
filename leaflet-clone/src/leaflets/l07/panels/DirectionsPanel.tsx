import { ImagePlaceholder, Panel } from '../../../ui'
import { TextLines } from '../../shared-0407/components/TextLines'
import { Heading } from '../components/Heading'
import { directions, reservation } from '../data'
import { theme } from '../theme'

const X = 55
const RIGHT = 45

/** Inside-middle (sky + green field from the sheet underlay): 오시는 길 and 예약 문의. */
export function DirectionsPanel() {
  return (
    <Panel style={{ color: theme.body }}>
      <Heading x={X} y={78} color={theme.olive}>
        {directions.heading}
      </Heading>
      <ImagePlaceholder label="map line art" className="absolute" style={{ left: 95, top: 180, width: 340, height: 258 }} />
      {directions.mapLabels.map((l) => (
        <TextLines
          key={l.lines[0]}
          className="absolute font-pretendard text-[15px] font-semibold"
          style={{ left: l.x, top: l.y }}
          lines={l.lines}
          lineClassName="leading-[23px]"
        />
      ))}
      <TextLines className="absolute font-pretendard text-[17px] tracking-[0.01em]" style={{ left: X, top: 468 }} lines={[directions.address]} lineClassName="leading-[26px]" />
      <TextLines className="absolute font-pretendard text-[17px] tracking-[0.01em]" style={{ left: X, top: 515 }} lines={directions.transit} lineClassName="leading-[24px]" />
      <TextLines
        className="absolute text-right font-pretendard text-[26px] font-black"
        style={{ right: RIGHT, top: 738 }}
        lines={[reservation.heading]}
        lineClassName="leading-[34px]"
      />
      <TextLines
        className="absolute text-right font-pretendard text-[22px] font-extrabold tracking-[0.05em]"
        style={{ right: RIGHT, top: 786 }}
        lines={reservation.contacts}
        lineClassName="leading-[32px]"
      />
      <TextLines
        className="absolute text-right font-pretendard text-[15px] tracking-[0.02em]"
        style={{ right: RIGHT - 2, top: 901 }}
        lines={reservation.note}
        lineClassName="leading-[26px]"
      />
    </Panel>
  )
}
