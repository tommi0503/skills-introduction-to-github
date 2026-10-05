import { ImagePlaceholder } from '../../../ui'
import type { ethereum } from '../data'
import { theme } from '../theme'

/** Lines of copy rendered as separate blocks (breaks come from data). */
export function Lines({ lines, className }: { lines: string[]; className?: string }) {
  return (
    <div className={className}>
      {lines.map((l) => (
        <div key={l}>{l}</div>
      ))}
    </div>
  )
}

/** Oversized faded word running off the bottom of the stage. */
export function BigWord({ word }: { word: string }) {
  return (
    <div
      className="whitespace-nowrap font-inter text-[200px] font-medium leading-none tracking-[-4px]"
      style={{ color: theme.bigWord }}
    >
      {word}
    </div>
  )
}

/** Floating crypto ticker card. */
export function CryptoCard({ coin }: { coin: typeof ethereum }) {
  return (
    <div className="h-[93px] w-[118px] rounded-[16px] px-[10px] pt-[11px] font-inter shadow-[0_6px_16px_rgba(90,60,160,0.12)]" style={{ background: theme.ethCard }}>
      <div className="flex items-center gap-[8px]">
        <span className="flex h-[23px] w-[23px] items-center justify-center rounded-full bg-white/70">
          <ImagePlaceholder label="Ethereum logo" className="h-[14px] w-[14px] rounded-full" />
        </span>
        <span className="text-[9.5px] text-[#1c1c1e]">{coin.name}</span>
      </div>
      <div className="mt-[8px] text-[20px] leading-[24px] text-[#1c1c1e]">{coin.price}</div>
      <div className="text-[12px] leading-[15px]" style={{ color: theme.positive }}>
        {coin.change}
      </div>
    </div>
  )
}
