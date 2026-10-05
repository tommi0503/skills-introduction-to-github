import { ChevronDown, Ellipsis, Ruler, RotateCcwSquare, X } from 'lucide-react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { Chrome } from '../components/Chrome'
import { CropFrame } from '../components/CropFrame'
import { SuggestionTile } from '../components/SuggestionTile'
import { ToolTabs } from '../components/ToolTabs'
import { editor } from '../data'
import { theme } from '../theme'

export function EditorScreen() {
  return (
    <AppScreen background={theme.dark}>
      <Chrome color="#fff" chipClassName="bg-[#5e5e5e]/95!" />
      <X size={21} strokeWidth={1.6} className="absolute top-[86px] left-[27px] text-[#e3e3e3]" />
      <Ellipsis size={20} strokeWidth={2} className="absolute top-[86px] left-[341px] text-[#e3e3e3]" />
      <span className="absolute top-[139px] left-[19px] flex size-[35px] items-center justify-center rounded-full bg-[#262626] text-[#e3e3e3]">
        <Ruler size={17} strokeWidth={1.7} />
      </span>
      <span className="absolute top-[139px] left-[225px] flex h-[35px] items-center gap-[4px] rounded-full bg-[#262626] pr-[11px] pl-[12px] text-[15px] text-[#e3e3e3]">
        {editor.aspect}
        <ChevronDown size={16} strokeWidth={2} />
      </span>
      <span className="absolute top-[139px] left-[333px] flex size-[35px] items-center justify-center rounded-full bg-[#262626] text-[#e3e3e3]">
        <RotateCcwSquare size={18} strokeWidth={1.7} />
      </span>
      <ImagePlaceholder label="photo being edited" className="absolute top-[194px] left-[24px] h-[428px] w-[340px]" />
      <CropFrame className="top-[186px] left-[16px] h-[442px] w-[357px]" arm={20} thickness={3} />
      <span className="absolute top-[581px] left-[91px] flex h-[28px] w-[207px] items-center justify-center rounded-[7px] bg-[#9e9e9e]/90 text-[13.5px] text-[#ececec]">
        {editor.hint}
      </span>
      <div className="absolute inset-x-[16px] top-[637px] flex gap-[9px]">
        {editor.suggestions.map((s) => (
          <SuggestionTile key={s.key} item={s} />
        ))}
      </div>
      <ToolTabs tools={editor.tools} active={editor.activeTool} />
    </AppScreen>
  )
}
