# 최종 소스와 재검수

각 `*-project/<collection>/`의 CSS·JSON·fixture가 최종 원본입니다. `*-project/tools/`의 생성·보정 스크립트는 작업 경과를 남긴 것입니다. 초기 생성기를 단독 실행하면 후속 보정이 사라질 수 있으므로, 최종 컬렉션을 대상으로 공식 preview와 통합 렌더러를 실행하세요.

필요 패키지는 requirements.txt에 있으며 Chromium 실행 파일이 필요합니다. 이 세션에서는 `/usr/bin/chromium`을 사용했습니다.

```sh
python -m http.server 8765 --bind 127.0.0.1 --directory .
# 별도 터미널에서
python render.py vectorbox all
```

`render.py`는 컬렉션과 해당 `assets/`의 실제 폰트·측정 토큰·팔레트·Lucide를 읽습니다. 원본 이미지 폴더가 없으면 보관된 비교 PNG의 왼쪽1280×720을 원본 비교용으로 읽습니다. 이를 슬라이드 HTML 배경으로 사용하지 않습니다.

`reference/`에는 제공 계약·preview 도구·허용 fixture 마크업을 보관했습니다. 예시 디자인 CSS는 포함하지 않았습니다. 공식 CLI는 다음과 같이 실행할 수 있습니다.

```sh
python reference/tools/preview.py vectorbox-project/vectorbox reference/contract/type-steps.json --out light.html
python reference/tools/preview.py vectorbox-project/vectorbox reference/contract/type-steps.json --dark --out dark.html
```

collection ZIP은 Rhetis용으로 외부 리소스를 포함하지 않습니다. review ZIP은 독립 HTML 검토에 필요한 폰트·플랫폼 공급부·컬렉션 소스를 함께 포함합니다. 압축을 푼 뒤 그 폴더만 localhost 서버로 제공해 열면 됩니다.
