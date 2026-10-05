import { ChevronDown } from 'lucide-react'
import { AppScreen, ImagePlaceholder, cn } from '../../../ui'
import { PhoneStatus } from '../components/PhoneStatus'
import { RoundAction } from '../components/RoundAction'
import { article, bookmarkIcon, shareActions } from '../data'

export function ArticleScreen() {
  return (
    <AppScreen className="font-figtree">
      <PhoneStatus />
      <div className="absolute top-[78px] left-[19px] flex w-[350px] gap-[5px]">
        {Array.from({ length: article.steps }, (_, i) => (
          <span key={i} className={cn('h-[3px] flex-1 rounded-full', i === article.step ? 'bg-[#111]' : 'bg-[#e9e9e9]')} />
        ))}
      </div>
      <div className="absolute top-[104px] left-[19px] flex h-[34px] w-[34px] items-center justify-center rounded-full bg-[#efefef]">
        <ChevronDown size={18} strokeWidth={3} />
      </div>
      <div className="absolute inset-x-0 top-[102px] flex flex-col items-center">
        <span className="text-[14.5px] leading-[18px] font-semibold text-[#111]">{article.title}</span>
        <span className="mt-[3px] text-[11px] leading-[14px] font-medium text-[#555]">
          {article.category} &nbsp;·&nbsp; {article.duration}
        </span>
      </div>
      <h1 className="absolute top-[166px] left-[22px] font-playfair text-[31px] leading-[40px] font-medium text-[#111]">{article.heading}</h1>
      <p className="absolute top-[239px] left-[22px] w-[346px] font-jakarta text-[17.1px] leading-[22.9px] tracking-[0.2px] text-[#222]">{article.body}</p>
      <ImagePlaceholder label="watermelon moon illustration" className="absolute top-[452px] left-[7px] h-[281px] w-[373px] rounded-[28px]" />
      <RoundAction action={{ key: 'bookmark', icon: bookmarkIcon }} size={60} className="absolute top-[742px] left-[19px] bg-[#f0f0f0] text-[#111]" iconSize={19} />
      <div className="absolute top-[742px] left-[169px] flex gap-[9px]">
        {shareActions.map((a) => (
          <RoundAction key={a.key} action={a} size={60} iconSize={19} className="bg-[#f0f0f0] text-[#111]" markTone="#bdbdbd" />
        ))}
      </div>
    </AppScreen>
  )
}
