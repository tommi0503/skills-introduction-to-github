import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { thanks as T } from './data'

const Thanks = () => (
  <Slide className="font-poppins">
    <ImagePlaceholder className="absolute inset-0" label="gradient background with logo watermark" />
    <Abs x={889} y={64} w={262} h={108} className="rounded-[18px] bg-[#5df07a] px-[18px] pt-[14px] text-[34px] font-semibold leading-[38px] text-black">
      {T.sticker.map((l) => <div key={l}>{l}</div>)}
    </Abs>
    <Abs x={1021} y={192} w={185} h={54} className="flex items-center justify-center rounded-[8px] bg-[#8b6bf5] text-[27px] font-bold text-[#e8e1ff]">{T.tag}</Abs>
    <ImagePlaceholder className="absolute rounded-full" tone="#c9ccd2" style={{ left: 53, top: 424, width: 60, height: 60 }} label="logo" />
    <Abs x={134} y={430} className="text-[29px] font-medium text-[#0d1f12]">{T.brand}</Abs>
    <Abs x={52} y={518} className="text-[124px] font-semibold leading-[150px] tracking-[-0.02em] text-[#1c4a14]">{T.title}</Abs>
  </Slide>
)

const deck: DeckDefinition = { id: '19', title: 'Framewave Thank You', slides: [Thanks] }
export default deck
