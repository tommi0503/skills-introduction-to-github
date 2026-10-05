import { X } from 'lucide-react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { DeviceChrome } from '../components/DeviceChrome'
import { SquareButton } from '../components/SquareButton'
import { evidence } from '../data'
import { rf } from '../theme'

/** Full-size photo evidence viewer with thumbnail strip. */
export function EvidenceScreen() {
  return (
    <AppScreen background={rf.bg} className="font-jakarta" style={{ color: rf.text }}>
      <DeviceChrome />
      <SquareButton className="absolute top-[73px] right-[19px] bg-[#fbfbfa]">
        <X size={15} strokeWidth={1.8} />
      </SquareButton>
      <ImagePlaceholder className="absolute top-[172px] right-[19px] left-[21px] h-[499px] rounded-[22px]" label="damaged parcel photo" />
      <div className="absolute top-[704px] left-0 flex w-full items-center justify-center gap-[4px]">
        {evidence.thumbs.map((t) => (
          <ImagePlaceholder
            key={t.key}
            className={cn('rounded-[5px]', t.active ? 'mr-[2px] h-[36px] w-[35px] shadow-[0_3px_6px_rgba(0,0,0,0.25)]' : 'h-[30px] w-[30px]')}
            label={t.key}
          />
        ))}
      </div>
      <p className="absolute top-[783px] w-full text-center text-[13.5px] tracking-[-0.4px] text-[#555]">{evidence.caption}</p>
    </AppScreen>
  )
}
