import { cn } from '../../../ui'
import { IconDisc } from '../../shared-2021/components/IconDisc'
import { QrIconBox } from '../../shared-2021/components/QrIconBox'
import type { ApplyMethod } from '../data'

export interface MethodBlockProps {
  method: ApplyMethod
  className?: string
}

/** One way to apply: icon + title, grey notes, blue highlight, optional QR caption. */
export function MethodBlock({ method, className }: MethodBlockProps) {
  return (
    <div className={cn('flex flex-col', className)}>
      <div className="flex items-center gap-[20px] pl-[74px]">
        <IconDisc icon={method.icon} size={41} iconSize={21} filled={method.iconFilled} />
        <span className="text-[27px] font-bold leading-none tracking-[-0.02em] text-[#3b5c80]">{method.title}</span>
      </div>
      <div
        className="flex flex-col items-center text-[18px] font-semibold leading-[30px] tracking-[-0.03em] text-[#5a5e64]"
        style={{ marginTop: method.notesGap }}
      >
        {method.notes.map((n) => (
          <span key={n}>{n}</span>
        ))}
      </div>
      <div style={{ marginTop: method.highlightGap }} className={cn('text-center leading-[30px] text-[#4a7bab]', method.highlightClassName)}>
        {method.highlight}
      </div>
      {method.qrCaption && (
        <div className="mt-[2px] flex items-start justify-between pl-[85px] pr-[58px]">
          <span className="mt-[4px] text-[17px] font-semibold tracking-[-0.03em] text-[#5a5e64]">{method.qrCaption}</span>
          <QrIconBox size={54} />
        </div>
      )}
    </div>
  )
}
