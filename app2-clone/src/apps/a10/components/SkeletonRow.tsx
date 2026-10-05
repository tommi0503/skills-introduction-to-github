/** Blurred loading placeholder for an airport row (pure UI shapes). */
const bar = 'absolute rounded-full bg-[#ebebed]'

export function SkeletonRow({ height = 107 }: { height?: number }) {
  const cols = [119, 194, 286]
  return (
    <div className="relative" style={{ height }}>
      <div className="absolute -top-[3px] left-[23px] h-[38px] w-[38px] rounded-full bg-[#d4d4d6] blur-[3px]" />
      <div className="absolute top-[25px] left-[51px] h-[18px] w-[18px] rounded-full bg-[#ececee] blur-[2px]" />
      <div className={`${bar} top-[57px] left-[37px] h-[9px] w-[22px] blur-[1.5px]`} />
      <div className={`${bar} -top-[6px] left-[96px] h-[14px] w-[132px] blur-[1.5px]`} />
      {[38, 53].map((top) => (
        <div key={top}>
          <div className={`${bar} left-[97px] h-[8px] w-[8px] blur-[1px]`} style={{ top }} />
          {cols.map((left) => (
            <div key={left} className={`${bar} h-[10px] w-[45px] blur-[1.5px]`} style={{ top, left: left - 7 }} />
          ))}
        </div>
      ))}
      <div className="absolute top-[85px] right-0 left-[96px] h-px bg-[#efeff1]" />
    </div>
  )
}
