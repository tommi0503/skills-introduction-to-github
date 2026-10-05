import { Search } from 'lucide-react'
import { AiOrb } from '../components/AiOrb'
import { CategoryCluster } from '../components/CategoryCluster'
import { FlowHeader } from '../components/FlowHeader'
import { PhotoArc } from '../components/PhotoArc'
import { PillInput } from '../components/PillInput'
import { arcPhotos, categories, steps, whereTo } from '../data'

/** Step 1 — choose a destination. */
export function WhereToScreen() {
  return (
    <div className="relative h-full w-full">
      <div className="absolute inset-x-[24.4px] top-[57.5px]">
        <FlowHeader step={1} total={steps.total} />
      </div>
      <div className="absolute inset-x-0 top-[151px] text-center">
        <div className="text-[22px] leading-[28px] font-semibold tracking-[-0.3px]">{whereTo.title}</div>
        <div className="mt-[6px] text-[13.5px] leading-[20px] text-[#8e8e8e]">{whereTo.subtitle}</div>
      </div>
      <div className="absolute inset-x-0 top-0 h-[308px] overflow-hidden">
        <PhotoArc photos={arcPhotos} dome={{ cx: 187.5, top: 266, r: 95 }} />
      </div>
      <div className="absolute inset-x-[25px] top-[310px]">
        <PillInput leading={<AiOrb size={39} />} leadingWidth={53} leadingInset={3} placeholder={whereTo.search} />
      </div>
      <div className="absolute inset-x-0 top-[350px]">
        <CategoryCluster
          items={categories}
          badgeFor={(key) =>
            key === 'search' ? (
              <span className="absolute -right-[3px] -bottom-[3px] flex rounded-full bg-[#ececec]">
                <Search size={10} strokeWidth={2.6} />
              </span>
            ) : null
          }
        />
      </div>
      <div className="absolute inset-x-0 top-[522px] text-center">
        <div className="text-[16.5px] leading-[22px] font-semibold tracking-[-0.2px]">{whereTo.emptyTitle}</div>
        <div className="mt-[3px] text-[12.5px] leading-[18px] text-[#9a9a9a]">{whereTo.emptySubtitle}</div>
      </div>
    </div>
  )
}
