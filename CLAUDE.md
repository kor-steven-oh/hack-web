# CLAUDE.md

이 파일은 이 저장소에서 작업할 때 Claude Code(claude.ai/code)에 지침을 제공한다.

## 프로젝트

정적 단일 페이지 사이트 — 빌드 시스템 없음, 패키지 매니저 없음, 의존성 없음.

- `index.html` — 자체 완결형 히어로 페이지 (인라인 CSS; 외부 리소스는 Google Fonts "Unbounded" 디스플레이 서체 + Pretendard CDN뿐).

## 개발

브라우저에서 바로 열기: `open index.html`

## 컨벤션

- **모든 페이지의 기본 폰트는 Pretendard.** CDN으로 로드하고(`https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css`) `font-family` 스택 맨 앞에 지정(`'Pretendard', ...`); 뒤에 OS 폰트 폴백 유지.
- 페이지는 자체 완결형 유지 (CSS/JS를 HTML 파일에 인라인).
- 디자인 토큰은 `:root` CSS 변수에 정의(`--sky-*`, `--ink`, `--accent`) — 새 색상은 여기서 파생.
- 애니메이션은 transform만 사용하고 `prefers-reduced-motion: reduce`에서 반드시 비활성화.

<!-- ASTRYX:START -->
Astryx v0.1.3 · 149 components
CLI: run every command as `npx astryx <cmd>` (shown below as `astryx ...`).

SETUP (once, in your app entry e.g. main.tsx) — without these, components render unstyled:
  import "@astryxdesign/core/reset.css";
  import "@astryxdesign/core/astryx.css";

WORKFLOW — discover, don't guess. Before writing UI:
1. `astryx build "<idea>"` — START HERE: returns a kit (closest [page] + [block]s + [component]s). No args = full playbook.
2. `astryx template <name> [--skeleton]` — scaffold the [page]/[block]s it named, or study their layout. Templates are reference code.
3. `astryx component <Name>` — props + examples for every component you use.

RULES:
- No <div> — components do all layout/spacing. Full page → AppShell; sidebar nav → SideNav.
- Frame first: pick the shell (AppShell / Layout+LayoutPanel) and budget regions in px BEFORE writing content (`astryx docs layout`).
- Dense data = rows (Table, List/Item) edge-to-edge — never Card-wrapped list items. Card = dashboard widgets, galleries, settings groups only.
- Status → StatusDot/Token; Badge only for counts and enumerated states, never decoration.
- Custom styling: component props first; else style/className with tokens — var(--color-*|--spacing-*|--radius-*). No raw hex/px. (No StyleX/Tailwind compiler here — don't use xstyle/utility classes.)
- Tokens for every value (`astryx docs tokens`). Brand/accent via `astryx theme` — never override --color-* in :root.

MORE CLI:
  search "<query>"   find any component / hook / doc / template / block
  component --list   149 components by category
  template --list    page + block recipes
  docs <topic>       color, elevation, icons, illustrations, layout, migration, motion, principles, shape, spacing, styling, theme, tokens, typography
  swizzle <Name>     eject component source for deep customization
  upgrade --apply    run after any @astryxdesign/core bump
<!-- ASTRYX:END -->
