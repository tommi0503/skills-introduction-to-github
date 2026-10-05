export interface Sight {
  name: string
  body: string[]
  photoLabel: string
}

export const culture = {
  number: '03',
  title: '제주의 문화 관광지',
  sights: [
    {
      name: '이호테우 말등대',
      body: [
        '빨간색과 하얀색의 말 모양 등대가 이국적인 풍경을 자',
        '아냅니다. 특히 아름다운 일몰 명소로 유명하며, 사진',
        '찍기 좋은 포토 스팟으로 많은 방문객들이 찾습니다.',
      ],
      photoLabel: 'lighthouse photo',
    },
    {
      name: '한라수목원',
      body: [
        '제주시내권에 위치하여 사계절 내내 방문하기 좋은 수',
        '목원입니다. 다양한 식물과 아름다운 산책로를 갖추고',
        '있으며, 죽림원 대나무 숲은 대표적인 포토존으로 유명',
        '합니다.',
      ],
      photoLabel: 'bamboo forest photo',
    },
  ] satisfies Sight[],
}

export const contact = {
  label: '관광안내',
  lines: ['+123-456-7890', 'hello@reallygreatsite.com', 'www.reallygreatsite.com'],
}

export const cover = {
  title: ['JEJU', 'TRAVEL:'],
  subtitle: '푸른 섬, 감성의 제주',
}
