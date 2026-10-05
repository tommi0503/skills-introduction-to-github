import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { clinic } from '../../shared-3435/data'
import { larana } from '../../shared-3435/theme'
import { departments } from '../data'

const PHOTO_HEIGHT = 955

/** Right outside panel (front cover): building photo with clinic name, departments strip. */
export function CoverPanel() {
  return (
    <Panel background={larana.paper}>
      <ImagePlaceholder label="병원 건물 사진" tone="#c9ccd1" style={{ width: 480, height: PHOTO_HEIGHT }} />
      <Placed x={0} y={314} width={498} className="flex flex-col items-center text-white">
        <span className="pl-[0.32em] text-[16.5px] font-medium leading-[22px] tracking-[0.32em]">{clinic.latin}</span>
        <span className="mt-[8px] pl-[0.06em] text-[57px] font-bold leading-[60px] tracking-[0.06em]">{clinic.name}</span>
      </Placed>
      <Placed
        x={0}
        y={PHOTO_HEIGHT}
        width={486}
        height={1018 - PHOTO_HEIGHT}
        className="flex items-center justify-center text-[20px] font-semibold"
        style={{ color: larana.label }}
      >
        {departments.map((d, i) => (
          <span key={d} className="flex items-center">
            {i > 0 && <span className="mx-[16px] h-[22px] w-[2px]" style={{ background: larana.label }} />}
            {d}
          </span>
        ))}
      </Placed>
    </Panel>
  )
}
