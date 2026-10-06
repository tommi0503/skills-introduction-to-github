import type { DeckDefinition } from '../../ui'
import { Frame, Ph, Pixel, T } from './components'
import { brand, cover, market } from './data'
import { theme } from './theme'

function Cover() {
  return (
    <Frame k={theme.k1} bg="#fff">
      <Ph x={97} y={0} w={384} h={94} radius="0 0 0 20px" tone="#eceef0" />
      <Ph x={0} y={94} w={97} h={176} radius="0 22px 0 0" tone="#6bb6d6" />
      <Ph x={249} y={247} w={232} h={23} radius="22px 0 0 0" tone="#7e9df0" />
      <Ph x={20} y={14} w={17} h={14} radius="3px" />
      <T x={43} y={15} className="text-[9px] font-bold" style={{ color: '#134e5a' }}>{brand}</T>
      <T x={132} y={17} className="text-[5px]">{cover.header[0]}</T>
      <T x={243} y={17} className="text-[5px]">{cover.header[1]}</T>
      <T x={420} y={17} className="text-[5px]">{cover.header[2]}</T>
      <Ph x={37} y={151} w={65} h={83} radius="8px" tone="#d1d5db" />
      <Pixel x={133} y={125} size={40} lh={40}>{cover.title.map((l) => <div key={l}>{l}</div>)}<div style={{ color: theme.sky }}>{cover.accent}</div></Pixel>
    </Frame>
  )
}
function Market() {
  const { ai, growth } = market
  return (
    <Frame k={theme.k2} bg="#f3f5f8">
      <T x={19} y={9} className="text-[5px]">{market.kicker}</T>
      <T x={461} y={9} className="text-[5px]" style={{ transform: 'translateX(-100%)' }}>{market.url}</T>
      <Pixel x={22} y={29} size={20} lh={21}>{market.title}<div style={{ color: theme.sky }}>{market.accent}</div></Pixel>
      <T x={20} y={98} w={96} h={49} className="flex flex-col items-center justify-center rounded-[8px] bg-white text-center text-[5.5px] font-bold leading-[7px]">{ai.label.map((l) => <div key={l}>{l}</div>)}</T>
      <T x={116} y={147} w={122} h={103} className="rounded-[8px] bg-white">
        <div className="absolute font-spacemono text-[24px] font-bold" style={{ left: 12, top: 28 }}>{ai.value}<span className="text-[14px]" style={{ color: theme.sky }}>✧</span></div>
        <div className="absolute text-[4px]" style={{ left: 12, top: 78 }}>{ai.year}</div>
      </T>
      <T x={23} y={177} w={86} className="text-[4px] leading-[5.5px]">{ai.body}</T>
      <T x={365} y={48} w={96} h={48} className="flex flex-col items-center justify-center rounded-[8px] text-center text-[6px] font-bold leading-[8px]" style={{ background: theme.mint }}>
        <div>{growth.label.map((l) => <div key={l}>{l}</div>)}</div>
      </T>
      <Ph x={244} y={98} w={121} h={152} radius="0 0 8px 8px" tone="#74b2e6" />
      <T x={256} y={126} className="whitespace-nowrap font-spacemono text-[24px] font-bold text-white">{growth.value}<span className="text-[14px]">✧</span></T>
      <T x={256} y={176} className="text-[4px] text-white">{growth.year}</T>
      <Ph x={337} y={199} w={50} h={43} radius="6px" tone="#d1d5db" />
      <T x={379} y={125} w={80} className="text-[4px] leading-[5.5px]">{growth.body}</T>
    </Frame>
  )
}
const deck: DeckDefinition = { id: '11', title: 'Synth NFT pitch', slides: [Cover, Market] }
export default deck
