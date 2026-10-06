import { ArrowRight } from 'lucide-react'
import { Abs } from '../../ui'
import { theme } from './theme'
import type { Finding } from './data'

const px = (v: number) => v * theme.k
export const HLine = ({ y }: { y: number }) => <Abs x={px(5)} y={px(y)} w={1280 - px(10)} h={2} style={{ background: theme.line }} />

export function FindingColumn({ f, x }: { f: Finding; x: number }) {
  const I = f.icon
  return (
    <>
      <Abs x={x} y={px(84)} w={px(70)}><I size={118} strokeWidth={1} /></Abs>
      <Abs x={x} y={px(156)} className="font-inter text-[20px] font-bold">{f.title}</Abs>
      <Abs x={x} y={px(172)} w={px(100)} className="font-inter text-[15px] leading-[21px]">{f.body}</Abs>
    </>
  )
}
export const PageMark = ({ text }: { text: string }) => (
  <Abs x={1010} y={px(206)} className="flex items-center gap-3 font-inter text-[12px] font-semibold" style={{ width: 230, justifyContent: 'flex-end' }}>
    {text}<ArrowRight size={34} strokeWidth={1.5} className="ml-12" />
  </Abs>
)
