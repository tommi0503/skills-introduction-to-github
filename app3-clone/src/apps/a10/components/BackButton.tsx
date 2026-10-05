import { ArrowLeft } from 'lucide-react'
import { IconButton } from '../../../ui'

export function BackButton() {
  return (
    <IconButton
      icon={ArrowLeft}
      size={42}
      iconSize={24}
      strokeWidth={1.6}
      className="absolute top-[47px] left-[19px] bg-[#ececec] text-[#1d2a12]"
    />
  )
}
