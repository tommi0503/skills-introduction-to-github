import { Fragment } from 'react'
import { X } from 'lucide-react'
import { cookie } from '../data'
import { theme } from '../theme'

/** Consent dialog captured pinned to the bottom-right of the first viewport. */
export function CookieBanner() {
  return (
    <div
      className="absolute rounded-[16px] border bg-white px-[16px] pt-[14px]"
      style={{ left: 897, top: 749, width: 527, height: 135, borderColor: '#d5d9e2', boxShadow: '0 4px 16px rgba(0,0,0,0.06)', color: theme.ink }}
    >
      <p className="w-[460px] text-[13px] leading-[21.125px] text-black/55">
        {cookie.text}{' '}
        {cookie.links.map((l, i) => (
          <Fragment key={l}>
            <span className="font-[450] text-[#0a0a0a] underline underline-offset-2">{l}</span>
            {i < cookie.links.length - 2 ? ', ' : i === cookie.links.length - 2 ? ', and ' : '.'}
          </Fragment>
        ))}
      </p>
      <X size={14} strokeWidth={1.5} className="absolute text-black/45" style={{ left: 485, top: 25 }} />
      <div className="absolute inset-x-[16px] bottom-[14px] flex items-center">
        <span className="flex h-[30px] w-[138px] items-center justify-center rounded-full border border-[#dcdcdc] text-[14px] font-[450]">
          {cookie.settings}
        </span>
        <span className="ml-auto flex h-[28px] w-[86px] items-center justify-center rounded-full bg-[#0a0a0a] text-[14px] font-[450] text-white">
          {cookie.reject}
        </span>
        <span className="ml-[8px] flex h-[28px] w-[148px] items-center justify-center rounded-full bg-[#0a0a0a] text-[14px] font-[450] text-white">
          {cookie.accept}
        </span>
      </div>
    </div>
  )
}
