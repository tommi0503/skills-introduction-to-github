# GitHub ZIP 재다운로드 검증

업로드된 ZIP 5개를 GitHub의 immutable commit `0f061dbbd07a74fd2612fbb6060d34242edc75ce`에서 HTTPS로 다시 다운로드했다. 작업 디렉터리의 ZIP을 복사해 원격 다운로드라고 표시하지 않았다.

- 검증 시각: 2026-10-06T18:14:27.428748+00:00
- 5개 ZIP byte 수·SHA-256·CRC 모두 통과
- 최종 PNG 1,057장의 SHA-256 및 1280×720 header 모두 통과
- 참고 시트 117개, native 참고 crop 1,057개, 개별 원본/결과 비교 1,057개 확인
- 20장 단위 미리보기53개·덱별탐색미리보기47개·offline preview.html 확인

각 ZIP 다운로드 URL·byte 수·SHA·결과는 github-download-verification.json에 기록했다. 원격 검증 기록은 ZIP 업로드 이후 작성되므로 소스의 후속 커밋으로 제공한다. ZIP 안에는 빌드·전체 브라우저 검사·개별 시각 검수 기록이 포함되어 있다.
