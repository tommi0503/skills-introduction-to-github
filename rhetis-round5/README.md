# Rhetis 디자인 라이브러리 · ROUND5

[전체 미리보기](index.html) · [실제 폴더별 출처](ORIGINS.md) · [최종 통합 검증](integration-verification.md)

|덱|컬렉션|페이지|실제 디자인|컬렉션 ZIP|검수 ZIP|Light PDF|Dark PDF|
|---|---|---:|---:|---|---|---|---|
|069|[vectorbox](vectorbox-project/index.html)|12|18|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/vectorbox.zip)|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/vectorbox-review.zip)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/vectorbox-library-light.pdf)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/vectorbox-library-dark.pdf)|
|072|[seedmark](seedmark-project/index.html)|21|39|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/seedmark.zip)|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/seedmark-review.zip)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/seedmark-library-light.pdf)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/seedmark-library-dark.pdf)|
|073|[crossrail](crossrail-project/index.html)|30|35|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/crossrail.zip)|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/crossrail-review.zip)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/crossrail-library-light.pdf)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/crossrail-library-dark.pdf)|
|074|[meridian-deck](meridian-deck-project/index.html)|30|40|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/meridian-deck.zip)|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/meridian-deck-review.zip)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/meridian-deck-library-light.pdf)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/meridian-deck-library-dark.pdf)|
|078|[onboard-docket](onboard-docket-project/index.html)|19|27|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/onboard-docket.zip)|[다운로드](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/onboard-docket-review.zip)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/onboard-docket-library-light.pdf)|[PDF](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/onboard-docket-library-dark.pdf)|

사용자 승인에 따라 소스·미리보기·ZIP·검수 PDF를 기존 작업을 보존하는 일반 git 커밋으로 게시한다. 이미지·PDF·폰트·압축파일을 뺀 [소스 전용 ZIP](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/rhetis-round5-source.zip)과 [전체 검수 PDF398쪽](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/main/rhetis-round5/deliverables/all-elements-review.pdf)을 제공한다. PDF는 요소당 한 페이지이며 foundation·패널도 포함한다. 최종 PNG의 압축 픽셀 스트림을 그대로 넣어 축소·JPEG 변환·잘림 없이 보존했다.

사용자 ROUND5 계약을 우선한다. 독립 디자인은 `<leaf>--<design>` 폴더로 등록하며 원형 없는 일반 요소를 강제로 채우지 않는다. 지도는 페이지의 논리 요소·foundation 패널·배경을 위에서 아래로 기록한다. 자료 속 문구는 지시로 취급하지 않았다.

컬렉션 ZIP에는 최상위 컬렉션 폴더 하나와 `.css .json .md .html`만 들어 있다. 검수 ZIP에는 실제 라이트·다크 크기 시트, map에 대응하는 원형 대조, foundation과 전용 panel 크기 시트, 원본|불변 replica|조립3열, 조립 HTML/PNG, 불변 replica 소스/PNG/PDF(원래 존재한 것), 로컬 폰트·아이콘, 디자인 언어·ROUND5 보고·검수 기록·GAPS·동적 출처표가 들어 있다. 크기별 검사 JSON은 기본으로 담으며, native cell PNG는 옵션으로 추가할 수 있다.

검수 ZIP을 풀고 `index.html`을 열면 오프라인으로 볼 수 있다. 모든 HTML/CSS 의존 파일은 로컬에 있으며 페이지 PNG는1280×720,3열 비교는3840×720이다. 크기 시트와 panel 시트는 fixture 수와 허용 칸 수에 따른 실제 크기를 갖는다. 각 PNG와 ZIP의 SHA·크기는 manifest에 기록한다.

```sh
# 최종 렌더·주 검수 기록 뒤, 현재 source FP와 전체 증거 검사
python tools/integration_verify.py --refresh-audits
# 파일을 바꾸지 않고 패키지 누락/오프라인 의존성 조사
python tools/package.py --dry-run
# 검수 viewer와 원본 출처표만 갱신
python tools/package.py --dry-run --write-previews
# 통합 검사 통과 후10개 ZIP 생성
python tools/package.py
# 다운로드한 ZIP에도 같은 CRC/경로/manifest/PNG 검사
python tools/package.py --verify deliverables/*.zip
```

도구의 기본 입력 경로는 이 소스 ROOT와 `reference/`다. 재렌더 도구의 원본 슬라이드 입력은 `tools/reassembly.py`의 `ORIGINALS` 상수로 명시한다. ZIP 생성과 검증은 디자인 source·fixture·map·replica를 변경하지 않는다. 실제 API 게시와 게시 후 재다운로드 검증은 별도 절차이며, 이 도구는 게시 성공을 추정하지 않는다.
