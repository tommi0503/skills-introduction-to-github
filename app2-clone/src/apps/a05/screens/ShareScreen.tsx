import { X } from 'lucide-react'
import { AppScreen } from '../../../ui'
import { share } from '../data'
import { theme } from '../theme'
import { Chrome } from '../components/Chrome'
import { CircleAction } from '../components/CircleAction'
import { MapBackdrop } from '../components/MapBackdrop'
import { PlaceMarker } from '../components/PlaceMarker'
import { Postcard } from '../components/Postcard'

export function ShareScreen() {
  return (
    <AppScreen className="font-archivo">
      <MapBackdrop />
      <PlaceMarker className="left-[203px] top-[180px]" />
      <div className="absolute inset-x-0 top-[352px] bottom-0 rounded-t-[30px]" style={{ background: theme.shareSheet, boxShadow: '0 -4px 20px rgba(0,0,0,.06)' }}>
        <div className="absolute left-1/2 top-[9px] h-[4px] w-[50px] -translate-x-1/2 rounded-full bg-[#c9cbce]" />
        <X size={22} strokeWidth={1.8} className="absolute left-[348px] top-[18px]" />
        <Postcard lines={share.postcard.lines} className="left-[67px] top-[33px] h-[160px] w-[252px]" />
        <div className="absolute inset-x-0 top-[213px] h-px bg-[#e0e2e4]" />
        <p className="a05-wide absolute left-[18px] top-[225px] text-[15px] font-bold tracking-[-0.7px] text-[#111]">{share.dmsTitle}</p>
        <div className="absolute left-[18px] top-[256px] flex gap-[15px]">
          {share.contacts.map((c) => (
            <CircleAction key={c.key} label={c.label} icon={c.icon} tone="#e2d4ec" />
          ))}
        </div>
        <div className="absolute inset-x-0 top-[345px] h-px bg-[#e0e2e4]" />
        <div className="absolute left-[70px] top-[355px] flex gap-[27px]">
          {share.targets.map((t) => (
            <CircleAction key={t.key} label={t.label} icon={t.icon} tone="#bfe5c0" />
          ))}
        </div>
      </div>
      <Chrome />
    </AppScreen>
  )
}
