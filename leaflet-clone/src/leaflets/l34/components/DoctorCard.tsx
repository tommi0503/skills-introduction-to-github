import { BulletList, ImagePlaceholder } from '../../../ui'
import { larana } from '../../shared-3435/theme'
import type { Doctor } from '../data'

/** Round portrait (placeholder) + name + bulleted credentials. */
export function DoctorCard({ doctor }: { doctor: Doctor }) {
  return (
    <div className="flex items-start">
      <ImagePlaceholder label={doctor.name} className="rounded-full" style={{ width: 133, height: 133 }} />
      <div className="ml-[34px] pt-[27px]">
        <p className="m-0 text-[20px] font-bold leading-[28px]" style={{ color: larana.label }}>
          {doctor.name}
        </p>
        <BulletList
          items={doctor.credentials}
          className="mt-[5px] text-[17.4px] font-medium leading-[30px]"
          itemClassName="gap-[11px]"
          marker="●"
          markerClassName="text-[6.5px]"
        />
      </div>
    </div>
  )
}
