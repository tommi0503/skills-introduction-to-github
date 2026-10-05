import { Star } from 'lucide-react'

export function RatingRow({ stars, label }: { stars: number; label: string }) {
  return (
    <div className="flex items-center gap-[8px]">
      <div className="flex gap-[1px]">
        {Array.from({ length: stars }, (_, i) => (
          <Star key={i} size={15} fill="#f4c542" stroke="#f4c542" />
        ))}
      </div>
      <span className="text-[15.5px] text-[#111]">{label}</span>
    </div>
  )
}
