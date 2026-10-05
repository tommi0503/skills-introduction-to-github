import { theme } from '../theme'

/** Label + filled input (visual only). */
export function FormField({ label, placeholder }: { label: string; placeholder: string }) {
  return (
    <div>
      <div className="text-[12px] tracking-[-0.3px]" style={{ color: theme.ink }}>
        {label}
      </div>
      <div
        className="mt-[8px] flex h-[42px] items-center rounded-[12px] px-[16px] text-[12px] tracking-[-0.3px]"
        style={{ background: theme.field, color: '#a5a5a5' }}
      >
        {placeholder}
      </div>
    </div>
  )
}
