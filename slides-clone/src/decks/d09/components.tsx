import type { CSSProperties, ReactNode } from 'react'
import { ImagePlaceholder, Slide } from '../../ui'
import { theme } from './theme'

export const Frame = ({ bg = '#fff', bar = true, light, children }: { bg?: string; bar?: boolean; light?: boolean; children: ReactNode }) => (
  <Slide background={bg}>
    <div className="relative origin-top-left" style={{ width: 1280 / theme.k, height: 720 / theme.k, transform: `scale(${theme.k})` }}>
      {children}
      <T x={0} y={167} w={315} className="text-center text-[2.6px]" style={{ color: light ? 'rgba(255,255,255,.7)' : '#9aa3b5' }}>{theme.footer}</T>
      {bar && <div className="absolute" style={{ left: 0, top: 174, width: 315, height: 3, background: theme.blue }} />}
    </div>
  </Slide>
)
export const T = ({ x, y, w, h, className = '', style, children }: { x: number; y: number; w?: number; h?: number; className?: string; style?: CSSProperties; children?: ReactNode }) => (
  <div className={`absolute font-inter ${className}`} style={{ left: x, top: y, width: w, height: h, ...style }}>{children}</div>
)
export const Ph = ({ x, y, w, h, r = 3, tone }: { x: number; y: number; w: number; h: number; r?: number; tone?: string }) => (
  <ImagePlaceholder tone={tone} className="absolute" style={{ left: x, top: y, width: w, height: h, borderRadius: r }} />
)
export const Kicker = ({ children }: { children: ReactNode }) => <T x={8} y={7} className="text-[3.4px]" style={{ color: theme.grey }}>{children}</T>
