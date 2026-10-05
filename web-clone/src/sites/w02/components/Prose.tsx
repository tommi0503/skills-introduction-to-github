import { cn } from '../../../ui'
import { theme } from '../theme'

/** Grey paragraph with an optional ink lead-in and trailing dotted link. */
export function Prose({ strong, rest, more, className }: { strong?: string; rest: string; more?: string; className?: string }) {
  return (
    <p className={cn(className)} style={{ color: theme.grey }}>
      {strong && <span style={{ color: theme.ink }} className="font-[450]">{strong} </span>}
      {rest}
      {more && (
        <>
          {' '}
          <span className="font-medium underline decoration-dotted decoration-1 underline-offset-[5px]" style={{ color: theme.link }}>{more}</span>
        </>
      )}
    </p>
  )
}
