import { Info } from 'lucide-react'
import { larana } from '../../shared-3435/theme'

export interface NoticeBoxProps {
  title: string
  body: string
  className?: string
}

/** Tinted, outlined call-out with an info icon title. */
export function NoticeBox({ title, body, className }: NoticeBoxProps) {
  return (
    <div
      className={`rounded-[9px] pl-[38px] pt-[30px] ${className ?? ''}`}
      style={{ background: '#e2e9f5', border: `2px solid ${larana.cardLine}` }}
    >
      <p className="m-0 flex items-center gap-[8px] text-[18px] font-bold leading-[24px]" style={{ color: larana.label }}>
        <Info size={18} fill={larana.blue} color="#fff" strokeWidth={2.5} />
        {title}
      </p>
      <p className="m-0 mt-[10px] whitespace-pre-line text-[14.5px] font-medium leading-[24.5px]" style={{ color: larana.inkSoft }}>
        {body}
      </p>
    </div>
  )
}
