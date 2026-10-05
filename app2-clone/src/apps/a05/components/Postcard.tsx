import { ImagePlaceholder, cn } from '../../../ui'

/** Tilted share postcard: logo, ruled handwritten-style lines, divider and a photo. */
export function Postcard({ lines, className }: { lines: string[]; className?: string }) {
  const colors = ['#1d1d1f', '#9a9a9e', '#3a6fe0']
  return (
    <div className={cn('absolute', className)} style={{ transform: 'rotate(-2.5deg)' }}>
      <div className="relative h-full w-full rounded-[14px] bg-white" style={{ boxShadow: '0 6px 18px rgba(0,0,0,.14)' }}>
        <ImagePlaceholder label="corner logo" className="absolute left-[10px] top-[22px] h-[34px] w-[44px] rounded-[6px]" />
        <div className="absolute left-[10px] top-[65px] w-[132px]">
          {lines.map((l, i) => (
            <p
              key={l}
              className="border-b border-[#e3e6ee] font-condensed text-[12.5px] italic leading-[25px] tracking-[0.4px]"
              style={{ color: colors[i] }}
            >
              {l}
            </p>
          ))}
        </div>
        <div className="absolute left-[147px] top-[18px] h-[134px] w-[1.5px] bg-[#7ea2e6]" />
        <ImagePlaceholder label="place photo" className="absolute left-[157px] top-[22px] h-[122px] w-[92px] rounded-[12px]" />
      </div>
    </div>
  )
}
