# Hello AI Hackathon — 참가팀 운영 대시보드

## 프로젝트 개요
삼성전자 System LSI **People팀**이 사내 **Hello AI Hackathon** 참가팀을 조회·관리하는 단일 페이지 대시보드.
- 순수 바닐라 **HTML/CSS/JS** (프레임워크·빌드 런타임 없음, 폰트 CDN만 사용)
- 성격: **조회 중심** 운영 도구 — 검색 · 상태/트랙 필터 · 정렬 · 팀 상세 패널
- **최종본 = `dashboard-v3.html`** (아래 "ver3" 섹션). v1(`dashboard.html`)·v2(`dashboard-v2.html`)는 이전 버전(보관). 셋 다 `teams.js` 공용, 조회 로직 동일.

## 파일 구조
| 파일 | 역할 |
|---|---|
| `dashboard-v3.html` | **★ 최종본 (v3)** — Tailwind CDN + Pretendard + Iconify Solar, 라이트 테마·짙은 블루 액센트·하단 블루 물결 (아래 "ver3" 섹션). 동일 `teams.js` 로드 |
| `dashboard-v2.html` | v2 중간본 — 리퀴드글래스/바다 (아래 "ver2" 섹션, 보관용) |
| `dashboard.html` | v1 원본 — `samsung-tech-design` 밝은 테마. `teams.js` 를 `<script src>` 로 로드 |
| `teams.js` | 데이터. `window.AXC_TEAMS` 배열(50팀 더미). v1·v2·v3 공용. **실데이터 교체 대상** |
| `dashboard-standalone.html` | **빌드 산출물**. `teams.js` 를 인라인 병합한 단일 파일(미리보기·공유·배포용). 직접 편집 금지 |
| `gen.py` | 더미 데이터 재생성 (seed 고정 → 항상 동일한 50팀) |
| `build.py` | `dashboard.html` + `teams.js` → `dashboard-standalone.html` 병합 |

## 실행 / 빌드
```bash
# 개발: 같은 폴더에 dashboard.html + teams.js 를 두고 브라우저로 dashboard.html 열기
#       <script src> 방식이라 file:// 더블클릭으로도 동작 (fetch 아님 → CORS 없음)

python3 gen.py     # 더미 데이터 재생성 → teams.js
python3 build.py   # 단일 파일 빌드 → dashboard-standalone.html
```
> **원칙:** `dashboard.html`(v1) 또는 `teams.js` 를 수정하면 반드시 `python3 build.py` 를 다시 실행해 standalone 을 갱신할 것. standalone 은 산출물이므로 손으로 고치지 말 것.
> `build.py` 는 **v1(`dashboard.html`)만** 대상 — `dashboard-v2.html` 은 standalone 산출물이 없고 `teams.js` 를 `<script src>` 로 직접 로드(더블클릭 동작). v2 를 빌드 대상에 포함할지는 미정(TODO).

## 데이터 스키마 (`window.AXC_TEAMS: Team[]`)
```
Team = {
  no,          // 1~50
  id,          // "HAI-001"
  name,        // 팀명
  org,         // 소속(개발실/팀)
  track,       // 트랙
  leader,      // 팀장 이름
  members,     // 인원 수
  memberList,  // [{ name, role }]  (0번째가 팀장)
  intro,       // 팀 소개 문단
  project,     // 프로젝트명
  desc,        // 프로젝트 설명
  status,      // 진행상태 (아래 STATUS_ORDER 중 하나)
  submitted,   // 제출 여부(boolean)
  score,       // 심사 점수 0~100 | null(미심사)
  award,       // 수상 등급 | null
  repo,        // 제출물 링크
  updated      // "YYYY-MM-DD"
}
```

## 도메인 값
- **진행상태 (STATUS_ORDER, 순서 유지):** `접수완료 → 선정중 → 미선정 → 과제 진행 → 제출완료 → 본선 심사 → 결선 심사`
- **트랙:** 설계 자동화 / 검증·테스트 / 수율·공정 / 문서·지식 / 업무 자동화 / 고객·영업
- **수상 등급:** AI Impact / AI Innovation / AI Insight / AI Inspiration / AI Ignition
- **조직:** SOC·CIS·모뎀·DDI·PMIC 개발실, 상품기획실, S/W개발실, 품질보증팀, 경영지원실, People팀

## 디자인 시스템 (samsung-tech-design)
- **밝은 테마**, 흰 배경 + 삼성 블루 `#1428a0` **단일 강조색**
- 폰트: **Manrope**(본문·UI), **JetBrains Mono**(숫자·ID·날짜 등 메타 전용)
- 규칙: 블루 외 강조색 금지 · `border-radius ≤ 12px` · 본문에 이모지/장식 아이콘 금지
- 토큰은 `dashboard.html` 상단 `:root` 블록 참조

## ver3 (`dashboard-v3.html`) — ★ 최종본
`taste-skill` 기반 신규 디자인. **로직·데이터·기능은 v1/v2와 동일**(아래 "구현 노트" 적용). Tailwind 유틸 클래스 + JS 마크업으로 구성.
- **스택 (CDN 필요 · 완전 오프라인 불가):** Tailwind CSS CDN · **Pretendard** · **Iconify Solar** 아이콘(`<iconify-icon>`) · JetBrains Mono(숫자). 이모지 없음.
- **테마:** 라이트. `bg-slate-100` + 블루 mesh 앰비언트(`.ambient`) + grain 오버레이 + **하단 블루 물결**(`.waves`, 3겹 SVG `roll`+`bob`, `fixed z-index:-10`, `#93b4ff→#4e86f0→#1d4ed8`).
- **액센트:** 짙은 블루 단일(`blue-600/700`) — 브랜드·아이콘·칩 active·정렬·행 hover·CTA·링크·포커스·파비콘. 상태 색은 별개 유지(결선심사만 accent 블루).
- **표면:** 흰 글래스 카드 `.glass`(= `white/.72` + slate 테두리 + 소프트 섀도 + inset 하이라이트).
- **레이아웃:** 스티키 글래스 nav → 인사 헤더 → KPI 4타일(grid) → 컨트롤 → 리스트(`max-h-[62dvh]` 내부 스크롤 · thead sticky · thin 스크롤바) → 상세 드로어. `max-w-7xl` · `min-h-[100dvh]` · `break-keep`.
- **상태 pill:** JS `STATUS_STYLE` 맵(상태 → Tailwind 색 클래스). **v1/v2 의 `.st-*` CSS 방식 아님.**
- **KPI:** `renderKpis` 가 Iconify 아이콘 + 타이틀/서브 생성(제출률 서브 = `제출수/전체` 실데이터).
- **모션:** 로드 stagger fade-up(`.reveal` + `--d`) · CTA hover/active scale · dot pulse · 파도. 전부 `prefers-reduced-motion` 정지.
- **a11y:** `:focus-visible` 링 · 행/헤더 키보드(Enter/Space) · `aria-sort` · `role=dialog`+포커스 이동/복귀 · 검색 `aria-label`.
- **빌드:** standalone 없음(`build.py` 는 v1 전용). CDN 로드라 `file://` 직접 열기 동작(단 인터넷 필요).

## ver2 (`dashboard-v2.html`) — 리퀴드글래스 리디자인 (중간본, 보관)
Aura 대시보드를 참고한 시각 리스킨. **로직·데이터·기능은 v1과 동일**(아래 "구현 노트" 그대로 적용). CSS + 마크업 구조 + `renderKpis` 마크업만 다름. 토큰은 v2 파일 상단 `:root` 참조.
- **컨셉:** 바다 배경 위에 떠 있는 반투명 프로스티드 유리 셸 + 투명 카드.
- **배경 (`.seascape`, `position:fixed; z-index:-1`):** `index.html` 의 바다 모션 이식.
  - `.sea` — 수직 그라디언트(상단 밝음 `#F2F7FF` → 하단 블루 `#4E93E0`). 상단은 밝게 유지, 아래만 파랑.
  - `.swell s1~s3` — 하단 앵커 방사형 스웰, `sway-a/b` 로 드리프트(하단에만 배치, 상단 스웰 없음).
  - `.waves w1~w3` — 하단 파도 3겹 SVG, `roll`(가로 순환) + `bob`(상하) + `blur`. 셸이 backdrop-filter 로 프로스팅하고, 셸 하단 여백(`margin-bottom`)으로 크리스프 파도 노출.
  - 포인터 패럴럭스: `--mx/--my`(@property) → `.waterscape` 이동. 별도 `<script>`.
- **셸 (`.app`):** 반투명(`rgba(255,255,255,.28)`) + `backdrop-filter blur` + 렌즈형 inset 그림자(상/좌 하이라이트, 하/우 블루 굴절)로 리퀴드글래스 굴곡. `overflow:hidden` 으로 라운드 클립 → **내부 스크롤 컨테이너는 `.main`**.
- **레이아웃 고정 + 리스트만 스크롤:** `.main { display:flex; flex-direction:column; overflow:hidden }`. 상단(topbar·KPI·컨트롤·resultmeta·foot) 고정, `.table-card` 가 남는 높이 차지, **`.table-scroll` 만 세로 스크롤**. `thead th { position:sticky; top:0 }` 로 헤더 고정.
- **커스텀 오버레이 스크롤바 (`.oscroll`):** native 스크롤바 숨김(`scrollbar-width:none` + `::-webkit-scrollbar{display:none}`) → **레이아웃 공간 0**. JS 가 `.table-card`(relative)에 썸 하나 생성 → 스크롤/호버 시 `.show`, idle 900ms 후 페이드아웃. 드래그 가능. `#tbody` MutationObserver 로 행 수 변동 시 재계산. (native 로는 "공간 미점유 + 자동 페이드" 동시 보장 불가해 직접 구현)
- **사이드바:** 좌측 아이콘 레일. **네비 항목은 장식** — 단일 뷰 도구라 실제 라우팅 없음.
- **KPI:** 흰 반투명 카드 + 틴트 아이콘 타일 + 서브라인. `renderKpis` 가 `SVG` 아이콘 맵 + 타이틀/서브 생성(제출률 서브는 `제출수/전체` 실데이터). **v1 대비 이 함수만 마크업 확장.**
- **v1 규칙과의 의도적 이탈:** `samsung-tech-design` 의 "밝은 단색 블루 / `radius ≤ 12px` / 이모지·장식 금지" 는 **v2 에 미적용**(리퀴드글래스 컨셉). v2 강조색은 `#2b6bff` 계열.
- **reduced-motion:** 바다·스웰·파도·패럴럭스·상태 dot pulse·hover transform 정지, 오버레이 썸 페이드 즉시.

## 구현 노트 (이어서 작업 시 필독)
1. **상태 추가·변경 시 반드시 동기화** — 놓치면 pill 색상이 누락됨(실제로 겪은 버그):
   - `dashboard.html`·`dashboard-v2.html` 의 `STATUS_ORDER` 배열 + `.st-<상태>` CSS 클래스 (**공백 제거형**)
   - `dashboard-v3.html` 의 `STATUS_ORDER` 배열 + `STATUS_STYLE` 맵(상태 → Tailwind 색 클래스)
   - `teams.js` / `gen.py` 의 상태값
2. **상태 pill 클래스 규칙:** `"st-" + status.split(" ").join("")` 로 생성. 따라서 CSS 클래스명도 공백을 뺀 형태(`.st-과제진행`, `.st-본선심사`, `.st-결선심사`). (정규식 이스케이프 함정 때문에 `split/join` 사용)
3. **No. 열**은 "현재 표시 순서" 기준이라 정렬·필터 시 재계산됨. 팀 고유번호가 필요하면 `t.no` 사용.
4. **상태 칩 카운트**는 검색 + 트랙 필터를 적용한 뒤 기준으로 계산.
5. **KPI:** '심사 진행중' = 본선 심사 + 결선 심사, '제출 완료율' = `submitted` 비율.
6. **검색 대상:** 팀명·팀장·소속·프로젝트·ID·트랙·**팀원 이름**.
7. **렌더링은 `innerHTML` 기반.** 현재는 신뢰 데이터라 무방하지만, 외부 입력이 섞이면 HTML 이스케이프를 추가할 것.
8. **상세 패널:** 행 클릭으로 열림, `ESC`/오버레이 클릭으로 닫힘. 팀 소개(`intro`) + 팀원 명단(`memberList`, 역할 포함) 표시.

## 향후 작업 후보 (TODO)
- [ ] `teams.js` 를 실제 참가팀 데이터로 교체 (스키마 유지)
- [ ] 상태 편집 기능(운영자가 진행상태 변경) + 변경 이력
- [ ] **UI 편집 → `teams.js` 반영** — 정적·`file://` 특성상 브라우저가 파일을 직접 못 씀(자동 갱신 불가). 방안 택1: ① 수정본 `teams.js` **다운로드(export)** 후 수동 교체(어디서나 동작, 추천) · ② **File System Access API** 로 직접 덮어쓰기(Chrome/Edge, `localhost`/https 필요) · ③ `localStorage`(파일 미변경, 세션 유지). (미구현)
- [ ] CSV 내보내기
- [ ] 뷰 전환(테이블 ↔ 카드)
- [x] 행 키보드 접근성(`tabindex`/`role`, Enter 로 상세 열기) — v2·v3 완료 (v1 미적용)
- [ ] 데이터 소스 연동(API 또는 CSV import) 및 갱신 흐름
- [ ] v3(최종)를 표준 배포본으로 확정 시 v1/v2 정리 여부 결정 (현재 보관 중)
