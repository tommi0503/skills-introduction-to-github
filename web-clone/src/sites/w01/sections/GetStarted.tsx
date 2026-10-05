import { Megaphone } from 'lucide-react'
import { Button } from '../components/Button'
import { Column } from '../components/Column'
import { getStarted } from '../data'
import { serifStyle, theme } from '../theme'

export function GetStarted() {
  const border = `1px solid ${theme.rule}`
  return (
    <Column height={492}>
      <h2 className={`${theme.fonts.serif} absolute left-[48px] top-[56px]`} style={{ ...serifStyle(26), color: theme.ink }}>
        {getStarted.title}
      </h2>
      <div className="absolute inset-x-0 top-[145px] flex h-[244px]" style={{ borderTop: border, borderBottom: border }}>
        {getStarted.columns.map((c, i) => (
          <div key={c.title} className="flex-1 px-[48px] pt-[42px]" style={{ borderLeft: i ? border : undefined }}>
            <p className="text-[20px] leading-[26px] font-medium" style={{ color: theme.ink }}>{c.title}</p>
            <p className="mt-[4px] w-[543px] text-[18px] leading-[23.4px]" style={{ color: theme.muted }}>{c.body}</p>
            <Button variant={c.cta.variant} className="mt-[30px]">{c.cta.label}</Button>
          </div>
        ))}
      </div>
      <div className="absolute inset-x-0 top-[389px] flex h-[103px] items-center px-[48px]" style={{ background: theme.panel }}>
        <p className="text-[20px] leading-[26px] font-medium" style={{ color: theme.ink }}>{getStarted.hiring.title}</p>
        <Megaphone className="ml-[8px] h-[28px] w-[40px] -rotate-12" style={{ color: theme.green }} fill={theme.green} />
        <p className="ml-auto text-[16px] leading-5" style={{ color: theme.ink }}>{getStarted.hiring.body}</p>
        <Button variant="outline" className="ml-[16px]">{getStarted.hiring.cta}</Button>
      </div>
    </Column>
  )
}
