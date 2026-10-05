import { ChevronLeft } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { theme } from '../theme'

/** Back button, brand wordmark (placeholder) and Skip link, plus the boost tag artwork. */
export function SignupHeader({ skip }: { skip: string }) {
  return (
    <>
      <button
        type="button"
        className="absolute flex items-center justify-center rounded-full bg-white shadow-[0_2px_8px_rgba(0,0,0,0.12)]"
        style={{ left: 18, top: 75, width: 32, height: 32, color: theme.purple }}
      >
        <ChevronLeft size={16} strokeWidth={2.6} />
      </button>
      <ImagePlaceholder className="absolute rounded-[4px]" style={{ left: 144, top: 75, width: 101, height: 30 }} label="Rakuten logo" />
      <span className="absolute text-[16px] font-bold" style={{ right: 23, top: 80, color: theme.purple }}>
        {skip}
      </span>
      <ImagePlaceholder
        className="absolute rounded-[6px]"
        style={{ left: 134, top: 136, width: 116, height: 62, transform: 'rotate(-6deg)', clipPath: 'polygon(14% 0, 100% 0, 100% 100%, 14% 100%, 0 50%)' }}
        label="+10% boost tag"
      />
    </>
  )
}
