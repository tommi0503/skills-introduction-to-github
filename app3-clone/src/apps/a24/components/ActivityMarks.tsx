import { theme } from '../theme'

/** Pairs of tiny habit glyphs under a date: a rose ring followed by a blue disc. */
export function ActivityMarks({ count }: { count: number }) {
  return (
    <div className="flex">
      {Array.from({ length: count }, (_, i) =>
        i % 2 === 0 ? (
          <span key={i} className="size-[10px] rounded-full border-[2px]" style={{ borderColor: theme.roseLight, marginLeft: i ? -1 : 0 }} />
        ) : (
          <span key={i} className="relative -ml-[1px] size-[10px] rounded-full" style={{ background: theme.markBlue }}>
            <span className="absolute left-[2px] top-[2.5px] size-[4px] rounded-full bg-white/80" />
          </span>
        ),
      )}
    </div>
  )
}
