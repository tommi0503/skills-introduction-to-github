import { Ellipsis, UserPlus } from 'lucide-react'
import { ImagePlaceholder } from '../../../ui'
import { HighlightStatusBar } from '../components/HighlightStatusBar'
import { NavHeader } from '../components/NavHeader'
import { detail, members, type Member } from '../data'
import { bond } from '../theme'

function MemberAvatar({ member }: { member: Member }) {
  const base = 'flex h-[47.5px] w-[47.5px] shrink-0 items-center justify-center rounded-full'
  switch (member.kind) {
    case 'photo':
      return (
        <div className="relative">
          <ImagePlaceholder label="avatar" className="h-[47.5px] w-[47.5px] rounded-full" />
          <span className="absolute -right-[1px] -bottom-[1px] h-[15px] w-[15px] rounded-full border-[2px] border-white bg-[#111]" />
        </div>
      )
    case 'initials':
      return <div className={`${base} bg-[#e8e8e8] text-[15.5px] text-[#444]`}>{member.initials}</div>
    case 'invite':
      return (
        <div className={`${base} bg-[#eeeeee] text-[#aaa]`}>
          <UserPlus size={16} strokeWidth={1.4} />
        </div>
      )
  }
}

function MemberRow({ member }: { member: Member }) {
  return (
    <div className="flex h-[68px] items-center">
      <MemberAvatar member={member} />
      <span className="ml-[13px] flex-1 text-[16px] font-medium text-[#111]" style={{ letterSpacing: -0.2 }}>
        {member.name}
      </span>
      {member.action && (
        <>
          <span className="flex h-[34px] items-center rounded-full bg-[#ececec] px-[11px] text-[15.5px] font-medium text-[#222]">
            {member.action}
          </span>
          <Ellipsis size={16} strokeWidth={1.6} className="mr-[6px] ml-[13px] text-[#555]" />
        </>
      )}
    </div>
  )
}

export function DetailScreen() {
  return (
    <div className="relative h-full font-inter" style={{ background: bond.screen }}>
      <HighlightStatusBar />
      <NavHeader center={<span className="text-[16px] font-semibold text-[#111]">{detail.title}</span>} />

      <div
        className="absolute rounded-[22px] bg-white"
        style={{ left: 16, top: 134, width: 360, height: 167, boxShadow: '0 4px 18px rgba(0,0,0,0.05)' }}
      >
        <div className="flex gap-[14px] pt-[15px] pl-[22px]">
          <span className="text-[26px] leading-[30px] opacity-60">{detail.emoji}</span>
          <h2 className="w-[215px] text-[20.6px] leading-[26px] font-medium text-[#111]" style={{ letterSpacing: -0.5 }}>
            {detail.heading}
          </h2>
        </div>
        <div className="mx-[18.5px] mt-[16px] h-px bg-[#e4e4e4]" />
        <div className="mt-[16px] flex flex-col gap-[11px] pl-[22px] text-[13.5px] leading-[19px] text-[#666]">
          {detail.meta.map((m) => (
            <span key={m}>{m}</span>
          ))}
        </div>
      </div>

      <p className="absolute text-[13.5px] text-[#8c8c8c]" style={{ left: 20.5, top: 342 }}>
        {detail.membersLabel}
      </p>
      <div className="absolute" style={{ left: 20, right: 16, top: 369 }}>
        {members.map((m) => (
          <MemberRow key={m.id} member={m} />
        ))}
      </div>
    </div>
  )
}
