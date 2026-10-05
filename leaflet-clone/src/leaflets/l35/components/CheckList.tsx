import { CircleCheck } from 'lucide-react'
import { BulletList } from '../../../ui'
import { larana } from '../../shared-3435/theme'

/** Symptoms list with filled blue check-circle markers. */
export function CheckList({ items, className }: { items: string[]; className?: string }) {
  return (
    <BulletList
      items={items}
      className={className}
      itemClassName="gap-[14px] items-center"
      marker={<CircleCheck size={17} fill={larana.blue} color="#fff" strokeWidth={2.5} />}
      markerClassName="flex"
    />
  )
}
