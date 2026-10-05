export function SignupTitle({ lines, top }: { lines: string[]; top: number }) {
  return (
    <h1
      className="absolute inset-x-0 text-center font-times text-[33px] leading-[35px] font-normal tracking-[-0.1px] text-[#3a3a3a]"
      style={{ top }}
    >
      {lines.map((l) => (
        <span key={l} className="block">
          {l}
        </span>
      ))}
    </h1>
  )
}
