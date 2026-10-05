import { ChevronDown } from 'lucide-react'
import { Placed } from '../../../ui'
import { AppStatusBar } from '../components/AppStatusBar'
import { ReaderControls } from '../components/ReaderControls'
import { chapter, player } from '../data'

const LINE = 24.3

/** One justified line of body copy (last line of a paragraph is still stretched, as in the mock). */
function TextLine({ text, indent = 0 }: { text: string; indent?: number }) {
  return (
    <div
      className="whitespace-nowrap"
      style={{ height: LINE, lineHeight: `${LINE}px`, paddingLeft: indent, textAlign: 'justify', textAlignLast: 'justify' }}
    >
      {text}
    </div>
  )
}

/** Right phone — chapter reading view. */
export function ReaderScreen() {
  return (
    <div className="absolute inset-0 font-inter text-[#1a1a1a]">
      <AppStatusBar />
      <Placed x={0} y={88} width={393} className="text-center">
        <div className="text-[12.5px] leading-[18px] text-[#444]">{chapter.eyebrow}</div>
        <div className="mt-[5px] text-[17px] leading-[19px] font-semibold tracking-[-0.01em] text-[#111]">
          {chapter.title.map((l) => (
            <div key={l}>{l}</div>
          ))}
        </div>
      </Placed>

      <Placed x={23} y={197} width={346} className="text-[16px] font-[450] tracking-[-0.025em] text-[#111]">
        <span className="absolute top-[-28px] left-[0px] font-times text-[58px] leading-[58px] text-[#111]">{chapter.dropCap}</span>
        {chapter.lines.map((l, i) => (
          <TextLine key={l} text={l} indent={i === 0 ? 26 : 0} />
        ))}
        <div className="opacity-60 blur-[2.2px]">
          {chapter.faded.map((l, i) => (
            <div key={l} style={{ height: LINE, lineHeight: `${LINE}px`, textAlign: i === 0 ? 'justify' : 'left', textAlignLast: i === 0 ? 'justify' : 'auto' }}>
              {l}
            </div>
          ))}
        </div>
      </Placed>

      <Placed x={26} y={764}>
        <ReaderControls {...player} />
      </Placed>
      <Placed x={186} y={820} className="text-[#222]">
        <ChevronDown size={21} strokeWidth={1.8} />
      </Placed>
    </div>
  )
}
