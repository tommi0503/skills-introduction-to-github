import { ArrowLeft, EllipsisVertical } from 'lucide-react'
import { theme } from '../theme'

/** Back arrow · centred title · overflow menu. */
export function NavHeader({ title, top = 54 }: { title: string; top?: number }) {
  return (
    <div className="relative flex items-center justify-between px-[16px]" style={{ height: 36, marginTop: top - 50, color: theme.ink }}>
      <ArrowLeft size={23} strokeWidth={1.8} />
      <span className="absolute left-1/2 -translate-x-1/2 text-[20px] font-medium tracking-[-0.3px]">{title}</span>
      <EllipsisVertical size={22} strokeWidth={2.6} className="-mr-[2px]" />
    </div>
  )
}
