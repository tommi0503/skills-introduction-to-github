import { IconBadge, ImagePlaceholder } from '../../../ui'
import { larana } from '../../shared-3435/theme'
import type { CareService } from '../data'

const BADGE = 56

/** Outlined card: round blue icon badge + title + detail line. */
export function ServiceCard({ service }: { service: CareService }) {
  return (
    <div
      className="flex h-[101px] items-center rounded-[10px] pl-[24px]"
      style={{ border: `2px solid ${larana.cardLine}` }}
    >
      {service.icon ? (
        <span className="rounded-full" style={{ background: larana.blue }}>
          <IconBadge icon={service.icon} size={BADGE} iconSize={28} className="text-white" />
        </span>
      ) : (
        <ImagePlaceholder label={service.title} className="rounded-full" style={{ width: BADGE, height: BADGE }} />
      )}
      <div className="ml-[11px]">
        <p className="m-0 text-[16.5px] font-bold leading-[24px]" style={{ color: larana.ink }}>
          {service.title}
        </p>
        <p className="m-0 text-[14.5px] font-medium leading-[24px]" style={{ color: larana.inkSoft }}>
          {service.detail}
        </p>
      </div>
    </div>
  )
}
