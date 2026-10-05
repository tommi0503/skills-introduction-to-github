import { ImagePlaceholder, cn } from '../../../ui'
import { innovation } from '../data'

export function Innovation() {
  return (
    <section className="px-8 pt-[160px]">
      <h2 className="text-[32px] font-medium leading-[35.2px] tracking-[-0.32px] text-[#0f0e0d]">{innovation.title}</h2>
      <div className="mt-[64px] flex justify-between">
        <ul className="w-[550px]">
          {innovation.tabs.map((tab) => (
            <li
              key={tab.label}
              className={cn(
                'h-[193px] pt-[20px]',
                tab.active ? 'border-t-2 border-[#0f0e0d] text-[#0f0e0d]' : 'border-t border-[#cccac6] text-[#706d66]',
              )}
            >
              <h3 className="text-[24px] font-medium leading-[31.2px] tracking-[-0.24px]">{tab.label}</h3>
            </li>
          ))}
        </ul>
        <ImagePlaceholder label="Agents product screenshot" className="h-[517px] w-[688px] rounded-[8px]" />
      </div>
    </section>
  )
}
