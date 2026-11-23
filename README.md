# 주신당 강남점 PB 프렙 계산기

병 수(또는 만들 g)만 입력하면 재료별 계량값이 나오는 PB 프렙 계산기.

- 사이트: `index.html` (GitHub Pages로 배포)
- 레시피 데이터: `src/data.json`
- 화면/계산 로직: `src/template.html`

## 수정 방법

1. `src/data.json`(레시피) 또는 `src/template.html`(화면) 수정
2. `python3 src/build.py` 실행 → `index.html` 재생성
3. 커밋 후 `main`에 푸시하면 1~2분 뒤 사이트에 반영
