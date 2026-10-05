import { BriefcasePlus, MapPin, UtensilsCrossed, Footprints } from 'lucide-react'
import type { ReactNode } from 'react'
import { AppScreen, ImagePlaceholder } from '../../../ui'
import { BottomPanel } from '../components/BottomPanel'
import { MenuGlyph } from '../components/MenuGlyph'
import { PhotoTile } from '../components/PhotoTile'
import { TopBar } from '../components/TopBar'
import { home, type Tile } from '../data'

const TILE = { w: 197, h: 188, gap: 17, left: 22 }

function TileRow({ tiles, top, render }: { tiles: Tile[]; top: number; render: (t: Tile, i: number) => ReactNode }) {
  return (
    <div className="absolute flex" style={{ left: TILE.left, top, gap: TILE.gap }}>
      {tiles.map((t, i) => render(t, i))}
    </div>
  )
}

function SectionLabel({ top, children }: { top: number; children: ReactNode }) {
  return (
    <div className="absolute inset-x-[22px] flex items-center justify-between text-[16px] font-semibold" style={{ top }}>
      {children}
    </div>
  )
}

export function HomeScreen() {
  const metaIcon = [UtensilsCrossed, Footprints]
  return (
    <AppScreen className="font-inter">
      <TopBar />
      <MenuGlyph x={22} y={72} />
      <ImagePlaceholder className="absolute rounded-[4px]" style={{ left: 127, top: 68, width: 135, height: 27 }} label="mindtrip logo" />
      <BriefcasePlus size={21} strokeWidth={1.7} className="absolute" style={{ left: 347, top: 70 }} />
      <SectionLabel top={124}>{home.getStarted}</SectionLabel>
      <TileRow
        tiles={home.starters}
        top={158}
        render={(t) => (
          <PhotoTile key={t.key} width={TILE.w} height={TILE.h}>
            <span className="text-[15px] font-semibold">{t.title}</span>
          </PhotoTile>
        )}
      />
      <SectionLabel top={373}>
        <span className="flex items-center gap-[4px]">
          {home.forYouPrefix}
          <MapPin size={14} strokeWidth={1.8} />
          {home.forYouPlace}
        </span>
        <span className="text-[15px] font-normal text-[#8e8e93]">{home.explore}</span>
      </SectionLabel>
      <TileRow
        tiles={home.forYou}
        top={406}
        render={(t, i) => {
          const Icon = metaIcon[i]
          return (
            <PhotoTile key={t.key} width={TILE.w} height={TILE.h} actions={t.actions}>
              <div className="flex flex-col whitespace-nowrap">
                {t.title && <span className="text-[14.5px] leading-[18px] font-semibold">{t.title}</span>}
                {t.lines?.map((l) => (
                  <span key={l} className="text-[14.5px] leading-[16px] font-semibold">
                    {l}
                  </span>
                ))}
                <span className="mt-[2px] flex items-center gap-[3px] text-[11.5px] opacity-90">
                  <Icon size={10} strokeWidth={2} />
                  {t.meta}
                </span>
              </div>
            </PhotoTile>
          )
        }}
      />
      <SectionLabel top={621}>{home.getInspired}</SectionLabel>
      <TileRow
        tiles={home.starters}
        top={654}
        render={(t) => <PhotoTile key={t.key} width={TILE.w} height={TILE.h} />}
      />
      <BottomPanel active="home" top={700} />
    </AppScreen>
  )
}
