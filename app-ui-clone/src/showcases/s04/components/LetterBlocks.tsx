export interface LetterBlock {
  key: string
  x: number
  slotX: number
  /** Override the corner radius (e.g. the rounder bowl of a "D"). */
  radius?: string
}

export interface LetterBlocksProps {
  blocks: LetterBlock[]
  top: number
  width: number
  height: number
  radius?: number
}

/** Big outlined, semi-transparent letter shapes behind the phones (decorative "FOOD"). */
export function LetterBlocks({ blocks, top, width, height, radius = 22 }: LetterBlocksProps) {
  return (
    <>
      {blocks.map((b) => (
        <div
          key={b.key}
          className="absolute"
          style={{
            left: b.x,
            top,
            width,
            height,
            borderRadius: b.radius ?? radius,
            border: '1.5px solid rgba(255,224,196,0.85)',
            background: 'linear-gradient(180deg, rgba(255,255,255,0.22) 0%, rgba(255,255,255,0.14) 55%, rgba(255,255,255,0) 100%)',
          }}
        >
          <div
            className="absolute"
            style={{
              left: b.slotX,
              top: 46,
              width: 8,
              height: height,
              borderRadius: '4px 4px 0 0',
              border: '1.5px solid rgba(255,200,150,0.8)',
              background: '#ff5a0a',
            }}
          />
        </div>
      ))}
    </>
  )
}
