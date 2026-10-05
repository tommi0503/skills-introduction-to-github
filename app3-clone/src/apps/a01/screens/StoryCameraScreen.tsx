import { Badge, ChevronDown, Infinity as InfinityIcon, RefreshCcw, X, ZapOff } from 'lucide-react'
import type { ReactNode } from 'react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { IgStatusBar } from '../components/IgStatusBar'
import { LayoutGlyph } from '../components/LayoutGlyph'
import { activeCameraMode, cameraModes } from '../data'
import { ig } from '../theme'

function ToolRail() {
  const tools: { key: string; node: ReactNode }[] = [
    { key: 'text', node: <span className="font-condensed text-[22px] leading-none font-medium tracking-[-0.5px]">Aa</span> },
    { key: 'boomerang', node: <InfinityIcon size={26} strokeWidth={1.8} /> },
    { key: 'layout', node: <LayoutGlyph size={26} strokeWidth={1.7} /> },
    { key: 'more', node: <ChevronDown size={30} strokeWidth={1.4} /> },
  ]
  return (
    <div className="absolute top-[343px] left-[21px] flex w-[24px] flex-col items-center gap-[20px] text-white">
      {tools.map((t) => (
        <div key={t.key} className="flex h-[28px] items-center">
          {t.node}
        </div>
      ))}
    </div>
  )
}

function CaptureRow() {
  return (
    <div className="absolute top-[648px] left-0 h-[76px] w-full">
      <div className="absolute left-[157px] flex h-[76px] w-[76px] items-center justify-center rounded-full border-[4px] border-white">
        <div className="h-[62px] w-[62px] rounded-full bg-[#cfcdd0]" />
      </div>
      <ImagePlaceholder tone={ig.photoOnDark} className="absolute top-[14px] left-[262px] h-[48px] w-[48px] rounded-full" label="effect" />
      <ImagePlaceholder className="absolute top-[21px] left-[339px] h-[35px] w-[35px] rounded-full" label="effect" />
    </div>
  )
}

function ModeBar() {
  return (
    <div className="absolute top-[776px] left-0 flex h-[36px] w-full items-center">
      <ImagePlaceholder className="absolute left-[16px] h-[34px] w-[34px] rounded-[7px]" tone="#f4f4f4" label="last photo" />
      <div className="absolute left-[116px] flex gap-[13px] text-[13px] tracking-[1.3px]">
        {cameraModes.map((m) => (
          <span key={m} className={cn(m === activeCameraMode ? 'font-semibold text-white' : 'font-medium text-[#8c8c8f]')}>
            {m}
          </span>
        ))}
      </div>
      <span className="absolute right-[12px] flex h-[44px] w-[44px] items-center justify-center rounded-full bg-[#3b3d43] text-white">
        <RefreshCcw size={22} strokeWidth={1.9} />
      </span>
    </div>
  )
}

/** Instagram story camera: dark viewfinder with tool rail, shutter and mode switcher. */
export function StoryCameraScreen() {
  return (
    <AppScreen background={ig.dark} className="font-inter text-white">
      <IgStatusBar color="#fff" />
      <div className="absolute inset-x-0 top-[60px] h-[692px] rounded-[22px]" style={{ background: ig.darkViewfinder }}>
        <div className="flex items-center justify-between px-[22px] pt-[20px]">
          <X size={26} strokeWidth={1.7} />
          <ZapOff size={24} strokeWidth={2.1} />
          <Badge size={28} strokeWidth={2.8} />
        </div>
      </div>
      <ToolRail />
      <CaptureRow />
      <ModeBar />
    </AppScreen>
  )
}
