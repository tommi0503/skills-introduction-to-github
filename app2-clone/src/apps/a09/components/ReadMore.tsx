import { cn } from '../../../ui'

/** Paragraph ending with an underlined "More" link. */
export function ReadMore({ text, more, className }: { text: string; more: string; className?: string }) {
  return (
    <p className={cn(className)}>
      {text} <span className="font-semibold text-[#222325] underline underline-offset-[2px]">{more}</span>
    </p>
  )
}
