import { ArrowLeft, Ellipsis } from 'lucide-react'
import { IconButton } from '../../../ui'

/** Back button · centred title · overflow button. */
export function ScreenHeader({ title }: { title: string }) {
  return (
    <div className="absolute inset-x-[20px] top-[81px] flex items-center justify-between">
      <IconButton icon={ArrowLeft} size={54} iconSize={20} strokeWidth={2} className="bg-white/45" />
      <span className="text-[17px] font-medium tracking-[-0.2px]">{title}</span>
      <IconButton icon={Ellipsis} size={54} iconSize={20} strokeWidth={2.4} className="bg-white/45" />
    </div>
  )
}
