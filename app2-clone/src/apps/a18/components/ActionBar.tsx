import type { NavItem } from '../data'

/** Viewer bottom actions: icon above label, evenly spread. */
export function ActionBar({ items }: { items: NavItem[] }) {
  return (
    <div className="absolute inset-x-[2px] top-[752px] flex justify-between px-[4px]">
      {items.map(({ key, label, icon: Icon }) => (
        <div key={key} className="flex w-[76px] flex-col items-center gap-[7px] text-[#1f1f1f]">
          <Icon size={21} strokeWidth={1.5} />
          <span className="text-[14px]">{label}</span>
        </div>
      ))}
    </div>
  )
}
