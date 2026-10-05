import { CircleX } from 'lucide-react'

/** Grey filled circular "×" used to clear an input. */
export function ClearButton({ size = 22 }: { size?: number }) {
  return <CircleX size={size} strokeWidth={2.2} color="#fff" fill="#8c8c8e" />
}
