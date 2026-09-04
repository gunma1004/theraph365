# -*- coding: utf-8 -*-
import os
import re

# 원본 템플릿 로드
template_path = "gangnam/index.html"
if not os.path.exists(template_path):
    template_path = "yongsan/index.html"

with open(template_path, "r", encoding="utf-8", errors="ignore") as f:
    base_html = f.read()

def apply_fixed_seo(html_text, loc_name):
    """단독/복합 키워드를 무조건 '{지역명} 출장마사지' 형식으로 고정 치환"""
    # 타이틀 & 메타 태그 최신화
    html_text = re.sub(r'<title>.*?</title>', f'<title>{loc_name} 출장마사지 - 24시 프리미엄 힐링 홈케어 | 테라피365</title>', html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r'<meta\s+name=["\']description["\']\s+content=["\'].*?["\']\s*/?>', 
                       f'<meta name="description" content="{loc_name} 전지역 24시간 출장마사지 추천. 30분 내 신속 방문 및 100% 후불제 안심 케어.">', html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r'<meta\s+name=["\']keywords["\']\s+content=["\'].*?["\']\s*/?>', 
                       f'<meta name="keywords" content="{loc_name} 출장마사지, {loc_name} 홈타이, 테라피365">', html_text, flags=re.DOTALL | re.IGNORECASE)
    
    # OG 태그 갱신
    html_text = re.sub(r'<meta\s+property=["\']og:title["\']\s+content=["\'].*?["\']\s*/?>', 
                       f'<meta property="og:title" content="{loc_name} 출장마사지 | 24시 프리미엄 홈케어 - 테라피365">', html_text, flags=re.DOTALL | re.IGNORECASE)
    html_text = re.sub(r'<meta\s+property=["\']og:description["\']\s+content=["\'].*?["\']\s*/?>', 
                       f'<meta property="og:description" content="{loc_name} 전지역 24시간 출장마사지 추천. 30분 내 신속 방문.">', html_text, flags=re.DOTALL | re.IGNORECASE)
    
    return html_text

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

# 고정 출장마사지 키워드 적용
gc_html = apply_fixed_seo(gc_html, "금천구")

with open("geumcheon/index.html", "w", encoding="utf-8") as f:
    f.write(gc_html)
print("✔ [geumcheon/index.html] 금천구 '금천구 출장마사지' 형식 적용 완료")

# ==============================================================================
# 2. 서울 전지역 (seoul/index.html) 생성
# ==============================================================================
os.makedirs("seoul", exist_ok=True)
seoul_html = base_html

# 명칭 치환
seoul_html = seoul_html.replace("강남구", "서울 전지역").replace("강남", "서울")
seoul_html = seoul_html.replace("용산구", "서울 전지역").replace("용산", "서울")
seoul_html = seoul_html.replace("gangnam", "seoul").replace("yongsan", "seoul")

# 고정 출장마사지 키워드 적용
seoul_html = apply_fixed_seo(seoul_html, "서울 전지역")

with open("seoul/index.html", "w", encoding="utf-8") as f:
    f.write(seoul_html)
print("✔ [seoul/index.html] 서울 전지역 '서울 전지역 출장마사지' 형식 적용 완료")