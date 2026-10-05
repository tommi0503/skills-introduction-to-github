import { ImagePlaceholder, Panel, Placed, VerticalText } from '../../../ui'
import { bubbles, faces, testimonialsPanel as d } from '../data'
import { theme } from '../theme'
import { Lines } from '../components/Lines'
import { SpeechBubble } from '../components/SpeechBubble'

/** Panel 3 — blue panel with brand line, speech-bubble testimonials and opening hours card. */
export function TestimonialsPanel() {
  return (
    <Panel background={theme.sky}>
      <Placed x={0} y={72} width={490}>
        <Lines lines={d.heading} className="text-center text-[23px] font-semibold leading-[38px] text-[#1e1e1e]" />
      </Placed>
      <Placed x={0} y={148} width={490} className="text-center font-poppins text-[41px] font-bold leading-[44px] tracking-[0.01em] text-white">
        {d.brand.pre}
        <span className="font-hi-melody text-[52px] font-normal">{d.brand.script}</span>
        {d.brand.post}
      </Placed>
      <Placed x={0} y={200} width={490}>
        <Lines lines={d.slogan} className="text-center font-poppins text-[20px] leading-[29px] text-[#1e1e1e]" />
      </Placed>
      {bubbles.map((b) => (
        <SpeechBubble key={b.key} bubble={b} fill={theme.bubble} textClassName="text-[16.5px] font-medium leading-[26.5px] text-[#4f88cf]" />
      ))}
      {faces.map((f, i) => (
        <Placed key={i} x={f.x} y={f.y} width={f.w} height={f.h}>
          <ImagePlaceholder label="face illustration" className="h-full w-full rounded-[45%]" />
        </Placed>
      ))}
      <Placed x={52} y={738} width={262} height={207} className="rounded-[28px]" style={{ background: theme.card }}>
        <ImagePlaceholder label="JOYFUL logo" className="absolute left-[38px] top-[32px] h-[68px] w-[120px] rounded-[6px]" />
        <div className="absolute left-[201px] top-[30px] flex h-[80px] w-[30px] items-center justify-center rounded-full text-white" style={{ background: theme.sky }}>
          <VerticalText mode="rotate" className="font-poppins rotate-180 text-[12px] font-semibold">{d.badge}</VerticalText>
        </div>
        <Lines lines={d.schedule} className="absolute left-[38px] top-[122px] font-poppins text-[15.5px] leading-[26px] text-[#1e1e1e]" />
      </Placed>
      <Placed x={343} y={750} width={86} height={80}>
        <ImagePlaceholder label="flower shape" className="h-full w-full rounded-full" tone="#e8edf3" />
      </Placed>
      <Placed x={343} y={855} width={86} height={82}>
        <ImagePlaceholder label="leaf shape" className="h-full w-full rounded-[50%_50%_40%_40%]" tone="#e8edf3" />
      </Placed>
    </Panel>
  )
}
