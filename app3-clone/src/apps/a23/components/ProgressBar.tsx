export function ProgressBar({ value, color, track, height }: { value: number; color: string; track: string; height: number }) {
  return (
    <div className="w-full rounded-full" style={{ height, background: track }}>
      <div className="h-full rounded-full" style={{ width: `${value * 100}%`, background: color }} />
    </div>
  )
}
