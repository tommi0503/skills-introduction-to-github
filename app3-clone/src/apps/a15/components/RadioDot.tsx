export function RadioDot({ checked, color }: { checked: boolean; color: string }) {
  return (
    <span
      className="block shrink-0 rounded-full bg-white"
      style={{ width: 24, height: 24, border: checked ? `8px solid ${color}` : '1.5px solid #8c8c8c' }}
    />
  )
}
