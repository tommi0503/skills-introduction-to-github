import { Abs, ImagePlaceholder, Slide, type DeckDefinition } from '../../ui'
import { theme as t } from './theme'
import { cover, tech, growth, model } from './data'
import { Box, Head, Lines, Pill } from './components'

const F = 'font-pretendard'

function Cover() {
  return (
    <Slide background="#fff" className={F}>
      <ImagePlaceholder className="absolute inset-0" tone="#f0f0f0" />
      <Abs x={72} y={78} className="text-[44px] font-bold leading-[64px]"><Lines lines={cover.title} /></Abs>
      <Abs x={72} y={512} className="text-[20px] leading-[34px]"><Lines lines={cover.tag} /></Abs>
      <Abs x={72} y={610} w={123} h={40} className="flex items-center justify-center bg-black text-[16px] text-white">{cover.cta}</Abs>
      <Abs x={780} y={616} w={422} className="text-right text-[13px] leading-[16px] text-[#999]"><Lines lines={cover.copy} /></Abs>
    </Slide>
  )
}

function Tech() {
  return (
    <Slide background="#fff" className={F}>
      <Head part={tech.part} title={tech.title} sub={tech.sub} />
      <Abs x={279} y={157} className="text-[20px] font-bold">고객 이슈</Abs>
      <Abs x={279} y={362} className="text-[20px] font-bold leading-[34px]">기능<br />우선순위</Abs>
      {tech.cols.map((c) => (
        <div key={c.x}>
          <Abs x={c.x} y={160} w={395} h={171} style={{ background: '#f2f2f2' }}>
            <div className="mt-[34px] text-center"><Pill>{c.pill}</Pill></div>
            <Lines lines={c.lines} className="mt-3 text-center text-[17px] leading-[30px] text-[#aaa]" />
          </Abs>
          <Abs x={c.x + 50} y={278} className="flex items-center rounded-full border-[1.5px] border-black bg-white px-3 py-[3px] text-[17px] font-bold"><span className="mr-1 size-[9px] rounded-full" style={{ background: t.red }} />{c.hl}</Abs>
          <Abs x={c.x + 195} y={308} w={1} h={70} className="bg-black" />
          <Abs x={c.x} y={366} w={395} h={126} className="border border-[#e5e5e5] text-center">
            <div className="mt-[28px]"><Pill black>{c.fn}</Pill></div>
            <div className="mt-[18px] text-[17px]">{c.desc}</div>
          </Abs>
          <ImagePlaceholder className="absolute" style={{ left: c.x, top: 492, width: 395, height: 179 }} />
        </div>
      ))}
    </Slide>
  )
}

function Growth() {
  return (
    <Slide background="#fff" className={F}>
      <Head part={growth.part} title={growth.title} sub={growth.sub} />
      <Abs x={281} y={154} className="text-[26px] font-bold">{growth.head}</Abs>
      <Abs x={326} y={242} w={234} h={234} className="flex items-center justify-center rounded-full border border-black text-[19px]">{growth.left}</Abs>
      <Abs x={473} y={285} className="rounded-full px-3 py-[5px] text-[14px] font-bold text-white" style={{ background: t.red }}>{growth.badge}</Abs>
      <Abs x={954} y={242} w={234} h={234} className="flex items-center justify-center rounded-full bg-black text-[19px] text-white">{growth.right}</Abs>
      <Abs x={560} y={236} className="text-[130px] font-thin leading-none text-[#ddd]">{'{'}</Abs>
      <Abs x={900} y={236} className="text-[130px] font-thin leading-none text-[#ddd]">{'}'}</Abs>
      {growth.mid.map(([a, b], i) => (
        <Abs key={a} x={655} y={[228, 340, 452][i]} w={200} className="text-center">
          <div className="text-[19px] font-bold">{a}</div><div className="text-[13px] text-[#999]">{b}</div>
          {i < 2 && <div className="mt-[10px] text-[20px] text-[#555]">↓</div>}
        </Abs>
      ))}
      {growth.boxes.map((b, i) => (
        <Abs key={i} x={[281, 761][i]} y={548} w={469} h={118} className="flex flex-col items-center justify-center bg-[#f3f3f3] text-center text-[17px] leading-[22px] text-[#555]">
          {b.map((l, j) => <div key={l} className={j === b.length - 1 ? 'font-bold text-black' : ''}>{l}</div>)}
        </Abs>
      ))}
    </Slide>
  )
}

function Model() {
  const m = model
  const rows = [243, 343, 443]
  const hs = [90, 90, 87]
  return (
    <Slide background="#fff" className={F}>
      <Head part={growth.part} title={growth.title} sub={m.sub} />
      <Abs x={281} y={154} className="text-[26px] font-bold">{m.head}</Abs>
      {[[285, 171], [474, 233], [771, 188], [1025, 205]].map(([x, w], i) => (
        <Abs key={i} x={x} y={208} w={w} className={`text-center text-[17px] ${i === 3 ? 'font-bold' : 'text-[#888]'}`}>{m.cols[Math.min(i, 2) === 2 && i === 3 ? 2 : i === 0 ? 0 : i === 1 ? 0 : 1]}</Abs>
      ))}
      {m.a.map(([k, v], i) => (
        <Box key={k} x={285} y={rows[i]} w={171} h={hs[i]} className={`flex flex-col items-center justify-center text-[16px] font-bold ${i === 2 ? 'bg-black text-white' : i === 1 ? 'bg-[#f2f2f2]' : 'bg-white'}`}><div>{k}</div><div>{v}</div></Box>
      ))}
      {m.b.map((r, i) => (
        <Box key={i} x={474} y={rows[i]} w={233} h={hs[i]} className="flex flex-col items-center justify-center bg-white text-[14px] leading-[16px]">
          <div className="text-[16px] font-bold">{r[0]}</div>{r.slice(1).map((l) => <div key={l} className="text-[#555]">{l}</div>)}
        </Box>
      ))}
      <Box x={771} y={245} w={188} h={86} className="flex flex-col items-center justify-center border-[#ddd] bg-[#f2f2f2] text-[16px] font-bold"><div>{m.c[0][0]}</div><div>{m.c[0][1]}</div></Box>
      <Box x={771} y={343} w={188} h={173} className="flex flex-col items-center justify-evenly border-[#ddd] bg-[#f2f2f2] text-[16px] font-bold">
        <Lines lines={m.c[1].slice(0, 2)} /><Lines lines={m.c[1].slice(2)} />
      </Box>
      <Abs x={1025} y={243} w={205} h={287} className="bg-black" />
      {m.d.map((d, i) => <Abs key={d} x={1043} y={[278, 419][i]} w={170} h={44} className="flex items-center justify-center rounded-full bg-white px-3 text-center text-[14px] font-bold leading-[14px]">{d}</Abs>)}
      {[[738, 276], [738, 392], [738, 490], [986, 285], [986, 440]].map(([x, y], i) => <Abs key={i} x={x} y={y} className="text-[19px] text-[#bbb]">→</Abs>)}
      <Abs x={287} y={572} className="text-[17px] font-medium leading-[34px]">{m.bullets.map((b) => <div key={b}>● {b}</div>)}</Abs>
    </Slide>
  )
}

const deck: DeckDefinition = { id: '30', title: '올투비 사업계획서', slides: [Cover, Tech, Growth, Model] }
export default deck
