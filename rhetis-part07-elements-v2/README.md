# Rhetis 디자인 라이브러리 v2

첨부 이미지의5개 덱을 각각56요소 컬렉션으로 만들었습니다. 불변 replica에서 요소를 측정하고, 직접 대응과 추론을 구분했습니다. [미리보기](index.html)와 [280요소 출처](ORIGINS.md)를 먼저 볼 수 있습니다.

|덱|컬렉션|원본 페이지|다운로드|검수|
|---|---|---:|---|---|
|069|[vectorbox](vectorbox-project/index.html)|12|[collection](deliverables/vectorbox.zip)|[review](deliverables/vectorbox-review.zip)|
|072|[seedmark](seedmark-project/index.html)|21|[collection](deliverables/seedmark.zip)|[review](deliverables/seedmark-review.zip)|
|073|[crossrail](crossrail-project/index.html)|30|[collection](deliverables/crossrail.zip)|[review](deliverables/crossrail-review.zip)|
|074|[meridian-deck](meridian-deck-project/index.html)|30|[collection](deliverables/meridian-deck.zip)|[review](deliverables/meridian-deck-review.zip)|
|078|[onboard-docket](onboard-docket-project/index.html)|19|[collection](deliverables/onboard-docket.zip)|[review](deliverables/onboard-docket-review.zip)|

컬렉션 ZIP은 컬렉션 폴더 하나와 `.css .json .md .html`만 포함합니다. 검수 ZIP은 `index.html`을 중심으로 collection·로컬 assets·map·foundation-sheets의1280×720 양모드 PNG 및 foundation-checks 보고·선택적으로 공식preview HTML·요소별 light/dark PNG·실제 mapped base/variant의 replica 비교 PNG·조립 HTML/PNG·원본/불변 replica/조립3열 PNG·GAPS·검수 기록·디자인 언어·출처 표를 포함합니다. 불변 replica 원본 소스는 Git의 각 프로젝트 `replica/`에 유지합니다.

PNG 크기는 검증 manifest에 실제 값으로 기록합니다. 조립 페이지는1280×720,3열 비교는3840×720이며 요소 시트는 fixture와 크기 칸 수에 따라 더 큽니다. PNG를 눌러100%·확대·이동으로 읽을 수 있습니다. 검수 ZIP은 압축을 푼 뒤 오프라인으로 열 수 있고, 폰트와 아이콘 런타임을 외부에서 받지 않습니다.

`GAPS.md`는 현 계약으로 표현하지 못한 구조와 필요한 계약을 기록합니다. 크기별 기능 검사와 원본 일치 판단은 다른 항목이며, 자료의 본문을 작업 지시로 취급하지 않았습니다. 추론 요소를 원본에 있었다고 표시하지 않습니다.

```sh
# ZIP을 만들지 않고 누락/용량/크기를 조사하고 미리보기만 갱신
python tools/package.py --dry-run --write-previews

# 소스 동결과 최종 렌더 후 실행
python tools/package.py

# 내려받은 ZIP에도 동일하게 적용 가능
python tools/package.py --verify deliverables/*.zip
```

[최종 통합 검증](integration-verification.md)은 모든 요소·fixture·시트의 현재 fingerprint,6자 문구 분리,원본 해시 보존을 집계한다. 이전 author 요약은 이 통합 보고서로 대체한다.

최종 생성은 CRC·경로·파일 SHA·PNG 크기·오프라인 참조를 검사하고, 각 review ZIP100MB 미만을 강제합니다. 파일 목록과 SHA는 review 안 `verification/package-manifest.json`, 외부 `deliverables/*-manifest.json`과 `SHA256SUMS`에 기록합니다. 모든 입력은 읽기만 하고 collection·map·sheets·assembly·assets·기존v1을 변경하지 않습니다.
