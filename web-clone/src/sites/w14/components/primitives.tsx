import type { CSSProperties, ReactNode } from 'react'
import type { LucideIcon } from 'lucide-react'
import { ArrowRight } from 'lucide-react'
import { cn } from '../../../ui'
import { colors, fonts, shadows } from '../theme'

type Variant = 'dark' | 'light' | 'nav'

const variantStyle: Record<Variant, CSSProperties> = {
  dark: { background: colors.ink, color: '#fff' },
  light: { background: colors.border, color: colors.ink },
  nav: { background: colors.navButton, color: colors.muted },
}

export interface PillButtonProps {
  children: ReactNode
  variant?: Variant
  arrow?: boolean
  leading?: ReactNode
  className?: string
  style?: CSSProperties
}

/** Rounded CTA pill used throughout the page (16px label, optional arrow). */
export function PillButton({ children, variant = 'dark', arrow, leading, className, style }: PillButtonProps) {
  return (
    <span
      className={cn(
        'inline-flex h-[38px] items-center rounded-full px-[14px] text-[16px] leading-[16px] font-semibold tracking-[-0.48px] whitespace-nowrap',
        fonts.sans,
        className,
      )}
      style={{ ...variantStyle[variant], ...style }}
    >
      {leading}
      {children}
      {arrow && <ArrowRight className="ml-[11px]" size={15} strokeWidth={1.8} />}
    </span>
  )
}

/** 44px square tile holding a 24px icon (feature cards / enterprise list). */
export function IconTile({ icon: Icon, children, className }: { icon?: LucideIcon | null; children?: ReactNode; className?: string }) {
  return (
    <div
      className={cn('flex h-[46px] w-[46px] items-center justify-center rounded-[8px]', className)}
      style={{ background: colors.subtle, boxShadow: shadows.tile }}
    >
      {Icon ? <Icon size={22} strokeWidth={1.6} color={colors.ink} /> : children}
    </div>
  )
}

/** Small grey pill with a bold label (feature card footer). */
export function Chip({ children, className }: { children: ReactNode; className?: string }) {
  return (
    <span
      className={cn(
        'inline-flex h-[36px] items-center rounded-full px-[14px] text-[16px] leading-[16px] font-semibold tracking-[-0.48px]',
        fonts.sans,
        className,
      )}
      style={{ background: colors.chip, color: colors.ink }}
    >
      {children}
    </span>
  )
}

export type TextRole = 'h1' | 'h2' | 'h2lg' | 'h3' | 'lead' | 'body' | 'card'

const textRole: Record<TextRole, string> = {
  h1: 'text-[45px] leading-[45px] tracking-[-0.7px] font-[560]',
  h2lg: 'text-[38px] leading-[38px] tracking-[-0.4px] font-[560]',
  h2: 'text-[32px] leading-[38.4px] tracking-[-0.64px] font-[560]',
  h3: 'text-[20px] leading-[26px] tracking-[-0.4px] font-semibold',
  lead: 'text-[18px] leading-[28.8px] tracking-[-0.18px] font-medium',
  body: 'text-[16px] leading-[24px] font-[450]',
  card: 'text-[24px] leading-[28.8px] tracking-[-0.48px] font-[500]',
}

const roleColor: Record<TextRole, string> = {
  h1: colors.ink,
  h2: colors.ink,
  h2lg: colors.ink,
  h3: colors.ink,
  card: colors.ink,
  lead: colors.body,
  body: colors.body,
}

/** Typography primitive mapping a semantic role to the reference metrics. */
export function Text({
  role,
  as: Tag = 'p',
  className,
  style,
  children,
}: {
  role: TextRole
  as?: 'p' | 'h1' | 'h2' | 'h3' | 'h4' | 'h5' | 'span' | 'div'
  className?: string
  style?: CSSProperties
  children: ReactNode
}) {
  return (
    <Tag className={cn(fonts.sans, textRole[role], className)} style={{ color: roleColor[role], ...style }}>
      {children}
    </Tag>
  )
}

/** Renders an array of lines with explicit breaks (matching the reference wrapping). */
export function Lines({ lines }: { lines: string[] }) {
  return (
    <>
      {lines.map((l, i) => (
        <span key={i} className="block">
          {l}
        </span>
      ))}
    </>
  )
}
