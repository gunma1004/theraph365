# -*- coding: utf-8 -*-
import os
import re
import random

# ==============================================================================
# 20종 스팸 회피 세부 테마 키워드 풀
# ==============================================================================
THEME_KEYWORDS_20 = [
    "출장 힐링 마사지", "출장 홈케어 마사지", "출장 릴렉스 마사지", "출장 프리미엄 힐링 마사지", "출장 바디케어 마사지",
    "출장 아로마 마사지", "출장 스웨디시 마사지", "출장 에스테틱 마사지", "출장 오일 테라피 마사지", "출장 딥티슈 마사지",
    "출장 타이 마사지", "출장 홈타이 마사지", "출장 건식 테라피 마사지", "출장 스트레칭 마사지", "출장 지압 힐링 마사지",
    "출장 리커버리 마사지", "출장 피로회복 마사지", "출장 1:1 맞춤형 마사지", "출장 감성 테라피 마사지", "출장 웰니스 마사지"
]

def apply_safe_seo(html_text, loc_name):
    """단독 '출장마사지'를 20종 복합 테마 키워드로 치환 및 SEO 정제"""
    k_samples = random.sample(THEME_KEYWORDS_20, 4)
    k1, k2, k3, k4 = k_samples[0], k_samples[1], k_samples[2], k_samples[3]
    
    # 1. 템플릿 내 단독 출장마사지 및 출장 마사지 정규식 치환
    html_text = re.sub(r'출장\s*마사지\s*&\s*홈타이', f'{k1} & {k2}', html_text)
    html_text = re.sub(r'출장\s*마사지\s*1등', f'{k1} 1등', html_text)
    html_text = re.sub(r'출장\s*마사지', k1, html_text)
    html_text = re.sub(r'출장\s*안마', '홈케어 테라피', html_text)
    
    # 2. 타이틀 & 메타 태그 최신화
    html_text = re.sub(r'<title>.*?</title>', f'<title>{loc_name} {k1} & {k2} 1등 힐링 테라피 | 테라피365</title>', html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*/?>', 
                       f'<meta name="description" content="{loc_name} 전지역 24시간 {k1} 및 {k2} 추천 TOP 5 안내. 30분 내 신속 방문 및 100% 후불제 안심 케어.">', html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r'<meta\s+name=["\']keywords["\']\s+content=["\'].*?["\']\s*/?>', 
                       f'<meta name="keywords" content="{loc_name} {k1}, {loc_name} {k2}, {loc_name} {k3}, 테라피365, {k4}">', html_text, flags=re.DOTALL | re.IGNORECASE)
    
    # 3. OG 태그 갱신
    html_text = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\'].*?["\']\s*/?>', 
                       f'<meta property="og:title" content="{loc_name} {k1} | 24시 프리미엄 힐링 홈케어 - 테라피365">', html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'].*?["\']\s*/?>', 
                       f'<meta property="og:description" content="{loc_name} 전지역 24시간 {k1} 및 {k2} 추천 TOP 5 안내. 30분 내 신속 방문.">', html_text, flags=re.DOTALL | re.IGNORECASE)
    
    return html_text

# 원본 템플릿 로드
template_path = "gangnam/index.html"
if not os.path.exists(template_path):
    template_path = "yongsan/index.html"

with open(template_path, "r", encoding="utf-8", errors="ignore") as f:
    base_html = f.read()

# ==============================================================================
# 1. 금천구 (geumcheon/index.html) 생성
# ==============================================================================
os.makedirs("geumcheon", exist_ok=True)
gc_html = base_html

# 명칭 치환
gc_html = gc_html.replace("강남구", "금천구").replace("강남", "금천")
gc_html = gc_html.replace("용산구", "금천구").replace("용산", "금천")
gc_html = gc_html.replace("gangnam", "geumcheon").replace("yongsan", "geumcheon")

# 금천구 세부 동 매핑 (가산동, 독산동, 시흥동)
gc_html = gc_html.replace("역삼동", "가산동").replace("논현동", "독산동").replace("삼성동", "시흥동")
gc_html = gc_html.replace("대치동", "가산동").replace("청담동", "독산동").replace("압구정동", "시흥동")
gc_html = gc_html.replace("이태원동", "가산동").replace("한남동", "독산동").replace("후암동", "시흥동")
gc_html = gc_html.replace("yeoksam", "gasan").replace("nonhyeon", "doksan").replace("samseong", "siheung")
gc_html = gc_html.replace("itaewon", "gasan").replace("hannam", "doksan")

# 20종 스팸 회피 키워드 패턴 적용
gc_html = apply_safe_seo(gc_html, "금천구")

with open("geumcheon/index.html", "w", encoding="utf-8") as f:
    f.write(gc_html)
print("✔ [geumcheon/index.html] 금천구 20종 안전 키워드 적용 페이지 생성 완료")

# ==============================================================================
# 2. 서울 전지역 (seoul/index.html) 생성
# ==============================================================================
os.makedirs("seoul", exist_ok=True)
seoul_html = base_html

# 명칭 치환
seoul_html = seoul_html.replace("강남구", "서울 전지역").replace("강남", "서울")
seoul_html = seoul_html.replace("용산구", "서울 전지역").replace("용산", "서울")
seoul_html = seoul_html.replace("gangnam", "seoul").replace("yongsan", "seoul")

# 20종 스팸 회피 키워드 패턴 적용
seoul_html = apply_safe_seo(seoul_html, "서울 전지역")

with open("seoul/index.html", "w", encoding="utf-8") as f:
    f.write(seoul_html)
print("✔ [seoul/index.html] 서울 전지역 20종 안전 키워드 적용 페이지 생성 완료")