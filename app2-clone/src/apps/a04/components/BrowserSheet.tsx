import type { ReactNode } from 'react'
import { ChevronLeft, PanelBottom, RotateCw, Share, X } from 'lucide-react'
import { theme } from '../theme'
import { FloatingCircle } from './FloatingCircle'
import { StatusRow } from './StatusRow'

export interface BrowserSheetProps {
  host: string
  children: ReactNode
}

/** In-app browser presented as a sheet over a dimmed backdrop, with header and bottom toolbar. */
export function BrowserSheet({ host, children }: BrowserSheetProps) {
  return (
    <div className="absolute inset-0" style={{ background: theme.backdrop }}>
      <StatusRow />
      <div className="absolute inset-x-0 bottom-0 top-[68px] overflow-hidden rounded-t-[38px] bg-white">
        <div className="absolute inset-x-0 top-[54px] bottom-0">{children}</div>
        <div
          className="absolute inset-x-0 top-0 flex h-[74px] items-center justify-between px-[15px]"
          style={{ background: 'linear-gradient(#fff 80%, rgba(255,255,255,0))' }}
        >
          <FloatingCircle className="h-[45px] w-[45px]">
            <X size={26} strokeWidth={1.6} color={theme.text} />
          </FloatingCircle>
          <span className="text-[16px] font-semibold" style={{ color: theme.text }}>
            {host}
          </span>
          <FloatingCircle className="h-[45px] w-[45px]">
            <PanelBottom size={18} strokeWidth={1.8} color={theme.text} />
          </FloatingCircle>
        </div>
        <div className="absolute inset-x-0 bottom-[24px] flex items-center justify-between px-[22px]">
          <FloatingCircle className="h-[47px] w-[47px]">
            <ChevronLeft size={24} strokeWidth={1.6} color="#b9b9b7" />
          </FloatingCircle>
          <FloatingCircle className="h-[47px] w-[102px] gap-[29px] rounded-full">
            <Share size={20} strokeWidth={1.8} color={theme.text} />
            <RotateCw size={20} strokeWidth={1.8} color={theme.text} />
          </FloatingCircle>
        </div>
      </div>
    </div>
  )
}
