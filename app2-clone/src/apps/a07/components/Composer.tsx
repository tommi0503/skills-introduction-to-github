import { Mic, Plus } from 'lucide-react'
import { theme } from '../theme'
import { FloatingButton } from './FloatingButton'

export function Composer({ placeholder }: { placeholder: string }) {
  return (
    <div className="flex items-center gap-[9px]">
      <FloatingButton icon={Plus} size={44} iconSize={22} />
      <div className="flex h-[44px] flex-1 items-center rounded-full bg-white pr-[5px] pl-[16px]" style={{ boxShadow: theme.floatShadow }}>
        <span className="flex-1 text-[16px] text-[#c2c2c2]">{placeholder}</span>
        <span className="flex h-[34px] w-[34px] items-center justify-center rounded-full bg-[#ececec] text-[#888]">
          <Mic size={16} strokeWidth={2} />
        </span>
      </div>
    </div>
  )
}
