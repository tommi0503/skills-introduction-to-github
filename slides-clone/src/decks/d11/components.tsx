import type { CSSProperties, ReactNode } from 'react'
import { ImagePlaceholder, Slide } from '../../ui'

export const Frame = ({ k, bg, children }: { k: number; bg: string; children: ReactNode }) => (
  <Slide background={bg}>
    <div className="relative origin-top-left" style={{ width: 1280 / k, height: 720 / k, transform: `scale(${k})` }}>{children}</div>
  </Slide>
)
export const T = ({ x, y, w, h, className = '', style, children }: { x: number; y: number; w?: number; h?: number; className?: string; style?: CSSProperties; children?: ReactNode }) => (
  <div className={`absolute font-inter ${className}`} style={{ left: x, top: y, width: w, height: h, ...style }}>{children}</div>
)
export const Ph = ({ x, y, w, h, radius = '0', tone }: { x: number; y: number; w: number; h: number; radius?: string; tone?: string }) => (
  <ImagePlaceholder tone={tone} className="absolute" style={{ left: x, top: y, width: w, height: h, borderRadius: radius }} />
)
export const Pixel = ({ x, y, size, lh, className = '', children }: { x: number; y: number; size: number; lh: number; className?: string; children: ReactNode }) => (
  <T x={x} y={y} className={`font-spacemono whitespace-nowrap ${className}`} style={{ fontSize: size, lineHeight: `${lh}px` }}>{children}</T>
)
