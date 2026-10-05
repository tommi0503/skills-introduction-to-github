import { ImagePlaceholder } from '../../../ui'
import { GScreen } from '../components/GScreen'
import { gmailDialog } from '../data'
import { theme } from '../theme'

export function GmailDialogScreen() {
  return (
    <GScreen background={theme.scrim}>
      <ImagePlaceholder label="dimmed logo" tone={theme.scrimArt} className="absolute left-[145px] top-[290px] h-[100px] w-[103px] rounded-[8px]" />
      <div
        className="absolute left-[23px] top-[321px] h-[216px] w-[344px] rounded-[6px] bg-white px-[22px] pt-[24px]"
        style={{ color: theme.text, boxShadow: '0 8px 20px rgba(0,0,0,.25)' }}
      >
        <h2 className="text-[15px] font-medium">{gmailDialog.title}</h2>
        <p className="mt-[21px] max-w-[290px] text-[13.5px] leading-[17.5px]">{gmailDialog.body}</p>
        <span className="absolute bottom-[18px] right-[21px] text-[14px] font-medium">{gmailDialog.action}</span>
      </div>
    </GScreen>
  )
}
