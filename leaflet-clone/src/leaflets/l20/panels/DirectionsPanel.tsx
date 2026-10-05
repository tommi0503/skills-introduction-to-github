import { Building } from 'lucide-react'
import { Divider, ImagePlaceholder, Panel, Placed } from '../../../ui'
import { CardSheet } from '../../shared-2021/components/CardSheet'
import { CenteredRow } from '../../shared-2021/components/CenteredRow'
import { HeadPill } from '../../shared-2021/components/HeadPill'
import { IconDisc } from '../../shared-2021/components/IconDisc'
import { QrIconBox } from '../../shared-2021/components/QrIconBox'
import { RouteRow } from '../components/RouteRow'
import { cards, directionsPanel as d } from '../data'

export function DirectionsPanel() {
  return (
    <Panel>
      <CardSheet insets={cards[1]} />
      <CenteredRow top={78} centerX={236}>
        <HeadPill className="h-[27px] w-[98px] text-[21px]">{d.heading}</HeadPill>
      </CenteredRow>
      <Placed x={80} y={138} width={320} height={250}>
        <ImagePlaceholder label="map illustration" className="h-full w-full" />
      </Placed>
      <Placed x={108} y={421} className="flex items-center">
        <Building size={30} strokeWidth={2.2} className="text-[#4677ae]" />
        <span className="ml-[22px] text-[22.5px] font-bold tracking-[-0.03em] text-[#3b5c80]">{d.place}</span>
      </Placed>
      <Placed x={110} y={472} className="flex flex-col text-[18.5px] font-medium leading-[31px] tracking-[-0.02em] text-[#4a4f57]">
        {d.address.map((a) => (
          <span key={a}>{a}</span>
        ))}
      </Placed>
      <Placed x={88} y={550} width={308}>
        <Divider color="#dcdfe3" thickness={2} />
      </Placed>
      <Placed x={86} y={566} className="flex flex-col gap-[20px]">
        {d.routes.map((r) => (
          <RouteRow key={r.id} route={r} />
        ))}
      </Placed>
      <CenteredRow top={737}>
        <HeadPill className="h-[28px] w-[82px] text-[21px]">{d.contactHeading}</HeadPill>
      </CenteredRow>
      <Placed x={80} y={787} width={320} height={159} className="rounded-[14px] bg-[#d5e3f1]">
        <div className="absolute left-[30px] top-[27px] flex flex-col gap-[16px]">
          {d.contacts.map((c) => (
            <div key={c.id} className="flex items-center gap-[14px]">
              <IconDisc icon={c.icon} size={25} iconSize={14} filled={c.filled} />
              <span className="text-[20px] font-semibold leading-[25px] text-[#3b5c80]">{c.text}</span>
            </div>
          ))}
        </div>
        <QrIconBox size={52} className="absolute left-[245px] top-[85px]" />
      </Placed>
    </Panel>
  )
}
