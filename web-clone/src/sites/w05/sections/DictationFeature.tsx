import { ImagePlaceholder, cn } from '../../../ui'
import { dictationFeature, showcases, type Showcase } from '../data'
import { theme } from '../theme'
import { IconTile } from '../components/IconTile'

/** Column-relative x positions (block starts at page x 120). */
const RAIL_X = 58
const LIST_X = 41
const MOCK_X = 430

function AppList() {
  return (
    <div
      className="absolute flex w-[260px] flex-col gap-[8px] rounded-[16px] p-[9px]"
      style={{ left: LIST_X, top: 287, background: '#2c2c2c', boxShadow: 'inset 0 1px 0 #414141, 0 0 0 1px #121212' }}
    >
      {dictationFeature.apps.map((app, i) => (
        <div
          key={app}
          className={cn('flex h-[48px] items-center gap-[12px] rounded-[8px] px-[16px] text-[16px] tracking-[-0.16px] text-white')}
          style={i === 0 ? { background: '#3e3e3e' } : undefined}
        >
          <ImagePlaceholder label={`${app} app icon`} className="size-5 rounded-[4px]" />
          {app}
        </div>
      ))}
    </div>
  )
}

function ShowcaseItem({ item }: { item: Showcase }) {
  return (
    <div className="absolute" style={{ left: MOCK_X, top: item.top }}>
      <ImagePlaceholder label="app mockup" tone={theme.media} className="h-[561px] w-[698px] rounded-[20px]" />
      {item.title && (
        <div className="ml-[-27px] mt-[39px] w-[652px]">
          <h3 className={`${theme.serif} flex items-center gap-[8px] text-[24px] font-bold leading-6 tracking-[-0.72px]`} style={{ color: theme.ink }}>
            {item.title}
            <ImagePlaceholder label="app icon" className="rounded-[4px]" style={{ width: item.iconSize, height: item.iconSize }} />
          </h3>
          <p className="mt-[10px] text-[16px] leading-[23.2px]" style={{ color: theme.text68 }}>
            {item.body}
          </p>
        </div>
      )}
    </div>
  )
}

export function DictationFeature() {
  return (
    <section className="relative mx-auto h-[2300px] w-[1200px]" style={{ background: theme.feature }}>
      <div className="absolute flex items-center gap-[10px] text-[12px] font-medium uppercase leading-[17.4px] tracking-[0.48px]" style={{ left: 41, top: 48, color: theme.text62 }}>
        <IconTile accent="dictation" icon="mic" />
        {dictationFeature.eyebrow}
      </div>
      <h2
        className={`${theme.serif} absolute text-[48px] font-bold leading-[48px] tracking-[-1.44px]`}
        style={{ left: 41, top: 92, color: theme.ink }}
      >
        {dictationFeature.title[0]}
        <br />
        {dictationFeature.title[1]}
      </h2>
      <p className="absolute w-[524px] text-[18px] leading-[28.8px]" style={{ left: 635, top: 48, color: theme.text62 }}>
        {dictationFeature.body}
      </p>
      <div
        className="absolute bottom-0"
        style={{ left: RAIL_X, top: 288, width: 35, background: '#3e3e3e', boxShadow: 'inset 1px 0 0 #1b1b1b, inset -1px 0 0 #1b1b1b' }}
      >
        <div className="absolute inset-y-0 left-[17px] w-px bg-black" />
      </div>
      <AppList />
      {showcases.map((s) => (
        <ShowcaseItem key={s.top} item={s} />
      ))}
    </section>
  )
}
