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
      className="whitespace-nowrap font-inter text-[200px] font-bold leading-none tracking-[-6px]"
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
        <span className="flex h-[24px] w-[24px] items-center justify-center rounded-full bg-white/60">
          <ImagePlaceholder label="Ethereum logo" className="h-[14px] w-[14px] rounded-full" />
        </span>
        <span className="text-[9.5px] font-medium text-[#1c1c1e]">{coin.name}</span>
      </div>
      <div className="mt-[8px] text-[20px] leading-[24px] text-[#1c1c1e]">{coin.price}</div>
      <div className="mt-[2px] text-[12.5px] leading-[16px]" style={{ color: theme.cryptoPositive }}>
        {coin.change}
      </div>
    </div>
  )
}
