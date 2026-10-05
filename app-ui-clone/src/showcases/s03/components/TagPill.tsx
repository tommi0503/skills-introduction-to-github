/** Small white uppercase label sitting on gradient cards. */
export function TagPill({ children, width }: { children: string; width: number }) {
  return (
    <span
      className="flex h-[24px] items-center rounded-full pl-[10px] bg-white/80 text-[10.3px] font-semibold tracking-[0.2px] text-[#3e3e44] uppercase"
      style={{ width }}
    >
      {children}
    </span>
  )
}
