# 전체 요소 PDF 검수 시트

141개 요소 디자인과 foundation 패널의 전체 시트435장, 크기·모드 샘플3448개를 담았습니다. 전체2151페이지입니다.

각 PDF에는 요소별 책갈피와 클릭 가능한 목록, 라이트·다크 전체 시트, fixture별 A3 확대 페이지, replica 대조 시트가 있습니다. 전체 시트는 원본 해상도를 보존하므로 확대해서 볼 수 있습니다. `MIN`은 fixture의 최소 칸입니다.

| 덱 | 컬렉션 | PDF | 페이지 | 크기 |
|---|---|---|---:|---:|
| 053 | rise-block | [다운로드](rise-block-elements-review.pdf) | 13 | 0.52 MiB |
| 054 | cinder-pulse | [다운로드](cinder-pulse-elements-review.pdf) | 453 | 15.66 MiB |
| 055 | current-fold | [다운로드](current-fold-elements-review.pdf) | 342 | 15.44 MiB |
| 056 | scanline-rise | [다운로드](scanline-rise-elements-review.pdf) | 567 | 20.56 MiB |
| 058 | halo-field | [다운로드](halo-field-elements-review.pdf) | 220 | 11.94 MiB |
| 067 | corner-signal | [다운로드](corner-signal-elements-review.pdf) | 535 | 20.35 MiB |
| 069 | anchor-frame | [다운로드](anchor-frame-elements-review.pdf) | 21 | 0.32 MiB |

검증: 모든 PDF 페이지를 실제 렌더했고, 전체435개 시트의 포함 이미지 픽셀을 원본 PNG와 비교했습니다. 모든 fixture·모드·크기 조합, 확대 영역의 잘림·겹침, 내부 링크를 검사했습니다. 자세한 결과는 [verification.json](verification.json), 출처와 페이지 위치는 [manifest.json](manifest.json)에 있습니다.

이 PDF는 기존 최종 PNG에서 생성했습니다. 기존 replica와 요소 CSS, fixture를 변경하지 않았습니다.

재생성:

```bash
python tools/build_review_pdfs.py
python tools/verify_review_pdfs.py
```

[게시된 PDF 실제 재다운로드 검증](download-verification.json) · [대표 화면 직접 검수](visual-review.json)
