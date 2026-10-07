# GitHub 개선본 ZIP 재다운로드 검증

게시된 커밋의 ZIP을 HTTPS로 실제 다시 내려받아 검사했습니다. 로컬 ZIP을 복사하여 검사한 결과가 아닙니다.

- 아티팩트 커밋: `cac3617aa806227a95e76ddf5dc2296c77f90761`
- 검증 시각(UTC): 2026-10-07T05:15:48.263527+00:00
- ZIP 5개: 게시 파일과 다운로드 파일의 바이트 수·SHA-256 일치, 전체 ZIP CRC 통과
- 최종 PNG 1,057개: 전부 1280×720, PNG SHA-256 모두 일치
- 원본 시트 117개, 개별 참고 crop 1,057개, 개별 비교 1,057개
- 20장 단위 미리보기 53개 및 전체 미리보기 HTML 확인

| 다운로드 | 크기(MiB) | SHA-256 |
| --- | ---: | --- |
| [presentation5-clone-quality-v2-part-01.zip](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/cac3617aa806227a95e76ddf5dc2296c77f90761/presentation5-clone-quality-v2-part-01.zip) | 92.88 | `dc12965b77268d11efe25d86168bc8aff0ddff936751eaa50008666fd4146273` |
| [presentation5-clone-quality-v2-part-02.zip](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/cac3617aa806227a95e76ddf5dc2296c77f90761/presentation5-clone-quality-v2-part-02.zip) | 93.00 | `34875ddc492021e5ed53baed5a55220ea0768d62b465b9a5f621394271813e05` |
| [presentation5-clone-quality-v2-part-03.zip](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/cac3617aa806227a95e76ddf5dc2296c77f90761/presentation5-clone-quality-v2-part-03.zip) | 93.05 | `e9559fa5ae162edb850e7fc32b47f9b8805f95e18e47a9c350e3d599e1964d70` |
| [presentation5-clone-quality-v2-part-04.zip](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/cac3617aa806227a95e76ddf5dc2296c77f90761/presentation5-clone-quality-v2-part-04.zip) | 92.96 | `a2465e773d90972267f2b2cd70a18fc0278f2f2c9b78710964e6a80d3411414f` |
| [presentation5-clone-quality-v2-part-05.zip](https://raw.githubusercontent.com/tommi0503/skills-introduction-to-github/cac3617aa806227a95e76ddf5dc2296c77f90761/presentation5-clone-quality-v2-part-05.zip) | 84.20 | `2c053d23fc8a9efa8f2f38639f668c361b6b93b3a62a2dc8f2a7ddc7c512bdc8` |

자기 자신의 해시를 ZIP 안에 넣는 순환을 피하기 위해 이 재다운로드 증빙은 게시 이후 별도 커밋으로 저장합니다. ZIP에는 생산 렌더·개별 비교·자동 검사 및 시각 검수 기록이 포함되어 있습니다.
