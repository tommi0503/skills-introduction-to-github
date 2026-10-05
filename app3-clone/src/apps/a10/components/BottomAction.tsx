import { Button } from '../../../ui'
import { theme } from '../theme'

/** Sticky white footer with a full-width pill button. */
export function BottomAction({ label }: { label: string }) {
  return (
    <div className="absolute inset-x-0 bottom-0 top-[746px] z-10 border-t border-[#ececec] bg-white">
      <Button
        className="absolute top-[12px] left-[17px] h-[53px] w-[356px] rounded-full text-[16px] font-semibold"
        style={{ background: theme.green, color: theme.greenInk }}
      >
        {label}
      </Button>
    </div>
  )
}
