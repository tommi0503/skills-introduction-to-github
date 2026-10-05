import { ChevronDown } from 'lucide-react'
import { brand, navActions, navItems } from '../data'
import { Serif } from '../components/Type'

export function NavBar() {
  return (
    <header className="flex h-[82px] items-center bg-[#0f0e0d] px-8 text-[14px] font-medium text-[#fafaf9]">
      <Serif as="div" className="-mt-[1px] w-[117px] text-[30px] leading-[39px] tracking-[-0.2px]">
        {brand}
      </Serif>
      <nav className="flex items-center gap-8">
        {navItems.map((item) => (
          <span key={item.label} className="flex items-center gap-1 leading-[18.2px]">
            {item.label}
            {item.hasMenu && <ChevronDown className="size-4" strokeWidth={2} />}
          </span>
        ))}
      </nav>
      <div className="ml-auto flex items-center gap-4">
        <span className="flex h-8 w-[78px] items-center justify-center gap-1 rounded-[3px] border border-[#fafaf9]/90">
          {navActions.login}
          <ChevronDown className="size-4" strokeWidth={2} />
        </span>
        <span className="flex h-8 w-[127px] items-center justify-center rounded-[3px] bg-[#fafaf9] text-[#0f0e0d]">
          {navActions.demo}
        </span>
      </div>
    </header>
  )
}
