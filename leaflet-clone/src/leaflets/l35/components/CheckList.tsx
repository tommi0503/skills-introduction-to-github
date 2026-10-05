import type { CSSProperties } from 'react'
import { CircleCheck } from 'lucide-react'
import { BulletList } from '../../../ui'
import { larana } from '../../shared-3435/theme'

/** Symptoms list with filled blue check-circle markers. */
export function CheckList({ items, className, style }: { items: string[]; className?: string; style?: CSSProperties }) {
  return (
    <div style={style}>
    <BulletList
      items={items}
      className={className}
      itemClassName="gap-[11px] items-center"
      marker={<CircleCheck size={20} fill={larana.blue} color="#fff" strokeWidth={2.5} />}
      markerClassName="flex"
    />
    </div>
  )
}
