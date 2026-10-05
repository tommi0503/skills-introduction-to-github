import { Paperclip } from 'lucide-react'
import { ImagePlaceholder, Panel, Placed } from '../../../ui'
import { checklist } from '../data'
import { blobs, theme } from '../theme'
import { CheckItem } from '../components/CheckItem'
import { LineBlock } from '../components/LineBlock'

/** Panel 1 — visiting checklist on a torn-paper note. */
export function ChecklistPanel() {
  return (
    <Panel>
      <Placed x={44} y={95}>
        <LineBlock lines={checklist.title} className="font-blackhan text-[58px] leading-[70px] tracking-[0.04em] text-white" />
      </Placed>
      <Placed x={33} y={282} width={388} height={571}>
        <ImagePlaceholder label="paper note" className="h-full w-full" style={{ borderRadius: blobs.note }} />
      </Placed>
      <Placed x={340} y={278}>
        <Paperclip size={92} strokeWidth={1.6} style={{ color: theme.clip }} className="-rotate-[40deg]" />
      </Placed>
      <Placed x={60} y={366} className="flex flex-col gap-[30px]">
        {checklist.items.map((lines) => (
          <CheckItem key={lines[0]} lines={lines} />
        ))}
      </Placed>
      <Placed x={232} y={760} width={218} height={176}>
        <ImagePlaceholder label="dog illustration" className="h-full w-full" style={{ borderRadius: '45% 40% 30% 30%' }} />
      </Placed>
    </Panel>
  )
}
