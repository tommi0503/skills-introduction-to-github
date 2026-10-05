import { ImagePlaceholder, cn } from '../../../ui'
import type { FooterLine } from '../data'

export interface CompanyFooterProps {
  lines: FooterLine[]
  buttonLabel: string
  className?: string
}

/** Business info footer with brand logo (placeholder) and terms button. */
export function CompanyFooter({ lines, buttonLabel, className }: CompanyFooterProps) {
  return (
    <div className={cn('px-[37px] font-pretendard text-[#959595]', className)}>
      <ImagePlaceholder label="Laundrygo 로고" className="mt-[3px] h-[31px] w-[127px]" />
      <div className="mt-[9px] text-[10.5px] leading-[15.5px] tracking-[0px]">
        {lines.map((line) => (
          <div key={line.text}>
            {line.text}
            {line.link && <span className="underline underline-offset-2">{line.link}</span>}
            {line.underlined && <span className="underline underline-offset-2">{line.underlined}</span>}
          </div>
        ))}
      </div>
      <div className="mt-[14px] inline-flex h-[23px] items-center rounded-[2px] border border-[#888] px-[5px] text-[9.3px] tracking-[-0.2px] text-[#666]">
        {buttonLabel}
      </div>
    </div>
  )
}
