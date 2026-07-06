"""
빌드: dashboard.html + teams.js  →  dashboard-standalone.html
teams.js 를 <script> 안에 인라인해 단일 파일로 만듭니다 (미리보기/공유/배포용).

실행: python3 build.py
※ dashboard.html 또는 teams.js 를 수정했다면 반드시 다시 실행해 standalone 을 갱신하세요.
   standalone 은 빌드 산출물이므로 직접 편집하지 마세요.
"""
html = open("dashboard.html", encoding="utf-8").read()
data = open("teams.js", encoding="utf-8").read()

marker = '<script src="teams.js"></script>'
assert marker in html, "dashboard.html 에서 teams.js 참조를 찾지 못했습니다."

merged = html.replace(marker, "<script>\n" + data.rstrip() + "\n</script>")
assert 'src="teams.js"' not in merged, "외부 참조가 남아있습니다."
assert "window.AXC_TEAMS" in merged

with open("dashboard-standalone.html", "w", encoding="utf-8") as f:
    f.write(merged)

print(f"빌드 완료 → dashboard-standalone.html ({len(merged):,} bytes)")
