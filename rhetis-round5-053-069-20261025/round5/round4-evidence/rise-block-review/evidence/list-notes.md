# List 첫줄 정렬 검수

- row 전체의 top에 붙던 절대 위치 bullet/num을 제거했다. name의 첫 line-box와 marker가 같은 grid 첫 행에 놓이고, note는 다음 행을 쓴다. name/note가 여러 줄이어도 marker가 첫 이름 줄에서 떨어지지 않는다.
- inferred item의 중앙 text-group 위치는 유지했다. 관찰된 cinder inline row, current 81px medallion, scanline source 두 줄의 원래 수치와 자식 구성은 별도로 보존했다. 도구/foundation/source-map/다른 요소를 수정하지 않았다.
- 정식 light/dark 모든 허용 칸 16상태에서 glyph·겹침·대비·paint·폰트 경고0, stale0이며 출력 SHA가 audit과 일치한다. rise bullet/num 확대 PNG에서 첫줄 정렬을 직접 확인했다.
