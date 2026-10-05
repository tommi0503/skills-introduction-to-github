/** Small white uppercase label sitting on gradient cards. */
export function TagPill({ children, width }: { children: string; width: number }) {
  return (
    <span
      className="flex h-[24px] items-center justify-center rounded-full bg-white/80 text-[9.5px] font-semibold tracking-[0.2px] text-[#4a4a50] uppercase"
      style={{ width }}
    >
      {children}
    </span>
  )
}
