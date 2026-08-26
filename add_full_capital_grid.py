import os
import re

# ==============================================================================
# 수도권 전체 구/동 상세 네비게이션 HTML 컴포넌트
# (메인/서브 어디에 삽입되어도 디자인이 깨지지 않도록 인라인 스타일 보강)
# ==============================================================================
FULL_REGIONS_HTML = """
        <!-- 수도권 전 지역 (서울·인천·경기) 통합 네비게이션 -->
        <div class="area-box" style="margin:35px 0; background:#12151e; border:1px solid #232938; border-radius:14px; padding:24px;">
            <h3 style="font-size:1.18rem; color:#e5b567; font-weight:800; margin-bottom:15px; border-bottom:1px solid #232938; padding-bottom:10px;">📍 테라피365 수도권 전 지역 안내 (서울 · 경기 · 인천)</h3>

            <!-- 1. 서울특별시 25개 자치구 -->
            <div style="font-size:0.98rem; font-weight:800; margin:20px 0 10px; padding-left:8px; border-left:3px solid #e74c3c; color:#ff7675;">[ 서울특별시 25개 자치구 ]</div>
            <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(120px, 1fr)); gap:8px;">
                <div style="background:#161a25; border:1px solid #e74c3c; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/seoul/index.html" style="color:#f1c40f; font-weight:bold; display:block;">★ 서울 전지역</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gangnam/index.html" style="color:#e1e3e8; font-weight:600; display:block;">강남구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/seocho/index.html" style="color:#e1e3e8; font-weight:600; display:block;">서초구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/songpa/index.html" style="color:#e1e3e8; font-weight:600; display:block;">송파구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gangdong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">강동구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/mapo/index.html" style="color:#e1e3e8; font-weight:600; display:block;">마포구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/yongsan/index.html" style="color:#e1e3e8; font-weight:600; display:block;">용산구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/seodaemun/index.html" style="color:#e1e3e8; font-weight:600; display:block;">서대문구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/eunpyeong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">은평구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/jongno/index.html" style="color:#e1e3e8; font-weight:600; display:block;">종로구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/junggu/index.html" style="color:#e1e3e8; font-weight:600; display:block;">중구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/jungnang/index.html" style="color:#e1e3e8; font-weight:600; display:block;">중랑구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/seongbuk/index.html" style="color:#e1e3e8; font-weight:600; display:block;">성북구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gangbuk/index.html" style="color:#e1e3e8; font-weight:600; display:block;">강북구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/dobong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">도봉구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/nowon/index.html" style="color:#e1e3e8; font-weight:600; display:block;">노원구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/seongdong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">성동구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gwangjin/index.html" style="color:#e1e3e8; font-weight:600; display:block;">광진구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/dongdaemun/index.html" style="color:#e1e3e8; font-weight:600; display:block;">동대문구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/yeongdeungpo/index.html" style="color:#e1e3e8; font-weight:600; display:block;">영등포구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/guro/index.html" style="color:#e1e3e8; font-weight:600; display:block;">구로구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/geumcheon/index.html" style="color:#e1e3e8; font-weight:600; display:block;">금천구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/yangcheon/index.html" style="color:#e1e3e8; font-weight:600; display:block;">양천구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gangse/index.html" style="color:#e1e3e8; font-weight:600; display:block;">강서구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/dongjak/index.html" style="color:#e1e3e8; font-weight:600; display:block;">동작구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gwanak/index.html" style="color:#e1e3e8; font-weight:600; display:block;">관악구</a></div>
            </div>

            <!-- 2. 인천광역시 -->
            <div style="font-size:0.98rem; font-weight:800; margin:20px 0 10px; padding-left:8px; border-left:3px solid #3498db; color:#74b9ff;">[ 인천광역시 8개 구/군 ]</div>
            <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(120px, 1fr)); gap:8px;">
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/incheon_bupyeong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">인천 부평구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/incheon_namdong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">인천 남동구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/incheon_yeonsu/index.html" style="color:#e1e3e8; font-weight:600; display:block;">인천 연수구(송도)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/incheon_michuhol/index.html" style="color:#e1e3e8; font-weight:600; display:block;">인천 미추홀구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/incheon_seogu/index.html" style="color:#e1e3e8; font-weight:600; display:block;">인천 서구(청라)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/incheon_gyeyang/index.html" style="color:#e1e3e8; font-weight:600; display:block;">인천 계양구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/incheon_junggu/index.html" style="color:#e1e3e8; font-weight:600; display:block;">인천 중구(영종도)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/incheon_donggu/index.html" style="color:#e1e3e8; font-weight:600; display:block;">인천 동구</a></div>
            </div>

            <!-- 3. 경기도 주요 시/구 -->
            <div style="font-size:0.98rem; font-weight:800; margin:20px 0 10px; padding-left:8px; border-left:3px solid #2ecc71; color:#55efc4;">[ 경기도 주요 시·구 ]</div>
            <div style="display:grid; grid-template-columns:repeat(auto-fill, minmax(120px, 1fr)); gap:8px;">
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/suwon/index.html" style="color:#e1e3e8; font-weight:600; display:block;">수원시 전체</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/suwon_paldal/index.html" style="color:#e1e3e8; font-weight:600; display:block;">수원 팔달구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/suwon_yeongtong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">수원 영통구(광교)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/seongnam/index.html" style="color:#e1e3e8; font-weight:600; display:block;">성남시 전체</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/seongnam_bundang/index.html" style="color:#e1e3e8; font-weight:600; display:block;">성남 분당구(판교)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/goyang/index.html" style="color:#e1e3e8; font-weight:600; display:block;">고양시 전체</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/goyang_ilsandong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">고양 일산동구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/yongin/index.html" style="color:#e1e3e8; font-weight:600; display:block;">용인시 전체</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/yongin_suji/index.html" style="color:#e1e3e8; font-weight:600; display:block;">용인 수지구</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/bucheon/index.html" style="color:#e1e3e8; font-weight:600; display:block;">부천시</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/hwaseong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">화성시(동탄)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/pyeongtaek/index.html" style="color:#e1e3e8; font-weight:600; display:block;">평택시(고덕)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/siheung/index.html" style="color:#e1e3e8; font-weight:600; display:block;">시흥시(배곧)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gimpo/index.html" style="color:#e1e3e8; font-weight:600; display:block;">김포시(구래)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/paju/index.html" style="color:#e1e3e8; font-weight:600; display:block;">파주시(운정)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/namyangju/index.html" style="color:#e1e3e8; font-weight:600; display:block;">남양주시(다산)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/uijeongbu/index.html" style="color:#e1e3e8; font-weight:600; display:block;">의정부시</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/hanam/index.html" style="color:#e1e3e8; font-weight:600; display:block;">하남시(미사)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gwangmyeong/index.html" style="color:#e1e3e8; font-weight:600; display:block;">광명시(철산)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/anyang/index.html" style="color:#e1e3e8; font-weight:600; display:block;">안양시(평촌)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/ansan/index.html" style="color:#e1e3e8; font-weight:600; display:block;">안산시(중앙)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gunpo/index.html" style="color:#e1e3e8; font-weight:600; display:block;">군포시(산본)</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/guri/index.html" style="color:#e1e3e8; font-weight:600; display:block;">구리시</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/osan/index.html" style="color:#e1e3e8; font-weight:600; display:block;">오산시</a></div>
                <div style="background:#161a25; border:1px solid #232938; padding:10px 6px; border-radius:6px; text-align:center;"><a href="/gwangju_gyeonggi/index.html" style="color:#e1e3e8; font-weight:600; display:block;">경기 광주시</a></div>
            </div>
        </div>
"""

# 타깃 파일 리스트 (필요 시 모든 서브페이지 폴더 추가 가능)
target_files = ["index.html", "seoul/index.html"]

for rel_path in target_files:
    if not os.path.exists(rel_path):
        print(f"⚠ [{rel_path}] 파일이 존재하지 않아 건너뜁니다.")
        continue
    
    with open(rel_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1) 기존 .area-box 영역이 있으면 해당 영역만 정확하게 교체
    if '<div class="area-box"' in content:
        content = re.sub(r'<div class="area-box".*?</div>\s*</div>(?=\s*</div>\s*<footer>|\s*<footer>)', 
                         FULL_REGIONS_HTML.strip(), content, flags=re.DOTALL)
    # 2) 서브페이지의 구 자치구 리스트 형태가 있을 경우 교체
    elif '<div class="gu-grid">' in content:
        content = re.sub(r'<div class="gu-grid">.*?</div>', FULL_REGIONS_HTML.strip(), content, flags=re.DOTALL)
    # 3) 없을 경우 푸터 직전 container 닫는 태그 앞에 안전하게 삽입
    else:
        content = re.sub(r'(\s*</div>\s*<footer>)', rf'\n{FULL_REGIONS_HTML}\n\1', content, flags=re.DOTALL)

    with open(rel_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"✔ [{rel_path}] 수도권 통합 네비게이션 적용 완료!")