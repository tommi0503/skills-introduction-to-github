import type { ReactNode } from 'react'
import { Abs, cn } from '../../ui'

export const synth = {
  ink: '#0a0a0a',
  paper: '#f2f5f8',
  grad: 'linear-gradient(90deg,#16d9a5 0%,#4fb3d9 55%,#7b9cf0 100%)',
  gradV: 'linear-gradient(180deg,#22d7b0 0%,#5db5dd 55%,#7b9cf0 100%)',
}

export function GradText({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <span className={cn('bg-clip-text text-transparent', className)} style={{ backgroundImage: synth.grad }}>
      {children}
    </span>
  )
}

export function SynthHeader({ section, dark }: { section: string; dark?: boolean }) {
  const c = dark ? '#fff' : synth.ink
  return (
    <>
      <Abs x={53} y={20} className="font-grotesk text-[13px]" style={{ color: c }}>{section}</Abs>
      <Abs x={0} y={20} w={1227} className="text-right font-grotesk text-[13px]" style={{ color: c }}>nft.synth.org</Abs>
    </>
  )
}

export const pixelIcon = (x: number, y: number, w = 125, h = 140) => ({ x, y, w, h })
