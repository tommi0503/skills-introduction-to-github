export function PageDots({ count, active, top }: { count: number; active: number; top: number }) {
  return (
    <div className="absolute flex gap-[10.5px]" style={{ left: 157, top }}>
      {Array.from({ length: count }, (_, i) => (
        <span key={i} className="h-[6.5px] w-[6.5px] rounded-full bg-white" style={{ opacity: i === active ? 1 : 0.55 }} />
      ))}
    </div>
  )
}
