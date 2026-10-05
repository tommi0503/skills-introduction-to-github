import { Bell, ChevronRight, Search, TextAlignStart } from 'lucide-react'
import { Avatar, ImagePlaceholder } from '../../../ui'
import { ArtworkCard } from '../components/ArtworkCard'
import { BlobNav } from '../components/BlobNav'
import { FadeText } from '../components/FadeText'
import { SoftCircleButton } from '../components/SoftCircleButton'
import { galleryScreen as d } from '../data'
import { theme } from '../theme'

function SectionTitle({ title, top }: { title: string; top: number }) {
  return (
    <div className="absolute right-[22px] left-[19px] flex items-center justify-between" style={{ top }}>
      <span className="text-[21.7px] font-semibold text-[#111]">{title}</span>
      <ChevronRight size={20} strokeWidth={2} />
    </div>
  )
}

export function GalleryScreen() {
  return (
    <div className="absolute inset-0">
      <div className="absolute top-[49px] left-[20px]">
        <FadeText gradient="linear-gradient(90deg, #c8c8c8, #8c8c8c)" className="text-[15px] leading-[19px]">
          {d.greeting}
        </FadeText>
        <br />
        <FadeText
          gradient="linear-gradient(90deg, #d0d0d0 0%, #9c9c9c 20%, #111 40%, #111 70%, #c4c4c4 100%)"
          className="mt-[1px] text-[22px] leading-[28px] font-medium"
        >
          {d.title}
        </FadeText>
      </div>
      <div className="absolute top-[52px] left-[252px] flex items-center gap-[15px]">
        <SoftCircleButton icon={TextAlignStart} size={54} iconSize={20} />
        <Avatar size={46} ring="2px solid #fff" />
      </div>

      {/* Search */}
      <div
        className="absolute top-[125px] left-[22px] flex h-[39px] w-[339px] items-center pr-[1.5px] pl-[9.5px]"
        style={{ background: 'linear-gradient(90deg, #f2f2f2, #f4f4f4 60%, #efefef)' }}
      >
        <Search size={17} strokeWidth={2} className="text-[#333]" />
        <FadeText gradient="linear-gradient(90deg, #b5b5b5, #cfcfcf)" className="ml-[12.5px] flex-1 text-[13px]">
          {d.search}
        </FadeText>
        <span className="relative flex h-[27px] w-[27px] items-center justify-center rounded-full bg-white">
          <Bell size={14} strokeWidth={1.8} />
          <span className="absolute top-[6px] right-[7px] h-[4px] w-[4px] rounded-full bg-[#e5484d]" />
        </span>
      </div>

      <SectionTitle title={d.forYou} top={209} />
      <div className="absolute top-[256px] left-[18px] flex gap-[19px]">
        {d.artworks.map((a) => (
          <ArtworkCard key={a.key} art={a} />
        ))}
      </div>

      <SectionTitle title={d.categories} top={678} />
      <div className="absolute top-[726px] left-[18px] flex gap-[19px]">
        {d.artworks.map((a) => (
          <div key={a.key} className="h-[120px] w-[233px] shrink-0 px-[26.5px] pt-[26.5px]" style={{ background: theme.card }}>
            <ImagePlaceholder className="h-full w-[179px]" label={`${a.title} category`} />
          </div>
        ))}
      </div>
      <div
        className="absolute right-0 bottom-0 left-0 h-[110px]"
        style={{ background: 'linear-gradient(180deg, rgba(255,255,255,0), #fdfdfd 85%)' }}
      />

      <div className="absolute top-[734px] left-[105px]">
        <BlobNav items={d.nav} activeKey={d.activeNav} />
      </div>
    </div>
  )
}
