import { bond, device } from '../theme'

export interface PeekPhoneProps {
  /** Visible fragments of the screen behind the stage edge. */
  caption: string
  hint: string
}

/**
 * The partially visible 6th device at the stage's right edge: a dark outlined
 * phone with a light content inset whose lower half is a keyboard.
 */
export function PeekPhone({ caption, hint }: PeekPhoneProps) {
  return (
    <div
      className="relative overflow-hidden border border-[#262626]"
      style={{ width: device.width, height: device.height, borderRadius: device.screenRadius, background: bond.stage }}
    >
      <div className="absolute overflow-hidden" style={{ left: 0, top: 33, width: 40, height: 290, background: bond.screen }}>
        <span className="absolute text-[6px] whitespace-nowrap text-[#333]" style={{ left: -2, top: 89 }}>
          {caption}
        </span>
        <span className="absolute text-[8px] whitespace-nowrap text-[#bdbdbd]" style={{ left: -6, top: 109 }}>
          {hint}
        </span>
        <div className="absolute inset-x-0 bottom-0 flex flex-col gap-[2.5px] pt-[17px] pl-0" style={{ top: 177, background: bond.keyboard }}>
          {[0, 1, 2].map((r) => (
            <div key={r} className="flex gap-[3px]">
              <span className="-ml-[5px] h-[16px] w-[12px] rounded-[2px] bg-white" />
              <span className="ml-[1px] h-[16px] w-[12px] rounded-[2px] bg-white" />
            </div>
          ))}
          <span className="-ml-[5px] h-[16px] w-[12px] rounded-[2px] bg-white" />
        </div>
      </div>
    </div>
  )
}
