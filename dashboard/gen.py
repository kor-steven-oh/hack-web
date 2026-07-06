"""
Hello AI Hackathon — 참가팀 더미 데이터 생성기
실행: python3 gen.py  →  teams.js 생성 (window.AXC_TEAMS 배열)
seed 고정으로 항상 동일한 50팀을 재현합니다. 실제 데이터로 교체 시 이 파일은 참고용.
"""
import random, json, datetime

random.seed(42)

ORGS = ["SOC개발실", "CIS개발실", "모뎀개발실", "DDI개발실", "PMIC개발실",
        "상품기획실", "S/W개발실", "품질보증팀", "경영지원실", "People팀"]
TRACKS = ["설계 자동화", "검증/테스트", "수율/공정", "문서/지식", "업무 자동화", "고객/영업"]
# 진행 단계 순서 (대시보드 STATUS_ORDER 와 반드시 동일하게 유지)
STATUS = ["접수완료", "선정중", "미선정", "과제 진행", "제출완료", "본선 심사", "결선 심사"]
AWARDS = ["AI Impact", "AI Innovation", "AI Insight", "AI Inspiration", "AI Ignition"]

TEAM_NAMES = ["반도체 요정들","실리콘 밸리","웨이퍼 메이커","트랜지스터","클럭 게이터","팹리스 파이터즈","넷리스트","야근 구조대","프롬프트 연금술사","에이전트 어벤저스","게이트키퍼","무어의 법칙","딥다이브","로직 락","커널 패닉","실리콘 드리머스","칩 위스퍼러","논블로킹","래치업","슈뢰딩거의 칩","오버클럭커","타이밍 클로저","리키지 헌터스","스택 오버플로우","세그폴트","히든 레이어","그래디언트","토큰 마스터","컨텍스트 윈도우","파인튜너스","벡터 서치","임베딩","어텐션 이즈 올","제로샷","체인 오브 소트","실리콘 마인드","AX 파이오니어","코드네임 나노","펨토초","엣지 케이스","빌드 브레이커즈","머지 컨플릭트","핫픽스","롤백 스쿼드","커밋 크루","리팩터링 길드","테크 데뷰터","언더클럭","패리티 비트","라스트 커밋"]
LASTNAMES = list("김이박최정강조윤장임한오서신권황안송류전홍")
GIVEN = ["민준","서연","도윤","지우","예준","하은","시우","서준","하윤","지호","지훈","수빈","현우","은지","준서","다현","윤서","건우","채원","성민","지원","유진","태현","소율","우진","가은","민서","동현","예린","시윤"]
ROLES = ["팀장", "백엔드", "프론트엔드", "데이터/ML", "기획/PM", "도메인 전문가", "디자인"]

PROJECT_BY_TRACK = {
    "설계 자동화": ["RTL 자동 리뷰 에이전트", "SDC 제약조건 자동 생성기", "레이아웃 DRC 어시스턴트", "IP 재사용 추천 엔진"],
    "검증/테스트": ["테스트벤치 자동 생성기", "커버리지 갭 분석 에이전트", "회귀 테스트 트리아지 봇", "웨이퍼 결함 분류 모델"],
    "수율/공정": ["수율 이상 조기탐지 대시보드", "공정 파라미터 최적화 코파일럿", "설비 로그 이상탐지", "불량 원인 RCA 어시스턴트"],
    "문서/지식": ["설계 스펙 Q&A 봇", "사내 지식 검색 에이전트", "회의록 자동 요약기", "온보딩 지식맵 생성기"],
    "업무 자동화": ["실행품의서 자동 작성기", "주간보고 자동 집계", "메일 분류·초안 어시스턴트", "일정·리소스 조율 봇"],
    "고객/영업": ["고객 기술문의 응대 봇", "경쟁사 스펙 비교 리포터", "영업 제안서 초안 생성기", "VOC 감성분석 대시보드"],
}
DESC = {
    "설계 자동화": "반복적인 설계 검토·제약조건 작업을 LLM 에이전트로 자동화하여 설계 리드타임을 단축하는 것을 목표로 합니다.",
    "검증/테스트": "검증 단계의 수작업 비중을 줄이고, 결함을 조기에 분류·재현하여 검증 사이클을 가속화합니다.",
    "수율/공정": "공정·설비 데이터에서 이상 신호를 조기에 포착하고 근본원인 분석을 지원해 수율 손실을 최소화합니다.",
    "문서/지식": "흩어진 사내 문서·스펙을 검색·요약·질의응답 형태로 연결해 지식 접근성을 높입니다.",
    "업무 자동화": "품의·보고·메일 등 반복 행정 업무를 자동화하여 실무자의 몰입 시간을 확보합니다.",
    "고객/영업": "고객 문의 대응과 제안 활동을 AI로 보조해 응대 품질과 속도를 동시에 개선합니다.",
}
INTRO_TPL = [
    "{org} 소속 실무자들이 모여 결성한 팀으로, 현업에서 겪은 {track} 과제를 직접 해결하고자 참가했습니다.",
    "서로 다른 직군이 모인 크로스펑셔널 팀입니다. {track} 영역의 비효율을 AI로 개선하는 데 집중합니다.",
    "{org}의 데이터와 도메인 지식을 바탕으로 {track} 문제를 현실적으로 풀어내는 것을 목표로 합니다.",
    "AI 활용 경험이 있는 멤버들이 모여, {track} 업무에 바로 적용 가능한 도구를 만드는 것을 지향합니다.",
]

def kor_name():
    return random.choice(LASTNAMES) + random.choice(GIVEN)

# 상태 분포 (대회 중후반 시점 가정) — 합계 50
status_plan = (["접수완료"] * 3 + ["선정중"] * 4 + ["미선정"] * 7 + ["과제 진행"] * 9 +
               ["제출완료"] * 11 + ["본선 심사"] * 10 + ["결선 심사"] * 6)
random.shuffle(status_plan)
assert len(status_plan) == 50

award_pool = (["AI Impact"] * 1 + ["AI Innovation"] * 2 + ["AI Insight"] * 2 +
              ["AI Inspiration"] * 2 + ["AI Ignition"] * 2)
random.shuffle(award_pool)

names = TEAM_NAMES[:]
random.shuffle(names)

base = datetime.date(2026, 6, 1)
teams = []
ai = 0
for i in range(50):
    status = status_plan[i]
    track = random.choice(TRACKS)
    org = random.choice(ORGS)
    members = random.randint(3, 6)
    leader = kor_name()
    mem = [{"name": leader, "role": "팀장"}]
    pool = ROLES[1:][:]
    random.shuffle(pool)
    for j in range(members - 1):
        mem.append({"name": kor_name(), "role": pool[j % len(pool)]})

    submitted = status in ("제출완료", "본선 심사", "결선 심사")
    if status == "결선 심사":
        score = random.randint(85, 98)
    elif status == "본선 심사":
        score = random.randint(78, 92)
    elif status == "미선정":
        score = random.randint(55, 74)
    else:
        score = None

    award = None
    if status == "결선 심사" and ai < len(award_pool):
        award = award_pool[ai]; ai += 1

    off = {"접수완료": (1, 5), "선정중": (3, 8), "미선정": (6, 12), "과제 진행": (10, 20),
           "제출완료": (20, 25), "본선 심사": (25, 30), "결선 심사": (30, 35)}[status]
    upd = base + datetime.timedelta(days=random.randint(*off))

    teams.append({
        "no": i + 1,
        "id": f"HAI-{i+1:03d}",
        "name": names[i],
        "org": org,
        "track": track,
        "leader": leader,
        "members": members,
        "memberList": mem,
        "intro": random.choice(INTRO_TPL).format(org=org, track=track),
        "project": random.choice(PROJECT_BY_TRACK[track]),
        "desc": DESC[track],
        "status": status,
        "submitted": submitted,
        "score": score,
        "award": award,
        "repo": f"https://git.internal/hai/hai-{i+1:03d}",
        "updated": upd.isoformat(),
    })

header = """// =============================================================
//  Hello AI Hackathon — 참가팀 더미 데이터 (50팀)
//  자동 생성(gen.py). 실제 운영 시 이 배열을 실제 데이터로 교체하세요.
//  스키마: no, id(HAI-001), name, org, track, leader, members,
//    memberList[{name,role}], intro, project, desc, status,
//    submitted, score(0~100|null), award(등급|null), repo, updated
//  진행상태: 접수완료 > 선정중 > 미선정 > 과제 진행 > 제출완료 > 본선 심사 > 결선 심사
// =============================================================
window.AXC_TEAMS = """

with open("teams.js", "w", encoding="utf-8") as f:
    f.write(header)
    f.write(json.dumps(teams, ensure_ascii=False, indent=2))
    f.write(";\n")

from collections import Counter
print("총 팀:", len(teams))
print("상태 분포:", dict(Counter(t["status"] for t in teams)))
print("수상:", dict(Counter(t["award"] for t in teams if t["award"])))
