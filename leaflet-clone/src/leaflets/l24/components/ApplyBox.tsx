import type { CSSProperties } from 'react'
import { library } from '../../shared-2425/theme'

interface ApplyBoxProps {
  title: string
  note: string
  contact: string
  style?: CSSProperties
}

/** Outlined lavender card: how to apply + contact. */
export function ApplyBox({ title, note, contact, style }: ApplyBoxProps) {
  return (
    <div
      className="absolute box-border flex flex-col rounded-[14px] pl-[23px] pt-[20px]"
      style={{ border: `2.5px solid ${library.navy}`, background: 'linear-gradient(90deg,#dde3f3,#e6e9f4)', color: library.deep, ...style }}
    >
      <p className="m-0 text-[20px] font-semibold leading-none tracking-[-0.03em]">{title}</p>
      <p className="m-0 mt-[17px] text-[11.5px] font-semibold leading-none tracking-[-0.02em]">{note}</p>
      <p className="m-0 mt-[17px] text-[13px] font-semibold leading-none">{contact}</p>
    </div>
  )
}
